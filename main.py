import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(
    page_title="Readme",
    page_icon="👋",
)

st.write("# Prototpye test page! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Superdisco 프로토타입 예시입니다. 데이터는 오픈소스를 사용했습니다.
    **👈 Select a demo from the sidebar** to see some examples
   
"""
)