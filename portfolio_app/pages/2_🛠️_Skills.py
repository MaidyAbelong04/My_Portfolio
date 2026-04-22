import streamlit as st
st.set_page_config(page_title="Skills", page_icon="🛠️")

st.markdown("""<style>
[data-testid="stAppViewContainer"] { background: linear-gradient(120deg, #e0f7fa, #b3e5fc); }
.skill-container { background: white; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
</style>""", unsafe_allow_html=True)

st.title("🛠️ Skills")
for skill, val in {"Python": 90, "Java": 80, "Frontend": 85}.items():
    st.markdown(f'<div class="skill-container"><b>{skill}</b></div>', unsafe_allow_html=True)
    st.progress(val)