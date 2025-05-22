
import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_itinerary_via_llm(query):
    prompt = (
        f"You are a cultural travel planner bot. Generate a {query['days']}-day cultural itinerary for a user "
        f"traveling from {query['origin']} to {query['city']}. The user is interested in {', '.join(query['interests'])}. "
        "Include famous spots, cultural insights, local food, and a warm tone. Format clearly day-wise with emojis and headings."
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response["choices"][0]["message"]["content"]
