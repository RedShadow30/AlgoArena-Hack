import streamlit as st

st.set_page_config(page_title="Welcome to KindBites", page_icon="👋", layout="centered")
st.sidebar.text("Made with ❤️‍🔥 by KindBites Team")

css_style = """
<style>
  .stApp {
    background: linear-gradient(to right, #00B822, #00ADE6); /* Green to Blue gradient */
  }
</style>
"""

st.markdown(css_style, unsafe_allow_html=True)
st.markdown("# Welcome to KindBites 🍜🍕🍫")

l_col, c_col, r_col = st.columns([1, 7, 7])

with c_col:
  st.image("pages/images/FoodShelter.jpg", caption="Credit: Getty Images, Copyright: Steve Debenport", width=500)

st.markdown("""
KindBites turns food waste into hope. We connect restaurants with surplus meals to people in need—using AI to ensure safety, trust, and speed. 
Fighting hunger with every donation.
""")

left_col, center_col, right_col = st.columns([1.5, 3, 1])
with center_col:
  st.markdown("**Don't waste it, KindBite it** 😉")
