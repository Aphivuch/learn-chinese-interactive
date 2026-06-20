import customtkinter as ctk
import pyttsx3
import threading


# --- 🔊 ตั้งค่าระบบเสียงพูดสดในคอมพิวเตอร์ ---
def speak_chinese(text):
    def run_speech():
        try:
            engine = pyttsx3.init()
            # พยายามปรับให้เป็นเสียงภาษาจีนกลาง (zh-CN) ถ้าเครื่องรองรับ
            voices = engine.getProperty('voices')
            for voice in voices:
                if 'zh' in voice.id.lower() or 'chinese' in voice.name.lower():
                    engine.setProperty('voice', voice.id)
                    break
            engine.setProperty('rate', 150)  # ความเร็วเสียงพูด
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print("🔊 ระบบเสียงในเครื่องมีปัญหา:", e)

    # รันแยกเธรดเพื่อไม่ให้หน้าต่างแอปค้างเวลาพูด
    threading.Thread(target=run_speech, daemon=True).start()


# --- 🎯 ฟังก์ชันตรวจคำตอบ ---
def check_answer(choice):
    if choice == "49路":
        result_label.configure(text="✅ 太棒了! (สุดยอดไปเลย!)", text_color="#2ecc71")
        speak_chinese("太棒了")  # สั่งคอมพิวเตอร์พูดสดๆ เลยคำนี้
    else:
        result_label.configure(text="❌ ว้า... ยังไม่ถูก ลองใหม่อีกทีนะ!", text_color="#e74c3c")


# --- 🎨 ตั้งค่าหน้าจอโปรแกรม ---
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("🇨🇳 เกมตอบคำถามภาษาจีน v1.2 (System Voice)")
root.geometry("650x500")

# --- 🚌 1. ส่วนแสดงภาพรถเมล์ ---
image_frame = ctk.CTkFrame(master=root, height=120, fg_color="#34495e")
image_frame.pack(pady=20, padx=40, fill="x")

bus_label = ctk.CTkLabel(
    master=image_frame,
    text="🚌 [ ภาพรถเมล์公共汽车 ]",
    font=("Arial", 20, "bold"),
    text_color="white"
)
bus_label.place(relx=0.5, rely=0.5, anchor="center")

# --- ❓ 2. ส่วนของคำถามภาษาจีน ---
question_label = ctk.CTkLabel(
    master=root,
    text="Question:\nเราจะนั่งรถเมล์สายไหนไปวังเยาวชน?\n我们坐几路公共汽车去少年宫？",
    font=("Arial", 20, "bold"),
    justify="center"
)
question_label.pack(pady=10)

# --- 📢 3. ส่วนแสดงผลลัพธ์ ---
result_label = ctk.CTkLabel(
    master=root,
    text="เลือกคำตอบด้านล่างได้เลย 👇",
    font=("Arial", 18, "bold"),
    text_color="#95a5a6"
)
result_label.pack(pady=10)

# --- 📦 4. กล่องใส่ปุ่มตัวเลือก ---
button_frame = ctk.CTkFrame(master=root, fg_color="transparent")
button_frame.pack(pady=20, padx=40, fill="x")

button_style = {
    "font": ("Arial", 20, "bold"),
    "height": 55,
    "corner_radius": 15,
    "fg_color": "#2c3e50",
    "hover_color": "#34495e"
}

btn_35 = ctk.CTkButton(master=button_frame, text="35路", command=lambda: check_answer("35路"), **button_style)
btn_35.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

btn_49 = ctk.CTkButton(master=button_frame, text="49路", command=lambda: check_answer("49路"), **button_style)
btn_49.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

btn_28 = ctk.CTkButton(master=button_frame, text="28路", command=lambda: check_answer("28路"), **button_style)
btn_28.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

button_frame.grid_columnconfigure((0, 1, 2), weight=1)

root.mainloop()