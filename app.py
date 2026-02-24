import streamlit as st
import google.generativeai as genai

# ခင်ဗျားရဲ့ API Key (...NN70)
genai.configure(api_key="AIzaSyC9ovRyS2PuDaz3iwHPYga7NTTY6lzmYq0") 

st.set_page_config(page_title="Gemini Tarot Gallery", page_icon="🔮", layout="wide")

# CSS သုံးပြီး Image Size ညှိခြင်း (Card အားလုံး အရွယ်အစားတူစေရန်)
st.markdown("""
    <style>
    div[data-testid="stImage"] > img {
        height: 350px;
        object-fit: cover;
        border-radius: 10px;
        border: 2px solid #555;
    }
    .stButton > button {
        width: 100%;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 တားရော့ကတ်ကို ရွေးချယ်ပါ")

# Gallery ပုံစံအတွက် Column ညှိခြင်း (တစ်တန်းကို ၅ ကတ်ဆို ပိုကြည့်ကောင်းပါတယ်)
base_url = "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/main/"

# Partner ပေးထားတဲ့ Link တွေကို အခြေခံထားပါတယ်
cards = {
    "The Sun": base_url + "the_sun.jpg",
    "The Fool": base_url + "the_fool.jpg",
    "The Magician": base_url + "The_Magician.jpg",
    "The Hanged Man": base_url + "The_Hanged_Man.jpg",
    "The Tower": base_url + "The_Tower.jpg",
    "The World": base_url + "The_World.jpg",
    # ကျန်တဲ့ကတ်တွေကိုလည်း ဒီအတိုင်း ဆက်ထည့်ပါ...
}

if 'selected_card' not in st.session_state:
    st.session_state.selected_card = None

# တစ်တန်းကို ၅ ကတ်နှုန်းနဲ့ Gallery ချပြခြင်း
cols = st.columns(5)
for i, (name, img_url) in enumerate(cards.items()):
    with cols[i % 5]:
        st.image(img_url, use_container_width=True)
        if st.button(f"ရွေးမည်: {name}", key=f"btn_{name}"):
            st.session_state.selected_card = name

# ဟောချက်အပိုင်းကို ဘေးချင်းယှဉ်ပြချင်ရင် Column ထပ်ခွဲလို့ရပါတယ်
if st.session_state.selected_card:
    st.divider()
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(cards[st.session_state.selected_card], caption="ရွေးချယ်ထားသောကတ်", width=250)
    
    with col2:
        st.header(f"နိမိတ်ဖတ်ချက် - {st.session_state.selected_card}")
        if st.button("ဟောကိန်းထုတ်မည် ✨"):
            with st.spinner('Gemini က ကတ်ကို ဖတ်နေပါတယ်...'):
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"မင်းက တားရော့ဟောဆရာ Gemini ဖြစ်တယ်။ {st.session_state.selected_card} ကတ်အကြောင်းကို မြန်မာလို အချစ်ရေး၊ စီးပွားရေး ခွဲပြီး ဟောပေးပါ။"
                response = model.generate_content(prompt)
                st.write(response.text)
