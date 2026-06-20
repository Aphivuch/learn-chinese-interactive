import streamlit as st

# --- 🎨 ตั้งค่าหน้าตาเว็บ ---
st.set_page_config(page_title="ChineseLearn 🇨🇳", page_icon="🚌", layout="centered")

st.title("🇨🇳 ChineseLearn v1.0")

# --- 🚌 ส่วนที่ 1: กล่องดีไซน์รถเมล์ ---
st.info("🚌 [ ภาพรถเมล์ 公共汽车 ]")

# --- ❓ ส่วนที่ 2: โจทย์คำถาม ---
st.markdown("### **Question:**")
st.markdown("#### เราจะนั่งรถเมล์สายไหนไปวังเยาวชน?")
st.subheader("我们坐几路公共汽车去少年宫？")

st.write("---")

# --- 📢 ส่วนที่ 3: ระบบตรวจคำตอบ + เสียงออนไลน์ ---
audio_html = """
    <audio id="correct-audio" src="https://soundoftext.com/static/sounds/zh-CN/c96d859a721869e0618035bc299e900a.mp3"></audio>
    <script>
        var audio = document.getElementById('correct-audio');
        audio.play();
    </script>
"""

# สร้างปุ่ม 3 ปุ่มเรียงกันในแนวนอนสไตล์มินิเกม
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("35路", use_container_width=True):
        st.error("❌ ว้า... ยังไม่ถูก ลองใหม่อีกทีนะ!")

with col2:
    if st.button("49路", use_container_width=True):
        st.success("✅ 太棒了! (สุดยอดไปเลย!)")
        # ยิงเสียง "ไท่ป้างเลอ" ทันทีที่กดปุ่มถูก
        st.components.v1.html(audio_html, height=0, width=0)

with col3:
    if st.button("28路", use_container_width=True):
        st.error("❌ ว้า... ยังไม่ถูก ลองใหม่อีกทีนะ!")