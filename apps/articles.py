import streamlit as st

def app():
    st.title("🍽️ Food Spoilage Tips")

    st.markdown("### Choose a food category:")

    # Create a horizontal row of emoji buttons
    col1, col2, col3, col4 = st.columns(4)

    # Session state to store the active category
    if "category" not in st.session_state:
        st.session_state.category = "Produce"

    with col1:
        if st.button("🍎 Produce"):
            st.session_state.category = "Produce"
    with col2:
        if st.button("🥛 Dairy"):
            st.session_state.category = "Dairy"
    with col3:
        if st.button("🥩 Meat"):
            st.session_state.category = "Meat"
    with col4:
        if st.button("🍞 Baked Goods"):
            st.session_state.category = "Baked Goods"

    # Display the selected category’s tips
    category = st.session_state.category

    if category == "Produce":
        st.subheader("🍎 Produce Spoilage Signs")
        st.markdown("""
        - Slimy or mushy texture  
        - Brown or dark spots on leafy greens  
        - Foul or sour odor  
        - Mold growth, especially on berries  
        """)
    elif category == "Dairy":
        st.subheader("🥛 Dairy Spoilage Signs")
        st.markdown("""
        - Sour smell (especially with milk or cream)  
        - Curdling or clumping in liquids  
        - Yellowing of cheese or unusual mold growth  
        - Swollen or puffed packaging  
        """)
    elif category == "Meat":
        st.subheader("🥩 Meat Spoilage Signs")
        st.markdown("""
        - Sticky, slimy film on the surface  
        - Grey or green discoloration  
        - Rotten or sulfur-like smell  
        - Dull appearance  
        """)
    elif category == "Baked Goods":
        st.subheader("🍞 Baked Goods Spoilage Signs")
        st.markdown("""
        - Visible mold (green, blue, white fuzz)  
        - Hardening or staleness  
        - Off smell from fillings  
        - Unusual sogginess or stickiness  
        """)

    st.info("📘 Come back often as we keep this guide updated to help prevent foodborne illness.")
