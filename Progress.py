import streamlit as st

def app():
    col1,col2,col3=st.columns(3)
    col1.write("Steps:")
    col2.write("Screen Time:")
    col3.write("Mood:")