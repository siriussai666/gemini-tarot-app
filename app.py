import streamlit as st
import google.generativeai as genai

# ခင်ဗျားရဲ့ API Key (...NN70) ကို ဒီမှာထည့်ပါ
genai.configure(api_key="AIzaSyC9ovRyS2PuDaz3iwHPYga7NTTY6lzmYq0") 

st.set_page_config(page_title="Gemini Tarot Gallery", page_icon="🔮", layout="wide")
st.title("🔮 တားရော့ကတ်ကို ရွေးချယ်ပါ")

# Gallery အတွက် ကတ်များနှင့် Raw Links များ
# Partner ရဲ့ Link တွေထဲက github.com ကို raw.githubusercontent.com လို့ ပြောင်းထားပါတယ်
base_url = "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/main/"

cards = {
    "The Sun": base_url + "the_sun.jpg",
    "The Fool": base_url + "the_fool.jpg",
    "The Magician": base_url + "The_Magician.jpg",
    "The Hanged Man": base_url + "The_Hanged_Man.jpg",
    "The Tower": base_url + "The_Tower.jpg",
    "Death": base_url + "Death.jpg",
    "The Emperor": base_url + "The_Emperor.jpg",
    "Strength": base_url + "The_Strength.jpg",
    "The World": base_url + "The_World.jpg",
    "The Lovers": base_url + "The_Lovers.jpg",
    "The Star": base_url + "The_star.jpg",
    "The Hermit": base_url + "The_Hermit.jpg",
    "The Chariot": base_url + "The_Chariot.jpg",
    "Wheel of Fortune": base_url + "Wheel_of_Fortune.jpg",
    "Justice": base_url + "Justice_Tarot.jpg",
    "Temperance": base_url + "Temperance.jpg",
    "The Devil": base_url + "The_Devil.jpg",
    "The Moon": base_url + "the_moon.jpg",
    "Judgement": base_url + "Judgement.jpg",
    "The High Priestess": base_url + "The_High_Priestess.jpg",
    "The Empress": base_url + "The_Empress.jpg",
    "The Hierophant": base_url + "The_Hierophant.jpg"
}

# Gallery UI (တစ်တန်းကို ၄ ကတ်နှုန်းပြပါမယ်)
cols = st.columns(4)
if 'selected_card' not in st.session_state:
    st.session_state.selected_card = None

for i, (name, img_url) in enumerate(cards.items()):
    with cols[i % 4]:
        st.image(img_url, use_container_width=True)
        if st.button(f"ရွေးမည်: {name}", key=f"btn_{name}"):
            st.session_state.selected_card = name

# ဟောချက်အပိုင်း
if st.session_state.selected_card:
    st.divider()
    st.header(f"ရွေးချယ်ထားသောကတ် - {st.session_state.selected_card}")
    
    if st.button("ဟောကိန်းထုတ်မည် ✨"):
        with st.spinner('Gemini က ကတ်ကို ဖတ်နေပါတယ်...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"မင်းက တားရော့ဟောဆရာ Gemini ဖြစ်တယ်။ {st.session_state.selected_card} ကတ်အကြောင်းကို မြန်မာလို အသေးစိတ်ဟောပေးပါ။"
            response = model.generate_content(prompt)
            st.write(response.text)
