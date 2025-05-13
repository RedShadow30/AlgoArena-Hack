import streamlit as st

def app():
    #st.set_page_config(page_title="Articles", page_icon="📚", layout="wide")

    st.title("Food Spoilage Tips")
    st.markdown("""
<style>
/* Make the base HTML, body, and root containers black */
html, body, .stApp {
    background-color: black !important;
}

/* Override Streamlit's main content wrapper */
[data-testid="stAppViewContainer"] {
    background-color: black !important;
}

/* Also force the background on block container which wraps all columns */
.css-1y4p8pa {
    background-color: black !important;
}

/* Optional: make sidebar black too, if used */
[data-testid="stSidebar"] {
    background-color: black !important;
}

/* Style buttons */
div.stButton > button {
    background-color: transparent;
    color: white;
    border: 2px solid white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
div.stButton > button:hover {
    background-color: #D3D3D3;
    color: black;
}
</style>
""", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
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

    category = st.session_state.get("category", "Produce")

    if category == "Produce":
        st.header("Produce Spoilage Signs")

    # 1. Change in Appearance (Text left, Image right)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 👀 Change in Appearance")
            st.write("- Discoloration, shriveling, or dark spots are early indicators that produce is no longer fresh.")
            st.write("- Dull or faded colors can also signal a loss of nutrients or spoilage.")
        with col2:
            st.image("apps/images/produce/yellowing_kale.jpg", caption="Yellowing kale", use_container_width=True)

    # 2. Unpleasant Odors (Image left, Text right)
        col3, col4 = st.columns(2)
        with col3:
            st.image("apps/images/produce/onion_odor.jpg", caption="Rotten onion", use_container_width=True)
        with col4:
            st.markdown("### 👃 Unpleasant Odors")
            st.write("- Sour, rotten, rancid, or fermented smells usually mean microbial activity has begun.")
            st.write("- Strong off-odors are one of the clearest signs that the food should be discarded.")

    # 3. Changes in Texture (Text left, Image right)
        col5, col6 = st.columns(2)
        with col5:
            st.markdown("### ✋ Changes in Texture")
            st.write("- Slimy, mushy, or unusually dry textures suggest cellular breakdown or excess moisture.")
            st.write("- Leafy greens, for example, often wilt or turn soggy when spoiled.")
        with col6:
            st.image("apps/images/produce/apple_texture.jpg", caption="Shriveled apple", use_container_width=True)

    # 4. Unpleasant Taste (Image left, Text right)
        col7, col8 = st.columns(2)
        with col7:
            st.image("apps/images/produce/spinach_taste.jpeg", caption="Rotten spinach", use_container_width=True)
        with col8:
            st.markdown("### 👅 Unpleasant Taste")
            st.write("- A bitter, sour, or rancid flavor can indicate the presence of spoilage bacteria or oxidation.")
            st.write("- If the taste is significantly off, it’s safest not to consume the item.")

    # 5. Enzymic Browning (Text left, Image right)
        col9, col10 = st.columns(2)
        with col9:
            st.markdown("### 🍌 Enzymic Browning")
            st.write("- This occurs in fruits like bananas, apples, and pears when the cut surfaces are exposed to oxygen.")
            st.write("- While sometimes harmless, it can also signal a breakdown in freshness over time.")
        with col10:
            st.image("apps/images/produce/browning_apple.jpeg", caption="Apple browning due to oxidation", use_container_width=True)

    # 6. Mold Growth (Image left, Text right)
        col11, col12 = st.columns(2)
        with col11:
            st.image("apps/images/produce/strawberry_mold.jpg", caption="Mold growing on strawberries", use_container_width=True)
        with col12:
            st.markdown("### 🧫 Mold Growth")
            st.write("- Mold appears as a fuzzy or velvety coating, often starting at the surface.")
            st.write("- It can be green, black, white, or even blue, depending on the mold species and food type.")
            st.write("- In produce, mold can rapidly spread through soft or moist areas.")

    # 7. Yeast Growth (Text left, Image right)
        col13, col14 = st.columns(2)
        with col13:
            st.markdown("### 🍶 Yeast Growth")
            st.write("- Yeast may appear as a whitish film, especially in high-sugar or moist environments.")
            st.write("- It can cause fermentation, producing gas bubbles or a yeasty odor.")
            st.write("- Spoiled fruits, fruit juices, or jams are common examples of visible yeast growth.")
        with col14:
            st.image("apps/images/produce/jam_yeast.jpg", caption="Yeast in jam", use_container_width=True)



    elif category == "Dairy":
        st.header("🥛 Dairy Spoilage Signs")

    # 1. Appearance (Text left, Image right)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 👀 Appearance")
            st.write("- Mold or discoloration on dairy items signals spoilage.")
            st.write("- Watch for blue, green, or black spots on cheese, yogurt, or cream.")
            st.write("- Cloudiness or separation in milk can indicate bacterial activity.")
        with col2:
            st.image("apps/images/dairy/yogurt_mold.jpeg", caption="Mold growing on yogurt", use_container_width=True)

    # 2. Smell (Image left, Text right)
        col3, col4 = st.columns(2)
        with col3:
            st.image("apps/images/dairy/butter_smell.jpg", caption="Moldy butter", use_container_width=True)
        with col4:
            st.markdown("### 👃 Smell")
            st.write("- A sour, rancid, or bitter smell is a strong indicator that dairy has gone bad.")
            st.write("- Milk and cream typically develop a sharp, acidic odor when spoiled.")
            st.write("- Yogurt may emit a fermented or overly tangy scent.")

    # 3. Texture (Text left, Image right)
        col5, col6 = st.columns(2)
        with col5:
            st.markdown("### ✋ Texture")
            st.write("- Spoiled milk may curdle or separate into clumps and watery liquid.")
            st.write("- Soft cheeses might become slimy or develop a gritty layer.")
            st.write("- Yogurt may appear overly watery on top or feel stringy when stirred.")
        with col6:
            st.image("apps/images/dairy/milk_texture.jpg", caption="Curdled milk", use_container_width=True)

    # 4. Taste (Image left, Text right)
        col7, col8 = st.columns(2)
        with col7:
            st.image("apps/images/dairy/cheese_taste.jpg", caption="Moldy cheese", use_container_width=True)
        with col8:
            st.markdown("### 👅 Taste")
            st.write("- A sour, metallic, or bitter taste is a strong sign the product has spoiled.")
            st.write("- Milk or cream that tastes 'off' should be discarded immediately.")
            st.write("- Spoiled cheese may taste overly sharp, ammonia-like, or chemically pungent.")

    elif category == "Meat":
        st.header("🥩 Meat Spoilage Signs")

    # 1. Appearance (Text left, Image right)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 👀 Appearance")
            st.write("- Spoiled meat may show discoloration such as a greenish tint, gray patches, or dull, faded tones.")
            st.write("- Mold spots can also form, especially if the meat has been stored improperly or too long.")
            st.write("- Fresh meat should be vibrant in color—if it looks strange, it's best to toss it.")
        with col2:
            st.image("apps/images/meat/meat_appearance.jpeg", caption="Discolored meat", use_container_width=True)

    # 2. Odor (Image left, Text right)
        col3, col4 = st.columns(2)
        with col3:
            st.image("apps/images/meat/meat_smell.jpg", caption="Spoiled meat with off smell", use_container_width=True)
        with col4:
            st.markdown("### 👃 Odor")
            st.write("- A strong, unpleasant odor is often the first and clearest sign of spoiled meat.")
            st.write("- The smell may be sour, rotten, or even ammonia-like, depending on the type and stage of spoilage.")
            st.write("- If your nose wrinkles when you open the package, don’t take a risk—throw it away.")

    # 3. Texture (Text left, Image right)
        col5, col6 = st.columns(2)
        with col5:
            st.markdown("### ✋ Texture")
            st.write("- Spoiled meat may feel slimy, sticky, or tacky to the touch due to bacterial buildup.")
            st.write("- This film often coats the surface and doesn't go away even when rinsed.")
            st.write("- Fresh meat should feel firm and slightly moist, not slippery or sticky.")
        with col6:
            st.image("apps/images/meat/meat_texture.jpg", caption="Slimy texture on spoiled meat", use_container_width=True)

    # 4. Taste (Image left, Text right)
        col7, col8 = st.columns(2)
        with col7:
            st.image("apps/images/meat/meat_taste.jpeg", caption="Avoid tasting suspicious meat", use_container_width=True)
        with col8:
            st.markdown("### 👅 Taste")
            st.write("- Spoiled meat may have a sour, metallic, or off flavor even after cooking.")
            st.write("- If you notice an unusual aftertaste or bitterness, stop eating immediately.")
            st.write("- Tasting meat to “check if it’s bad” is dangerous—trust the smell and appearance first.")

        
    elif category == "Baked Goods":
        st.header("🍞 Baked Goods Spoilage Signs")

    # 1. Appearance (Text left, Image right)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 👀 Appearance")
            st.write("- Mold growth is a common visual indicator of spoilage in bread, cakes, and pastries.")
            st.write("- Look for green, white, or black fuzzy patches on the surface.")
            st.write("- Discoloration or changes in crust color may also signal aging or contamination.")
        with col2:
            st.image("apps/images/baked_goods/baked_appearance.jpeg", caption="Mold on bread", use_container_width=True)

    # 2. Smell (Image left, Text right)
        col3, col4 = st.columns(2)
        with col3:
            st.image("apps/images/baked_goods/baked_smell.jpg", caption="Stale or sour smell", use_container_width=True)
        with col4:
            st.markdown("### 👃 Smell")
            st.write("- Spoiled baked goods may have a sour, musty, or fermented odor.")
            st.write("- Sweet items like cakes may develop an alcoholic smell due to yeast overgrowth.")
            st.write("- If the scent feels off from the usual baked aroma, it’s best not to consume.")

    # 3. Texture (Text left, Image right)
        col5, col6 = st.columns(2)
        with col5:
            st.markdown("### ✋ Texture")
            st.write("- Spoiled bread can become overly hard, crumbly, or spongy in a soggy way.")
            st.write("- Pastries may feel sticky, rubbery, or lose their crispness due to moisture imbalance.")
            st.write("- Any sliminess or unexpected softness can indicate mold or staling.")
        with col6:
            st.image("apps/images/baked_goods/baked_texture.jpg", caption="Unusual baked good texture", use_container_width=True)

    # 4. Taste (Image left, Text right)
        col7, col8 = st.columns(2)
        with col7:
            st.image("apps/images/baked_goods/baked_taste.jpg", caption="Avoid sour or stale taste", use_container_width=True)
        with col8:
            st.markdown("### 👅 Taste")
            st.write("- Spoiled baked goods may taste sour, bitter, or have a stale aftertaste.")
            st.write("- Sweet treats might lose flavor or take on a sharp, fermented bite.")
            st.write("- If the taste is odd or unpleasant, it’s best not to continue eating.")
        
        st.info("📘 Come back often as we keep this guide updated to help prevent foodborne illness.")
