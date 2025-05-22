
import streamlit as st
import os

def show_landing():
    st.title("In Cultural Lens")
    st.subheader("Discover India's Hidden Gems, Arts, and Heritage")
    st.markdown("Explore the cultural richness of Indian cities and plan your journey in a smart, personalized way.")

    st.markdown("### 🌆 Featured Cultural Cities")
    cities = ["Jaipur", "Varanasi", "Mysore"]
    cols = st.columns(len(cities))

    for i, city in enumerate(cities):
        with cols[i]:
            image_path = f"assets/city_images/{city.lower()}.jpg"
            if os.path.exists(image_path):
                st.image(image_path, use_column_width=True)
            st.caption(city)
