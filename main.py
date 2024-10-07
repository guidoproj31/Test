import streamlit as st

st.write("hello world")
st.title("CSV Checker")
uploaded_file = st.file_uploader("Choose a file", type="csv")