import streamlit as st 
from streamlit_echarts import st_echarts
from gradio_client import Client, handle_file
import tempfile
import re
import pymongo
import base64
from urllib.parse import quote_plus

st.set_page_config(page_title="KindBites", page_icon="🍽️", layout="wide")

@st.cache_resource
def init_connection():
    return pymongo.MongoClient("mongodb+srv://finding:nemo@algoarena-cluster.mzcfclp.mongodb.net/")

client = init_connection()

def insert_food_item(data):
    db = client.Market
    db.Food_Items.insert_one(data)

@st.cache_data(ttl=600)
def get_data():
    db = client.Market
    items = list(db.Food_Items.find())
    return items

def image_to_base64(image_data):
    return base64.b64encode(image_data.getvalue()).decode("utf-8")

def base64_to_image(base64_str):
    return f"data:image/jpeg;base64,{base64_str}"

def app():
    st.title("🍽️ KindBites Market")

    if "input_method_confirmed" not in st.session_state:
        st.session_state.input_method_confirmed = False
    if "image_uploaded" not in st.session_state:
        st.session_state.image_uploaded = False
    if "image_data" not in st.session_state:
        st.session_state.image_data = None
    if "selected_address" not in st.session_state:
        st.session_state.selected_address = None

    left_col, center_col, right_col = st.columns([1.5, 2, 1.5], gap="large")

    # ---------------- LEFT: Donation Flow ----------------
    with left_col:
        st.subheader("📤 Donate Food")

        with st.form("input_method_form"):
            company_name = st.text_input("Company Name")
            food_name = st.text_input("Food Item")
            quantity = st.number_input("Quantity", min_value=1, step=1)
            expiration_date = st.date_input("Expiration Date")
            pickup_time = st.time_input("Preferred Pickup Time")
            address = st.text_area("Company Address")
            contains_allergen = st.checkbox("⚠️ Contains Allergens?")
            contains_lactose = st.checkbox("🥛 Contains Lactose?")
            upload_option = st.radio("Choose input method:", ["Upload from device", "Capture with camera"])
            confirm_input = st.form_submit_button("✅ Confirm Input Method")

        if confirm_input:
            st.session_state.input_method_confirmed = True
            st.session_state.image_uploaded = False
            st.session_state.image_data = None

        if st.session_state.input_method_confirmed:
            st.markdown("### 📸 Upload or Capture Image")

            if upload_option == "Upload from device":
                uploaded_img = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], key="upload_input")
            else:
                uploaded_img = st.camera_input("Take a photo of the food", key="camera_input")

            if uploaded_img:
                st.session_state.image_uploaded = True
                st.session_state.image_data = uploaded_img
                st.image(uploaded_img, caption="Submitted Food Image", use_container_width=True)

        if st.session_state.image_uploaded and st.session_state.image_data:
            if st.button("🚀 Submit Food Donation"):
                st.success(f"✅ Thanks, {company_name}! Your {food_name} submission was received.")
                st.image(st.session_state.image_data, caption="Submitted Food Image", use_container_width=True)

                st.markdown("### 🧠 Quality Check in Progress...")

                try:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                        tmp_file.write(st.session_state.image_data.getvalue())
                        tmp_file_path = tmp_file.name

                    model_client = Client("Chanereach/Food_Spoilage_Detection")
                    result = model_client.predict(image=handle_file(tmp_file_path), api_name="/predict")

                    match = re.search(r"(\d+)", result)
                    percentage = int(match.group(1)) if match else 70
                    description = result

                    st.markdown("#### 🍏 Freshness Score")
                    freshness_options = {
                        "series": [{
                            "type": "gauge",
                            "progress": {"show": True, "width": 18},
                            "axisLine": {"lineStyle": {"width": 18}},
                            "detail": {"valueAnimation": True, "formatter": "{value}%"},
                            "data": [{"value": percentage, "name": "Quality"}]
                        }]
                    }
                    st_echarts(options=freshness_options, height="300px")
                    st.info(f"🧾 **Model Analysis:** {description}")

                    encoded_image = image_to_base64(st.session_state.image_data)

                    insert_food_item({
                        "name": food_name,
                        "company": company_name,
                        "quantity": quantity,
                        "description": description,
                        "image_base64": encoded_image,
                        "freshness": percentage,
                        "expiration_date": str(expiration_date),
                        "pickup_time": str(pickup_time),
                        "contains_allergen": contains_allergen,
                        "contains_lactose": contains_lactose,
                        "address": address
                    })

                except Exception as e:
                    st.error(f"🚫 Error calling Gradio API: {e}")
            else:
                st.info("✅ Image uploaded. Please submit the donation.")

    # ---------------- CENTER: Marketplace ----------------
    with center_col:
        st.subheader("🛒 Food Marketplace")

        for item in get_data():
            with st.expander(f"🍴 {item.get('name', 'Unknown Item')} from {item.get('company', 'Unknown')}"):
                if "image_base64" in item:
                    st.image(base64_to_image(item["image_base64"]), use_container_width=True)

                st.write(f"**Quantity:** {item.get('quantity', 'N/A')}")
                st.write(f"**Description:** {item.get('description', 'No description available.')}")

                if item.get("contains_allergen") or item.get("contains_lactose"):
                    st.markdown("### ⚠️ Allergen Info")
                    if item.get("contains_allergen"):
                        st.markdown("<span style='color:#E0A800;font-size:18px'>⚠️ <b>Contains Allergens</b></span>", unsafe_allow_html=True)
                    if item.get("contains_lactose"):
                        st.markdown("<span style='color:#E0A800;font-size:18px'>⚠️ <b>Contains Lactose</b></span>", unsafe_allow_html=True)

                st.write(f"**Freshness Score:** {item.get('freshness', 'N/A')}%")
                st.write(f"**Expiration Date:** {item.get('expiration_date', 'N/A')}")
                st.write(f"**Pickup Time:** {item.get('pickup_time', 'N/A')}")
                st.write(f"**Address:** {item.get('address', 'N/A')}")

                if st.button("📍 Get Me Directions", key=f"dir_{item['_id']}"):
                    st.session_state.selected_address = item.get("address")

    # ---------------- RIGHT: Map / Routing ----------------
    with right_col:
        st.subheader("🗺️ Fastest Route")

        if st.session_state.selected_address:
            api_key = "AIzaSyASfZLYRJsxaThiO-MJ_HqFnlDCY47pNiQ"  
            embed_url = f"https://www.google.com/maps/embed/v1/place?key={api_key}&q={quote_plus(st.session_state.selected_address)}"
            st.markdown("### 📍 Directions to Selected Pickup Location")
            st.components.v1.html(
                f"""
                <iframe
                    width="100%"
                    height="350"
                    frameborder="0"
                    style="border:0"
                    src="{embed_url}"
                    allowfullscreen>
                </iframe>
                """,
                height=350,
            )
            st.info(f"Directions for: {st.session_state.selected_address}")
        else:
            st.image("https://via.placeholder.com/300x250.png?text=Map+Coming+Soon", caption="Route Map", use_container_width=True)

if __name__ == "__main__":
    app()



        


