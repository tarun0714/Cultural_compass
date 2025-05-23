import streamlit as st
from sections.landing import show_landing
from sections.city_info import show_city_info
from sections.itinerary_bot import generate_itinerary_via_llm
from sections.map_click import map_selection
import cohere

st.set_page_config(page_title="Cultural Lens", layout="wide")

# Landing section
show_landing()

# Right sidebar chatbot about selected city
if "selected_city_info" in st.session_state:
    city = st.session_state["selected_city_info"]

    with st.sidebar:
        st.markdown(f"### 🧭 Cultural Info for {city}")
        st.write("Here’s what you can explore:")
        st.markdown(f"- 🎭 Traditional Arts of **{city}**")
        st.markdown(f"- 🏛️ Tourist Hotspots")
        st.markdown(f"- 🧵 Local Crafts & Festivals")

        prompt = f"Tell me about the cultural heritage, art forms, and best tourist spots in {city}."
        if st.button("🧠 Ask Cultural Bot"):
            co = cohere.Client(st.secrets["COHERE_API_KEY"])
            with st.spinner("Fetching cultural insights..."):
                response = co.generate(
                    model="command-light",  # ✅ Free model
                    prompt=prompt,
                    max_tokens=600,
                    temperature=0.7
                )
                st.success(response.generations[0].text)

# Show interactive map
map_selection()

# Sidebar itinerary planner
with st.sidebar:
    st.header("🎯 Plan Your Trip")

    preselected_city = st.session_state.get("selected_city_from_map", "Udaipur")
    city = st.text_input("City to Visit", value=preselected_city)

    origin = st.text_input("Traveling From")
    days = st.slider("How many days will you stay?", 1, 5, 2)
    interests = st.multiselect("Your Interests", ["Art", "Food", "Temples", "Festivals", "Museums", "Historic"])

    if st.button("Generate Itinerary"):
        st.session_state.chat_query = {
            "city": city,
            "origin": origin,
            "days": days,
            "interests": interests
        }

# Chatbot Output via Cohere
if "chat_query" in st.session_state:
    q = st.session_state.chat_query
    st.chat_message("user").write(
        f"Plan a {q['days']}-day trip to **{q['city']}** from **{q['origin']}** with interests: {', '.join(q['interests'])}"
    )
    with st.spinner("Generating your personalized itinerary..."):
        itinerary = generate_itinerary_via_llm(q)
    st.chat_message("assistant").write(itinerary)
