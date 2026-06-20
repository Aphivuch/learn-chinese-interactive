import streamlit as st

# --- 🎨 1. ตั้งค่าหน้าตาแอปให้ใหญ่พิเศษ (Extra Large GUI) ---
st.set_page_config(page_title="ChineseLearn 🇨🇳", page_icon="🚌", layout="centered")

# ปรับแต่ง CSS เพื่อขยายขนาดทุกอย่างให้ใหญ่และดูสนุก
st.markdown("""
    <style>
    /* ขยายหัวข้อหน้า */
    .page-header { font-size: 28px; font-weight: bold; color: #95a5a6; text-align: left; margin-bottom: -20px; }

    /* ขยายหัวข้อหลัก */
    .main-title { font-size: 50px; font-weight: bold; text-align: center; color: #2c3e50; margin-bottom: 20px; }

    /* กล่องรูปรถเมล์ขนาดใหญ่ */
    .bus-card { background-color: #f1f4f9; padding: 40px; border-radius: 30px; border: 4px solid #3498db; text-align: center; font-size: 80px; margin-bottom: 30px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .bus-label { font-size: 22px; color: #34495e; font-weight: bold; display: block; margin-top: 10px; }

    /* กล่องคำถามขนาดใหญ่ */
    .question-box { font-size: 32px; font-weight: bold; text-align: center; color: #2c3e50; background: #ffffff; padding: 25px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin-bottom: 40px; line-height: 1.4; }

    /* ปรับปุ่มให้ใหญ่สะใจเด็กๆ */
    div.stButton > button {
        font-size: 30px !important;
        font-weight: bold !important;
        height: 80px !important;
        border-radius: 20px !important;
        border: 3px solid #2c3e50 !important;
        transition: 0.3s !important;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        background-color: #34495e !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# แสดงคำว่า "หน้า 1"
st.markdown('<div class="page-header">หน้า 1</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">🇨🇳 ChineseLearn</div>', unsafe_allow_html=True)

# --- 🚌 2. ส่วนแสดงภาพรถเมล์ขนาดใหญ่ ---
st.markdown('<div class="bus-card">🚌<span class="bus-label">ภาพรถเมล์ 公共汽车</span></div>', unsafe_allow_html=True)

# --- ❓ 3. ส่วนของคำถาม (ใหญ่พิเศษ) ---
st.markdown("""
    <div class="question-box">
        เราจะนั่งรถเมล์สายไหนไปวังเยาวชน?<br>
        <span style="color: #d35400; font-size: 38px;">我们坐几路公共汽车去少年宫？</span>
    </div>
""", unsafe_allow_html=True)

# --- 📢 4. ระบบจัดการเสียงและเอฟเฟกต์ ---
sound_url = "https://dict.youdao.com/dictvoice?audio=%E5%A4%AA%E6%A3%92%E4%BA%86&le=zh"
congrats_gif = "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndnZueXp6eXp6eXp6eXp6eXp6eXp6eXp6eXp6eXp6eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7abKhOpuMcmLjdcI/giphy.gif"

if "choice" not in st.session_state:
    st.session_state.choice = None

# สร้างปุ่มกด 3 ปุ่ม (ขนาดใหญ่)
col1, col2, col3 = st.columns(3)

with col1:
    label_35 = "❌ 35路" if st.session_state.choice == "35" else "35路"
    if st.button(label_35, use_container_width=True):
        st.session_state.choice = "35"

with col2:
    label_49 = "✅ 49路" if st.session_state.choice == "49" else "49路"
    if st.button(label_49, use_container_width=True):
        st.session_state.choice = "49"

with col3:
    label_28 = "❌ 28路" if st.session_state.choice == "28" else "28路"
    if st.button(label_28, use_container_width=True):
        st.session_state.choice = "28"

# --- 5. การแสดงผลลัพธ์ฉลองชัยชนะ 🎉 ---
if st.session_state.choice == "49":
    # แสดงข้อความสำเร็จ
    st.success("✅ 太棒了! (สุดยอดไปเลย!)")

    # ยิงเอฟเฟกต์ Balloons ของ Streamlit
    st.balloons()

    # แสดงภาพยินดีขนาดใหญ่ (Congratulations Visual)
    st.image(congrats_gif, use_container_width=True)

    # เล่นเสียงอัตโนมัติ
    st.audio(sound_url, format="audio/mp3", autoplay=True)

elif st.session_state.choice in ["35", "28"]:
    st.error("❌ ว้า... ยังไม่ถูก ลองใหม่อีกทีนะ!")

# เพิ่มข้อความเครดิตท้ายเว็บของคุณเดฟแบบตรงๆ ตามสั่งเลยครับ
st.success("โชคดีนะจั้ะ by:Poor_dev")