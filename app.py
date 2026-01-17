from streamlit_qrcode_scanner import qrcode_scanner  
import streamlit as st

qr_code = qrcode_scanner(key='qrcode_scanner')  

if qr_code:  
    st.write(qr_code) 
