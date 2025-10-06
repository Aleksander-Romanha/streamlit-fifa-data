import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data_mod.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA 2023 OFFICIAL DATASET! ⚽")
st.sidebar.markdown("Developed by [Aleksander](https://github.com/Aleksander-Romanha)")

btn = st.button("Access data on Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
    The dataset of football players from 2023 provides
    comprehensive information about professional football players.
    It contains a wide range of attributes, including player demographics,
    physical characteristics, game statistics, contract details, and
    club affiliations.

    With **over 17,000 records**, this dataset offers a valuable resource for
    football analysts, researchers, and enthusiasts interested in exploring various
    aspects of the football world. It enables the study of player attributes,
    performance metrics, market valuation, club analysis, player positioning,
    and player development over time.
"""
)