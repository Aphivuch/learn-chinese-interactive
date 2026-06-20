import streamlit as st

# --- 🎨 1. ตั้งค่าหน้าตาแอปให้พรีเมียม เรียบหรู ---
st.set_page_config(page_title="ChineseLearn 🇨🇳", page_icon="🚌", layout="centered")

# ใช้ CSS ปรับแต่ง UI ให้ดูสะอาด และดึงปลั๊กอินเอฟเฟกต์พลุกระดาษ (Confetti) มาเตรียมไว้
st.markdown("""
    <style>
    .main-title { font-size: 36px; font-weight: bold; text-align: center; color: #2c3e50; margin-bottom: 20px; }
    .bus-container { background-color: #f8f9fa; padding: 30px; border-radius: 20px; border: 3px solid #3498db; text-align: center; font-size: 40px; margin-bottom: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    .bus-text { font-size: 18px; color: #7f8c8d; font-weight: normal; margin-top: 5px; }
    .question-text { font-size: 24px; font-weight: bold; text-align: center; color: #2c3e50; line-height: 1.6; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🇨🇳 ChineseLearn</div>', unsafe_allow_html=True)

# --- 🚌 2. ส่วนแสดงภาพรถเมล์ ---
st.markdown('<div class="bus-container">🚌<div class="bus-text">ภาพรถเมล์ 公共汽车</div></div>', unsafe_allow_html=True)

# --- ❓ 3. ส่วนของคำถาม ---
st.markdown(
    '<div class="question-text">เราจะนั่งรถเมล์สายไหนไปวังเยาวชน?<br><span style="color: #e67e22; font-size: 28px;">我们坐几路公共汽车去少年宫？</span></div>',
    unsafe_allow_html=True)

# --- 📢 4. ระบบตรวจคำตอบและสเตตัสเสียง "太棒了！" ---
# ลิงก์เสียงภาษาจีนกลางคำว่า 太棒了！ (Tài bàng le!) ของจริง ชัดแจ๋ว
sound_url = "https://dict.youdao.com/dictvoice?audio=%E5%A4%AA%E6%A3%92%E4%BA%86&le=zh"

# โค้ด JavaScript สำหรับยิงเอฟเฟกต์พลุกระดาษฉลองเต็มหน้าจอ
confetti_html = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        // ยิงพลุกระดาษทันที
        confetti({
            particleCount: 150,
            spread: 80,
            origin: { y: 0.6 }
        });
    </script>
"""

# สร้างตัวแปรเก็บสถานะการเลือกตอบ เพื่อแสดงผล ❌ หรือ ✅ หน้าปุ่ม
if "choice_status" not in st.session_state:
    st.session_state.choice_status = None

# สร้างปุ่มกด 3 ปุ่มเรียงกันในแนวนอน
col1, col2, col3 = st.columns(3)

with col1:
    btn_35_label = "❌ 35路" if st.session_state.choice_status == "35" else "35路"
    if st.button(btn_35_label, use_container_width=True):
        st.session_state.choice_status = "35"

with col2:
    btn_49_label = "✅ 49路" if st.session_state.choice_status == "49" else "49路"
    if st.button(btn_49_label, use_container_width=True):
        st.session_state.choice_status = "49"

with col3:
    btn_28_label = "❌ 28路" if st.session_state.choice_status == "28" else "28路"
    if st.button(btn_28_label, use_container_width=True):
        st.session_state.choice_status = "28"

st.write("")

# --- 5. ส่วนแสดงผลลัพธ์ การเล่นเสียงออโต้ และเอฟเฟกต์ ---
if st.session_state.choice_status == "49":
    st.success("✅ 太棒了! (สุดยอดไปเลย!)")

    # 1. ยิงเอฟเฟกต์พลุกระดาษกระจายเต็มจอ 🎉
    st.components.v1.html(confetti_html, height=0, width=0)

    # 2. เปิดเสียง "ไท่ป้างเลอ!" ขึ้นเองทันทีแบบซ่อนเครื่องเล่น (เนียนตา 100%)
    st.audio(sound_url, format="audio/mp3", autoplay=True)

elif st.session_state.choice_status in ["35", "28"]:
    st.error("❌ ว้า... ยังไม่ถูก ลองใหม่อีกทีนะ!")