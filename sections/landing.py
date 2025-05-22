
import streamlit as st
import os

def show_landing():
    st.header("**Cultural Lens**")
    st.subheader("Discover India's Hidden Gems, Arts, and Heritage")
    st.markdown("Explore the cultural richness of Indian cities and plan your journey in a smart, personalized way.")

    st.markdown("## 🏙️ Featured Cultural Cities")
    cities = ["Jaipur", "Varanasi", "Mysore", "Udaipur", "Delhi"]
    cols = st.columns(len(cities))

    for i, city in enumerate(cities):
      with cols[i]:
        image_path = f"assets/city_images/{city.lower()}.jpg"

        if os.path.exists(image_path):
            if st.button(f"📍 {city}", key=city):
                st.session_state["selected_city_info"] = city

            from PIL import Image
            img = Image.open(image_path)
            img = img.resize((300, 200))  # 👈 Make them all look the same
            st.image(img)
            st.caption(city)
