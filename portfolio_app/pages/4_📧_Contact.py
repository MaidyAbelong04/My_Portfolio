import streamlit as st
import streamlit.components.v1 as components

# Setup ng page
st.set_page_config(page_title="Contact Me", page_icon="📧", layout="wide")

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #e0f2f7; 
    }
    </style>
""", unsafe_allow_html=True)

st.title("📧 Get in Touch")
st.write("Feel free to reach out for inquiries, collaborations, or any opportunities.")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Send a Message")
    
    components.html("""
    <style>
        .container { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        input, textarea { width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ccc; border-radius: 8px; box-sizing: border-box; }
        button { width: 100%; background-color: #7d3cff; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; }
    </style>
    <div class="container">
        <form action="https://api.web3forms.com/submit" method="POST">
            <input type="hidden" name="access_key" value="e8f8f1de-b311-4d4b-8877-485283f3985d">
            <input type="text" name="name" placeholder="Enter your full name" required>
            <input type="email" name="email" placeholder="Enter your email address" required>
            <textarea name="message" placeholder="Write your message here..." required></textarea>
            <button type="submit">Send Message</button>
        </form>
    </div>
    """, height=350)

with col2:
    st.subheader("Connect with Me")
    st.write("You can also find me here:")
    st.link_button("🌐 GitHub", "https://github.com/MaidyAbelong04")
    st.link_button("📱 Facebook", "https://www.facebook.com/maidy.abelong.7")
    st.markdown("---")
    st.info("📍 **Location:** Masbate, Philippines")