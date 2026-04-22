import streamlit as st
import os
import base64

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "maidy.jpg")

st.set_page_config(page_title="Maidy E. Abelong", layout="centered")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: #e3f2fd; 
    }

    .midnight-card {
        display: flex;
        align-items: center;
        gap: 40px;
        padding: 50px;
        background: rgba(255, 255, 255, 0.8);
        border-radius: 30px;
        margin-top: 50px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    }

    .profile-pic {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #fbbf24; /* Gold Border */
        box-shadow: 0 0 15px rgba(251, 191, 36, 0.2);
    }

    .text-area h1 { color: #1e293b; font-size: 2.5rem; margin: 0; }
    .text-area h3 { color: #d97706; font-size: 1.2rem; margin: 10px 0; letter-spacing: 1px; font-weight: 700; }
    .text-area p { color: #334155; font-size: 1.1rem; line-height: 1.6; }
    
    /* 5. Button */
    div.stButton > button {
        background: #fbbf24;
        color: #1e293b;
        border: none;
        padding: 12px 30px;
        border-radius: 50px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- CONTENT ---
st.markdown('<div class="midnight-card">', unsafe_allow_html=True)

if os.path.exists(image_path):
    with open(image_path, "rb") as image_file:
        img_b64 = base64.b64encode(image_file.read()).decode()
    st.markdown(f'<img src="data:image/jpeg;base64,{img_b64}" class="profile-pic">', unsafe_allow_html=True)

st.markdown("""
    <div class="text-area">
        <h1>Hello I'm Maidy E. Abelong</h1>
        <h3>CS STUDENT | ASPIRING WEB DEVELOPER</h3>
        <p>Passionate about creating simple, useful, and accessible mobile and web applications.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
if st.button("Explore My Work"):
    st.balloons()