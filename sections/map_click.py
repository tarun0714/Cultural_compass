import streamlit as st
from streamlit_folium import st_folium
import folium
from geopy.geocoders import Nominatim

def map_selection():
    st.markdown("### 🗺️ Explore India on Map")

    m = folium.Map(location=[23.0, 80.0], zoom_start=5)
    map_data = st_folium(m, width=700, height=450)

    if map_data and map_data.get("last_clicked"):
        lat = map_data["last_clicked"]["lat"]
        lon = map_data["last_clicked"]["lng"]

        geolocator = Nominatim(user_agent="cultural-lens")
        try:
            location = geolocator.reverse((lat, lon), language="en", timeout=10)
            address = location.raw.get("address", {})
            city = address.get("city") or address.get("town") or address.get("village") or address.get("state")

            if city:
                st.success(f"You clicked near: **{city}**")
                if st.button(f"Yes, select {city}"):
                    st.session_state["selected_city_from_map"] = city
        except:
            st.warning("Could not detect city. Try again.")
    else:
        st.caption("🖱️ Click on a location in India to begin your cultural journey.")

    st.markdown("---")
