from pathlib import Path
import sys

import streamlit as st
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.storage import db

def dashboard():
    st.title("Space Weather Dashboard")

    col1, col2, col3 = st.columns(3)

    last_plasma = db.get_latest_n_plasma(1)
    last_mag = db.get_latest_n_mag(1)
    last_kp = db.get_latest_n_kp(1)

    with col1:
        st.metric("Solar Wind Speed", last_plasma[-1][2] if last_plasma else "N/A")
    with col2:
        st.metric("Latest bz", last_mag[-1][1] if last_mag else "N/A")
    with col3:
        st.metric("Latest Kp", last_kp[-1][1] if last_kp else "N/A")

    n_plasma = 300
    plasma_rows = db.get_latest_n_plasma(n_plasma)

    n_mag = 300
    mag_rows = db.get_latest_n_mag(n_mag)

    n_kp = 50
    kp_rows = db.get_latest_n_kp(n_kp)

    st.write(f"plasma rows : {len(plasma_rows)}")
    st.write(f"mag rows : {len(mag_rows)}")
    st.write(f"kp rows : {len(kp_rows)}")

    plasma_df = pd.DataFrame(plasma_rows)
    mag_df = pd.DataFrame(mag_rows)
    kp_df = pd.DataFrame(kp_rows)

    st.subheader("Plasma Data")
    st.dataframe(plasma_df)

    st.subheader("Magnetic Field Data")
    st.dataframe(mag_df)

    st.subheader("Kp Index Data")
    st.dataframe(kp_df)

if __name__ == '__main__':
    dashboard()
