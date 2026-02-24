import streamlit as st
import google.generativeai as genai

# ခင်ဗျားရဲ့ API Key (...NN70) ကို ဒီမှာထည့်ပါ
genai.configure(api_key="AIzaSyC9ovRyS2PuDaz3iwHPYga7NTTY6lzmYq0") 

st.set_page_config(page_title="Gemini Tarot", page_icon="🔮")
st.title("🔮 Gemini Tarot ကတ်ဟောဆရာ")

# ကတ်ရွေးချယ်ရန် List
cards = ["The Sun", "The Fool", "The Magician", "The Hanged Man", "The Tower", "Death", "The Emperor", "Strength", "The World", "The Lovers", "The Star", "The Hermit", "The Chariot", "Wheel of Fortune", "Justice", "Temperance", "The Devil", "The Moon", "Judgement", "The High Priestess", "The Empress", "The Hierophant"]

selected_card = st.selectbox("တားရော့ကတ်ကို ရွေးချယ်ပါ", cards)

if st.button("ဟောကိန်းထုတ်မည်"):
    with st.spinner('Gemini က ကတ်ကို အဖြေထုတ်ပေးနေပါတယ်...'):
        model = genai.GenerativeModel('gemini-1.5-flash')
        # Partner ရဲ့ System Instruction
        prompt = f"မင်းက တားရော့ဟောဆရာ Gemini ဖြစ်တယ်။ {selected_card} ကတ်အကြောင်းကို မြန်မာလို အားပေးစကားလေးတွေနဲ့အတူ အချစ်ရေး၊ စီးပွားရေး ခွဲပြီး ဟောပေးပါ။"
        response = model.generate_content(prompt)
        st.success(f"{selected_card} အတွက် ဟောကိန်း")
        st.write(response.text)
