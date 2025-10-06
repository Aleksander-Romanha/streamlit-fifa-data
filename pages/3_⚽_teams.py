import streamlit as st
import pandas as pd
import base64

st.set_page_config(
    page_title="Players",
    page_icon="⚽",
    layout="wide"
)

df_data = st.session_state["data"]

clubs = df_data["Club"].unique()
selected_club = st.sidebar.selectbox("Club", clubs)

df_filtered = df_data[df_data["Club"] == selected_club].set_index("Name")

st.image(df_filtered["Club Logo png"].values[0])
st.markdown(f"## {selected_club}")

def encode_image(image_path):
    if image_path:
        with open(image_path, "rb") as image_file:
            raw_base64 = base64.b64encode(image_file.read()).decode("utf-8")
            return f"data:image/png;base64,{raw_base64}"
df_filtered["Photo png b64"] = df_filtered["Photo png"].apply(encode_image)
df_filtered["Flag png b64"] = df_filtered["Flag png"].apply(encode_image)

columns = ["Age", "Photo png b64", "Flag png b64", "Overall", 'Value(£)', 'Wage(£)', 'Joined',
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Weekly Wage", format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()
                 ),
                 "Photo png b64": st.column_config.ImageColumn("Photo"),
                 "Flag png b64": st.column_config.ImageColumn("Flag"),
             })