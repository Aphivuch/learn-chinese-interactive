import streamlit as st

# --- 🎨 ตั้งค่าหน้าตาเว็บให้ดูดีและพรีเมียม ---
st.set_page_config(page_title="ChineseLearn 🇨🇳", page_icon="🚌", layout="centered")

# ตกแต่งสไตล์เพิ่มเติมให้สวยงาม
st.markdown("""
    <style>
    .big-title { font-size: 36px; font-weight: bold; text-align: center; color: #2c3e50; margin-bottom: 20px; }
    .bus-template { background-color: #f0f3f6; padding: 20px; border-radius: 15px; border-left: 10px solid #3498db; margin-bottom: 25px; text-align: center; font-size: 24px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🇨🇳 ChineseLearn v1.1</div>', unsafe_allow_html=True)

# --- 🚌 ส่วนที่ 1: กล่องดีไซน์รถเมล์แบบดูดีขึ้น ---
st.markdown('<div class="bus-template">🚌 [ ภาพรถเมล์ 公共汽车 ]</div>', unsafe_allow_html=True)

# --- ❓ ส่วนที่ 2: โจทย์คำถาม ---
st.markdown("### ❓ **คำถามประจำวัน**")
st.markdown("#### เราจะนั่งรถเมล์สายไหนไปวังเยาวชน?")
st.subheader("我们坐几路公共汽车去少年宫？")

st.write("---")

# --- 📢 ส่วนที่ 3: ระบบตรวจคำตอบ + แถบเครื่องเล่นเสียงแก้ปัญหาเสียงหาย ---
# ลิงก์เสียงออนไลน์คำว่า "ไท่ป้างเลอ"
sound_url = "https://soundoftext.com/static/sounds/zh-CN/c96d859a721869e0618035bc299e900a.mp3"

# สร้างปุ่ม 3 ปุ่มเรียงกันในแนวนอน
col1, col2, col3 = st.columns(3)

# สร้างสเตตัสเก็บค่าการกดคำตอบเพื่อไม่ให้เสียงหายเวลาหน้าจอรี่เฟรช
if "answered_correct" not in st.session_state:
    st.session_state.answered_correct = False

with col1:
    if st.button("35路", use_container_width=True):
        st.session_state.answered_correct = False
        st.error("❌ ว้า... ยังไม่ถูก ลองใหม่อีกทีนะ!")

with col2:
    if st.button("49路", use_container_width=True):
        st.session_state.answered_correct = True

with col3:
    if st.button("28路", use_container_width=True):
        st.session_state.answered_correct = False
        st.error("❌ ว้า... ยังไม่ถูก ลองใหม่อีกทีนะ!")

# ถ้ากดเลือก 49路 (คำตอบที่ถูก)
if st.session_state.answered_correct:
    st.success("✅ 太棒了! (สุดยอดไปเลย!)")
    st.markdown("👇 **กดฟังเสียงพูดภาษาจีนตรงนี้ได้เลยครับ**")
    # แสดงแถบเล่นเสียงของ Streamlit โดยตรง (แก้ปัญหาเสียงเงียบ)
    st.audio(sound_url, format="audio/mp3", autoplay=True)