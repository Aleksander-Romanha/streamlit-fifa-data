import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏻‍♂️",
    layout="wide"
)

df_data = st.session_state["data"]

clubs = df_data["Club"].unique()
selected_club = st.sidebar.selectbox("Club", clubs)

df_players = df_data[df_data["Club"] == selected_club]
players = df_players["Name"].unique()
slected_player = st.sidebar.selectbox("Player", players)

player_stats = df_data[df_data["Name"] == slected_player].squeeze()

st.image(player_stats["Photo png"])
st.title(player_stats["Name"])

st.markdown(f"**Club:** {player_stats['Club']}")
st.markdown(f"**Position:** {player_stats['Position']}")

col1, col2, col3, col4, = st.columns(4)
col1.markdown(f"**Age:** {player_stats['Age']}")
col2.markdown(f"**Height (m):** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Weight (kg):** {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Value", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Weekly Wage", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Release Clause", value=f"£ {player_stats['Release Clause(£)']:,}")