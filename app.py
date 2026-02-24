import streamlit as st
import google.generativeai as genai

# ခင်ဗျားရဲ့ API Key (...NN70)
genai.configure(api_key="AIzaSyC9ovRyS2PuDaz3iwHPYga7NTTY6lzmYq0") 

st.set_page_config(page_title="Gemini Tarot Mystery", page_icon="🔮")

# CSS ကို နာမည်ဖျောက်ဖို့နဲ့ ခလုတ်လှလှလေးဖြစ်ဖို့ ပြင်ထားပါတယ်
st.markdown("""
    <style>
    .stImage > img {
        width: 100% !important;
        height: 280px !important;
        object-fit: contain !important;
        background-color: #1a1a1a;
        border-radius: 8px;
    }
    /* ခလုတ်ကို ကတ်ပုံနဲ့ တစ်သားတည်းဖြစ်အောင် ညှိခြင်း */
    div.stButton > button {
        width: 100%;
        height: 45px;
        background-color: #2e2e2e;
        color: white;
        border: 1px solid #444;
        border-radius: 0 0 8px 8px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #4a4a4a;
        border: 1px solid #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 သင်၏ ကံကြမ္မာကတ်ကို ရွေးချယ်ပါ")
st.write("ကတ်ပုံပေါ်ရှိ 'ရွေးချယ်မည်' ခလုတ်ကို နှိပ်၍ ဟောကိန်းထုတ်နိုင်ပါသည်။")

base_url = "https://raw.githubusercontent.com/siriussai666/gemini-tarot-app/main/"

# ၂၂ ကတ်လုံး စာရင်း
cards = {
    "The Sun": base_url + "the_sun.jpg",
    "The Fool": base_url + "the_fool.jpg",
    "The Magician": base_url + "the_magic.jpg",
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

# Gallery ပြသခြင်း (နာမည်မပါဘဲ ခလုတ်ပဲပြပါမယ်)
cols = st.columns(4)
card_list = list(cards.items())

for i in range(len(card_list)):
    name, img_url = card_list[i]
    with cols[i % 4]:
        st.image(img_url)
        # ခလုတ်မှာ နာမည်မပြဘဲ "ရွေးချယ်မည်" လို့ပဲ ပြပါမယ်
        if st.button(f"ရွေးချယ်မည်", key=f"btn_{i}"):
            st.session_state.selected_card = name

# ဟောချက်အပိုင်း (ကတ်ရွေးပြီးမှ နာမည်ကို Gemini က ပြောပြမှာပါ)
if st.session_state.selected_card:
    st.divider()
    if st.button("ဟောကိန်းထုတ်ရန် နှိပ်ပါ ✨"):
        with st.spinner('Gemini က ကတ်ကို ဖတ်နေပါတယ်...'):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"မင်းက တားရော့ဟောဆရာ Gemini ဖြစ်တယ်။ {st.session_state.selected_card} ကတ်အကြောင်းကို မြန်မာလို အသေးစိတ် ဟောပေးပါ။ အစမှာ သင်ရွေးချယ်လိုက်တဲ့ကတ်ကတော့ {st.session_state.selected_card} ဖြစ်ပါတယ် လို့ အသိပေးပါ။"
            response = model.generate_content(prompt)
            st.write(response.text)
            # ဟောပြီးရင် Reset လုပ်ချင်ရင် သုံးနိုင်ပါတယ်
            if st.button("ကတ်အသစ် ပြန်ရွေးမည်"):
                st.session_state.selected_card = None
                st.rerun()
