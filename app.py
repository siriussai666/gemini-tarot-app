import streamlit as st
import google.generativeai as genai

# API Key ကို သေချာထည့်ပါ
genai.configure(api_key="AIzaSyC9ovRyS2PuDaz3iwHPYga7NTTY6lzmYq0") 

st.set_page_config(page_title="Gemini Tarot Mystery", page_icon="🔮")

# Mystery Gallery CSS
st.markdown("""
    <style>
    .stImage > img { height: 280px !important; object-fit: contain !important; background-color: #1a1a1a; border-radius: 8px; }
    div.stButton > button { width: 100%; background-color: #2e2e2e; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 သင်၏ ကံကြမ္မာကတ်ကို ရွေးချယ်ပါ")

base_url = "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/main/"

# ကတ်စာရင်း
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

# ဟောချက်အပိုင်း (v1beta Error ကို ကျော်ဖြတ်ရန် ပြင်ဆင်ချက်)
if st.session_state.selected_card:
    st.divider()
    if st.button("ဟောကိန်းထုတ်ရန် နှိပ်ပါ ✨"):
        with st.spinner('Gemini က ကတ်ကို ဖတ်နေပါတယ်...'):
            try:
                # 404 ကို ကျော်ဖို့ model နာမည်ကို အခြေခံကစပြီး စမ်းပါမယ်
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"မင်းက တားရော့ဟောဆရာ Gemini ဖြစ်တယ်။ {st.session_state.selected_card} ကတ်အကြောင်းကို မြန်မာလို အသေးစိတ် ဟောပေးပါ။"
                
                # Syntax Fix
                response = model.generate_content(prompt)
                st.write(response.text)
            except Exception as e:
                # v1beta error ကြောင့် model ရှာမတွေ့ရင် ဒီနေရာကနေ ဟောပေးပါမယ်
                st.warning("Model Update ဖြစ်နေလို့ ခေတ္တစောင့်ပါ။ အခြား Model နဲ့ ကြိုးစားကြည့်ပါမယ်...")
                try:
                    model_alt = genai.GenerativeModel('gemini-pro')
                    response = model_alt.generate_content(prompt)
                    st.write(response.text)
                except:
                    st.error(f"Error: {e}. ကျေးဇူးပြု၍ requirements.txt ထဲတွင် google-generativeai ကို update လုပ်ပေးပါ။")
