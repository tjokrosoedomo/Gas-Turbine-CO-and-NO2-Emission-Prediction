import streamlit as st
import requests


st.title("Aplikasi Pengecekan Emisi NOx dan CO")
AT = st.number_input("Ambient Temperature (degC)")
AP = st.number_input("Ambient Pressure (mbar)")
AH = st.number_input("Ambient Humidity (%)")
AFDP = st.number_input("Air Filter Difference Pressure (mbar)")
GTEP = st.number_input("Gas Turbine Exhaust Pressure (mbar)")
TIT = st.number_input("Turbine Inlet Temperature (degC)")
TAT = st.number_input("Turbine After Temperature (degC)")
TEY = st.number_input("Turbine Energy Yield (MWH)")
CDP = st.number_input("Compressor Discharge Pressure (mbar)")


# inference
data = {"AT":AT, 
        "AP":AP,
        "AH":AH,
        "AFDP":AFDP,
        "GTEP":GTEP,
        "TIT":TIT,
        "TAT":TAT,
        "CDP":CDP,
        "TEY":TEY}

URL = "https://milestone-2-tjokrosoedomo-10.herokuapp.com/"

# komunikasi
r = requests.post(URL, json=data)
res = r.json()
if res['code'] == 200:
    st.title(res['result'])