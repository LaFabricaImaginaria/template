import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
now = date.now()

from code.shared_functions import skip_echo

def display():
    _, c1, c2, _ = st.columns([2,7,3,2])
    with c1:
        repo_path = "https://raw.githubusercontent.com/sebastiandres/talk_2021_11_pyconcl/main/images"
        
        
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("# Reporte Mensual  2022")
        st.markdown("## Walmart Chile")
        st.markdown("# Estrategia Digital & RRSS")
        st.markdown("##### Presentación realizada en streamlit (:exploding_head: *streamlit-ception*)")
        st.write(".format(now.month),.format(now.year)")

    with c2:
        st.image("images/streamlit_cl.png")
