import streamlit as st
import google.generativeai as genai

# ခင်ဗျားရဲ့ API Key (...NN70)
genai.configure(api_key="AIzaSyC9ovRyS2PuDaz3iwHPYga7NTTY6lzmYq0") 

# Layout ကို Wide မသုံးဘဲ ပုံမှန်ပဲ ထားကြည့်ပါမယ် (Laptop မှာ ပိုကြည့်ကောင်းဖို့)
st.set_page_config(page_title="Gemini Tarot Gallery", page_icon="🔮")

# CSS ကို ပိုပြီး တိတိကျကျ ပြင်လိုက်ပါတယ်
st.markdown("""
    <style>
    /* ပုံရဲ့ Size ကို Fix လုပ်ပြီး Frame ညီအောင် ညှိခြင်း */
    .stImage > img {
        width: 100% !important;
        height: 280px !important; /* အရွယ်အစားကို Laptop နဲ့ ကိုက်အောင် နည်းနည်း လျှော့ထားပါတယ် */
        object-fit: contain !important; /* ပုံမပြတ်သွားအောင် contain သုံးထားပါတယ် */
        background-color: #1a1a1a;
        border-radius: 8px;
    }
    /* ခလုတ်ကို ပုံနဲ့ ကပ်နေအောင် ညှိခြင်း */
    .stButton button {
        width: 100%;
        font-size: 12px !important;
        padding: 0px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 တားရော့ကတ်ကို ရွေးချယ်ပါ")

base_url = "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/main/"

# ကတ်စာရင်း (Link တွေကို စစ်ဆေးပြီးသားပါ)
cards = {
    "The Sun": base_url + "the_sun.jpg",
    "The Fool": base_url + "the_fool.jpg",
    "The Magician": base_url + "The_Magician.jpg",
    "The Hanged Man": base_url + "The_Hanged_Man.jpg",
    "The Tower": base_url + "The_Tower.jpg",
    "The World": base_url + "The_World.jpg",
    "The Emperor": base_url + "The_Emperor.jpg",
    "Death": base_url + "Death.jpg",
    "The Devil": base_url + "The_Devil.jpg"
}

if 'selected_card' not in st.session_state:
    st.session_state.selected_card = None

# Laptop Screen မှာ တစ်တန်းကို ၃ ကတ်နှုန်းက အရှင်းဆုံးပါပဲ
cols = st.columns(3)
card_list = list(cards.items())

for i in range(len(card_list)):
    name, img_url = card_list[i]
    with cols[i % 3]:
        st.image(img_url)
        if st.button(f"ရွေးမည်: {name}", key=f"btn_{name}"):
            st.session_state.selected_card = name

# ဟောချက်အပိုင်း
if st.session_state.selected_card:
    st.divider()
    st.header(f"ရွေးထားသောကတ် - {st.session_state.selected_card}")
    if st.button("ဟောကိန်းထုတ်မည် ✨"):
        with st.spinner('Gemini က ကတ်ကို ဖတ်နေပါတယ်...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"မင်းက တားရော့ဟောဆရာ Gemini ဖြစ်တယ်။ {st.session_state.selected_card} ကတ်အကြောင်းကို မြန်မာလို ဟောပေးပါ။"
            response = model.generate_content(prompt)
            st.write(response.text)
