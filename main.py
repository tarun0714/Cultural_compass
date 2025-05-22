
import streamlit as st
from sections.landing import show_landing
from sections.city_info import show_city_info
from sections.itinerary_bot import generate_itinerary_via_llm
from sections.map_click import map_selection

st.set_page_config(page_title="Cultural Lens", layout="wide")

# Landing section
show_landing()

if "selected_city_info" in st.session_state:
    city = st.session_state["selected_city_info"]

    with st.sidebar:
        st.markdown(f"### 🧭 Cultural Info for {city}")

        st.write("Here’s what you can explore:")
        st.markdown(f"- 🎭 Traditional Arts of **{city}**")
        st.markdown(f"- 🏛️ Tourist Hotspots")
        st.markdown(f"- 🧵 Local Crafts & Festivals")

        # Optional: Chat-like LLM call
        import openai
        openai.api_key = st.secrets["OPENAI_API_KEY"]

        prompt = f"Tell me about the cultural heritage, art forms, and best tourist spots in {city}."
        if st.button("🧠 Ask Cultural Bot"):
            with st.spinner("Fetching cultural insights..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.success(response["choices"][0]["message"]["content"])


map_selection()


# Sidebar chatbot
with st.sidebar:
    st.header("🎯 Plan Your Trip")

    # Prefill city if map selected it
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

# Chatbot Output
if "chat_query" in st.session_state:
    q = st.session_state.chat_query
    st.chat_message("user").write(
        f"Plan a {q['days']}-day trip to **{q['city']}** from **{q['origin']}** with interests: {', '.join(q['interests'])}"
    )
    with st.spinner("Generating your personalized itinerary..."):
        itinerary = generate_itinerary_via_llm(q)
    st.chat_message("assistant").write(itinerary)
