import streamlit as st
import google.generativeai as genai

# ခင်ဗျားရဲ့ API Key (...NN70)
genai.configure(api_key="AIzaSyC9ovRyS2PuDaz3iwHPYga7NTTY6lzmYq0") 

st.set_page_config(page_title="Gemini Tarot Gallery", page_icon="🔮")

# CSS ကို ပိုကောင်းအောင် ညှိထားပါတယ် (Laptop မှာ ညီနေစေဖို့)
st.markdown("""
    <style>
    .stImage > img {
        width: 100% !important;
        height: 280px !important;
        object-fit: contain !important;
        background-color: #1a1a1a;
        border-radius: 8px;
    }
    div.stButton > button {
        width: 100%;
        font-size: 11px !important;
        padding: 5px !important;
        border-radius: 0 0 8px 8px;
    }
    /* ကတ်တစ်ခုစီကြားက အကွာအဝေးကို ညှိခြင်း */
    div[data-testid="column"] {
        padding: 5px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 တားရော့ကတ် ၂၂ ကတ်")

base_url = "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/main/"

# Magician ရဲ့ Error ကို ဒီမှာ ပြင်ပေးထားပါတယ်
cards = {
    "The Sun": base_url + "the_sun.jpg",
    "The Fool": base_url + "the_fool.jpg",
    "The Magician": base_url + "The%20_Magician.jpg", # Space ကို %20 နဲ့ ပြင်ထားတယ်
    "The Hanged Man": base_url + "The_Hanged_Man.jpg",
    "The Tower": base_url + "The_Tower.jpg",
    "The World": base_url + "The_World.jpg",
    "The Emperor": base_url + "The_Emperor.jpg",
    "Death": base_url + "Death.jpg",
    "The Devil": base_url + "The_Devil.jpg",
    "Judgement": base_url + "Judgement.jpg",
    "The Justice": base_url + "Justice_Tarot.jpg",
    "The Chariot": base_url + "The_Chariot.jpg",
    "The Empress": base_url + "The_Empress.jpg",
    "The Hermit": base_url + "The_Hermit.jpg",
    "The Hierophant": base_url + "The_Hierophant.jpg",
    "High Priestess": base_url + "The_High_Priestess.jpg",
    "The Lovers": base_url + "The_Lovers.jpg",
    "The Strength": base_url + "The_Strength.jpg",
    "The Star": base_url + "The_star.jpg",
    "Wheel Of Fortune": base_url + "Wheel_of_Fortune.jpg",
    "The Moon": base_url + "the_moon.jpg",
    "Temperance": base_url + "Temperance.jpg"
}

if 'selected_card' not in st.session_state:
    st.session_state.selected_card = None

# Laptop မှာ တစ်တန်းကို ၄ ကတ်နှုန်းက အကောင်းဆုံးပါပဲ
cols = st.columns(4)
card_list = list(cards.items())

for i in range(len(card_list)):
    name, img_url = card_list[i]
    with cols[i % 4]:
        st.image(img_url)
        if st.button(f"ရွေးမည်: {name}", key=f"btn_{i}"):
            st.session_state.selected_card = name

# ဟောချက်အပိုင်း
if st.session_state.selected_card:
    st.divider()
    st.header(f"ရွေးထားသောကတ် - {st.session_state.selected_card}")
    if st.button("ဟောကိန်းထုတ်မည် ✨"):
        with st.spinner('Gemini က ကတ်ကို ဖတ်နေပါတယ်...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            # System Instruction အနည်းငယ်ထည့်ထားပါတယ်
            prompt = f"မင်းက တားရော့ဟောဆရာ Gemini ဖြစ်တယ်။ {st.session_state.selected_card} ကတ်အကြောင်းကို မြန်မာလို အသေးစိတ် ဟောပေးပါ။"
            response = model.generate_content(prompt)
            st.write(response.text)
