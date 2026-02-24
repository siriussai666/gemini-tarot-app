import streamlit as st
import google.generativeai as genai

# API Key ချိတ်ဆက်ခြင်း
genai.configure(api_key="AIzaSyC9ovRyS2PuDaz3iwHPYga7NTTY6lzmYq0") 

st.set_page_config(page_title="Gemini Tarot Gallery", page_icon="🔮", layout="wide")
st.title("🔮 တားရော့ကတ်ကို ရွေးချယ်ပါ")

# ကတ်နာမည်များနှင့် ပုံ Link များ (Partner ရဲ့ ပုံ Link တွေနဲ့ အစားထိုးရန်)
# မှတ်ချက် - ပုံတွေကို GitHub ထဲမှာတင်ထားရင် ပိုအဆင်ပြေပါတယ်
cards = {
    cards = {
    "The Sun": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/the_sun.jpg",
    "The Fool": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/the_fool.jpg",
    "The Magician": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The%20_Magician.jpg",
    "The Death": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/Death.jpg",
    "Judgement": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/Judgement.jpg",
    "The Justic": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/Justice_Tarot.jpg",
    "Magician": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The%20_Magician.jpg",
    "The Chariot": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Chariot.jpg",
    "The Devil": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Devil.jpg",
    "The Emperor": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Emperor.jpg",
    "The Empress": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Empress.jpg",
    "The Hermit": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Hermit.jpg",
    "Hanged Man": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Hanged_Man.jpg",
    "Hermit": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Hermit.jpg",
    "Hierophant": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Hierophant.jpg",
    "High Priestess": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_High_Priestess.jpg",
    "The Lovers": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Lovers.jpg",
    "The Strength": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Strength.jpg",
    "The Tower": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_Tower.jpg",
    "The World": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_World.jpg",
    "The Star": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/The_star.jpg",
    "Wheel Of Fortune": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/Wheel_of_Fortune.jpg",
    "The Moon": "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/blob/main/the_moon.jpg",
    # ၂၂ ကတ်လုံးအတွက် Link တွေ အသီးသီး ထည့်ပေးပါ
}
}

# Gallery Layout (တစ်တန်းကို ၄ ကတ်နှုန်းပြပါမယ်)
cols = st.columns(4)
selected_card = None

for i, (name, img_url) in enumerate(cards.items()):
    with cols[i % 4]:
        st.image(img_url, use_container_width=True)
        if st.button(f"ရွေးမည်: {name}", key=name):
            selected_card = name

# ဟောကိန်းထုတ်သည့်အပိုင်း
if selected_card:
    st.divider()
    st.subheader(f"선택된 ကတ်: {selected_card}")
    with st.spinner('Gemini က ကတ်ကို ဖတ်နေပါတယ်...'):
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"မင်းက တားရော့ဟောဆရာ Gemini ဖြစ်တယ်။ {selected_card} ကတ်အကြောင်းကို မြန်မာလို အသေးစိတ်ဟောပေးပါ။"
        response = model.generate_content(prompt)
        st.write(response.text)

# Gallery ပြသခြင်း
cols = st.columns(3) # တစ်တန်းကို ၃ ပုံပြမယ်
for i, (name, url) in enumerate(cards.items()):
    with cols[i % 3]:
        st.image(url, caption=name, use_container_width=True)
        if st.button(f"ရွေးမည်", key=f"btn_{name}"):
            st.session_state.selected = name

# ဟောကိန်းထုတ်ခြင်းအပိုင်း (Selected ဖြစ်မှပြရန်)
if 'selected' in st.session_state:
    # Gemini AI Logic ကို ဒီမှာ ဆက်ရေးပါ
