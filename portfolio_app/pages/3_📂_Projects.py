import streamlit as st
st.set_page_config(page_title="Projects", page_icon="📂")

st.markdown("""<style>
[data-testid="stAppViewContainer"] { background: linear-gradient(120deg, #e0f7fa, #b3e5fc); }
</style>""", unsafe_allow_html=True)

st.title("📂 My Projects")
projects = {"Library Management System": "A Streamlit-based system for managing library books, tracking borrowed items, and organizing student records.", "Mini App Calculator": "A simple application that performs basic arithmetic operations, designed for quick and easy calculations."}
for name, desc in projects.items():
    with st.expander(name): st.write(desc)