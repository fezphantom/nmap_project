import streamlit as st
import pandas as pd
from parser import parse_nmap_xml, classify_risk  # 🔥 THIS IS THE LINK

st.title("🔐 Nmap Security Dashboard")

file = st.file_uploader("Upload Nmap XML", type=["xml"])

if file:
    results = parse_nmap_xml(file)  # 🔥 using your parser

    df = pd.DataFrame(results)

    df["risk"] = df.apply(lambda x: classify_risk(x["port"], x["state"]), axis=1)

    st.dataframe(df)
