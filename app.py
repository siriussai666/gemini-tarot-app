import streamlit as st
from google import genai
from google.genai import types
import os

# API Key ကို Secrets ထဲကနေ လုံခြုံစွာ ယူသုံးခြင်း
api_key = st.secrets["GEMINI_API_KEY"]
client = genai.Client(api_key=api_key)

st.set_page_config(page_title="Gemini Tarot Mystery", page_icon="🔮")
st.title("🔮 သင်၏ ကံကြမ္မာကတ်ကို ရွေးချယ်ပါ")

# Tarot Cards Setup
base_url = "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/main/"
cards = {
    "The Sun": base_url + "the_sun.jpg", "The Fool": base_url + "the_fool.jpg",
    "The Magician": base_url + "the_magic.jpg", "The Hanged Man": base_url + "The_Hanged_Man.jpg",
    "The Tower": base_url + "The_Tower.jpg", "The World": base_url + "The_World.jpg",
    "The Emperor": base_url + "The_Emperor.jpg", "Death": base_url + "Death.jpg",
    "The Devil": base_url + "The_Devil.jpg", "Judgement": base_url + "Judgement.jpg",
    "Justice": base_url + "Justice_Tarot.jpg", "The Chariot": base_url + "The_Chariot.jpg",
    "The Empress": base_url + "The_Empress.jpg", "The Hermit": base_url + "The_Hermit.jpg",
    "The Hierophant": base_url + "The_Hierophant.jpg", "High Priestess": base_url + "The_High_Priestess.jpg",
    "The Lovers": base_url + "The_Lovers.jpg", "The Strength": base_url + "The_Strength.jpg",
    "The Star": base_url + "The_star.jpg", "Wheel Of Fortune": base_url + "Wheel_of_Fortune.jpg",
    "The Moon": base_url + "the_moon.jpg", "Temperance": base_url + "Temperance.jpg"
}

if 'selected_card' not in st.session_state:
    st.session_state.selected_card = None

cols = st.columns(4)
card_list = list(cards.items())

for i in range(len(card_list)):
    name, img_url = card_list[i]
    with cols[i % 4]:
        st.image(img_url)
        if st.button(f"ရွေးချယ်မည်", key=f"btn_{i}"):
            st.session_state.selected_card = name

if st.session_state.selected_card:
    st.divider()
    if st.button("ဟောကိန်းထုတ်ရန် နှိပ်ပါ ✨"):
        with st.spinner('Gemini က ကတ်ကို ဖတ်နေပါတယ်...'):
            try:
                # SDK အသစ်၏ ခေါ်ဆိုပုံ
                model_id = "gemini-2.0-flash" 
                prompt = f"မင်းက တားရော့ဟောဆရာ Gemini ဖြစ်တယ်။ {st.session_state.selected_card} ကတ်အကြောင်းကို မြန်မာလို အသေးစိတ် ဟောပေးပါ။"
                
                response = client.models.generate_content(
                    model=model_id,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        tools=[types.Tool(google_search=types.GoogleSearch())]
                    )
                )
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}. Key အသစ်ကို Secrets မှာ ထည့်ထားပါသလား?")
