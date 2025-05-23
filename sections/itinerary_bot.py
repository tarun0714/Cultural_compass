import cohere
import streamlit as st

# Setup Cohere client
co = cohere.Client(st.secrets["COHERE_API_KEY"])

def generate_itinerary_via_llm(query):
    prompt = (
        f"You are a cultural travel planner bot. Generate a {query['days']}-day cultural itinerary for a user "
        f"traveling from {query['origin']} to {query['city']}. The user is interested in {', '.join(query['interests'])}. "
        "Include famous spots, cultural insights, local food, and a warm tone. Format clearly day-wise with emojis and headings."
    )

    response = co.generate(
        model="command-light",  # ✅ Free & supported
        prompt=prompt,
        max_tokens=600,
        temperature=0.7
    )

    return response.generations[0].text
