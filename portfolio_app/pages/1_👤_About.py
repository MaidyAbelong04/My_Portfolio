import streamlit as st
st.set_page_config(page_title="About Me", page_icon="👤")

st.markdown("""<style>
[data-testid="stAppViewContainer"] { background: linear-gradient(120deg, #e0f7fa, #b3e5fc); }
.card { background: white; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
</style>""", unsafe_allow_html=True)

st.title("👤 About Me")
st.markdown('<div class="card">An aspiring developer currently studying Computer Science at DEBESMSCAT, with a strong interest in creating impactful digital solutions.</div>', unsafe_allow_html=True)

st.subheader("🎓 Education")
st.markdown('<div class="card">Bachelor of Science in Computer Science, DEBESMSCAT - PRESENT 2023</div>', unsafe_allow_html=True)

st.subheader("🚀 Goals")
st.markdown('<div class="card">• To become a skilled Mobile Developer <br>• To build modern and responsive Web Applications</div>', unsafe_allow_html=True)