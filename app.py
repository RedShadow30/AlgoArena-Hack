import streamlit as st
st.set_page_config(page_title="KindBites", page_icon="🍽️", layout="centered")
from multiapp import MultiApp
from apps import market, articles, chatbot



app = MultiApp()

css_style = """
<style>
  .stApp {
    background: linear-gradient(to right, #00B822, #00ADE6); /* Green to Blue gradient */
  }
</style>
"""

st.markdown(css_style, unsafe_allow_html=True)
st.markdown("""
# Welcome to KindBites 🍜🍕🍫

Pitch here!

""")


app.add_app("Market", market.app)
app.add_app("Articles", articles.app)
app.add_app("Chatbot", chatbot.app)

app.run()
