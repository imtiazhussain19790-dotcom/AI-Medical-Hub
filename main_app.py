import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="AI Pro Medical Hub", page_icon="🏥", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("🏥 AI Pro Medical Hub")
selection = st.sidebar.selectbox(
    "Select a Service:", 
    ["🏠 Home", "⚖️ BMI Calculator", "🩸 Diabetes Prediction", "❤️ Heart Disease", "🧪 Liver Function", "🧠 Parkinson's Check", "💡 Health Tips", "👨‍💻 About Me"]
)

# --- 3. Home Page ---
if selection == "🏠 Home":
    st.title("🏥 Welcome to AI Pro Medical Hub")
    st.subheader("Your Advanced AI Health Partner")
    st.image("https://img.icons8.com/fluency/150/medical-heart.png")
    st.markdown("""
    Ye app clinical standards ke mutabiq design ki gayi hai. 
    Aap sidebar se test select karein aur apni detail reports enter karein.
    """)
    st.info("📢 **Updates:** Ab har test ke sath aapko makhsoos Health Tips bhi di jayengi.")

# --- 4. BMI Calculator (With Health Tips) ---
elif selection == "⚖️ BMI Calculator":
    st.title("⚖️ BMI & Body Analysis")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
        feet = st.number_input("Height: Feet", min_value=1, max_value=8, value=5)
        inches = st.number_input("Height: Inches", min_value=0, max_value=11, value=7)
    
    if st.button("Calculate BMI"):
        total_inches = (feet * 12) + inches
        height_m = total_inches * 0.0254
        bmi = weight / (height_m * height_m)
        st.subheader(f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("Category: Underweight")
            st.write("💡 **Tip:** Proteins aur Healthy Fats ka istemal badhayein.")
        elif 18.5 <= bmi < 25:
            st.success("Category: Healthy")
            st.write("💡 **Tip:** Isi tarah protein aur exercise ka tawazun barkarar rakhein.")
        else:
            st.error("Category: Overweight/Obese")
            st.write("💡 **Tip:** Rozana 30 mins paidal chalein aur junk food se parhez karein.")

# --- 5. Diabetes Prediction (With Clinical Tips) ---
elif selection == "🩸 Diabetes Prediction":
    st.title("🩸 Diabetes Risk Analysis")
    glucose = st.number_input("Glucose Level (mg/dL)", 0, 500, 100)
    insulin = st.number_input("Insulin Level", 0, 900, 80)
    
    if st.button("Predict Diabetes"):
        if glucose > 140:
            st.error("Result: High Risk Indicators")
            st.markdown("""
            ### 💡 Health Tips for High Glucose:
            * **Sugar se parhez:** Meethi cheezon aur soft drinks se door rahein.
            * **Fiber:** Sabziyon aur phal ka istemal zyada karein.
            * **Water:** Rozana 8-10 glass pani piyein.
            """)
        else:
            st.success("Result: Normal")
            st.write("💡 **Tip:** Har 6 mahine baad apna checkup karwate rahein.")

# --- 6. Heart Disease (With Cardio Tips) ---
elif selection == "❤️ Heart Disease":
    st.title("❤️ Heart Health Analysis")
    chol = st.number_input("Serum Cholestoral (mg/dl)", 100, 600, 200)
    bp = st.number_input("Resting BP (mm Hg)", 80, 200, 120)
    
    if st.button("Analyze Heart"):
        if chol > 240 or bp > 140:
            st.error("Result: Risk Factors Detected")
            st.markdown("""
            ### 💡 Heart Care Tips:
            * **Namak kam karein:** BP control karne ke liye namak ka istemal kam karein.
            * **Healthy Fats:** Fried food ke bajaye nuts aur olive oil istemal karein.
            * **Walk:** Dil ki mazbooti ke liye tez chalna behtareen exercise hai.
            """)
        else:
            st.success("Result: Healthy Indicators")
            st.write("💡 **Tip:** Stress kam karein aur neend puri karein.")

# --- 7. Liver Function (With Liver Tips) ---
elif selection == "🧪 Liver Function":
    st.title("🧪 Liver Function Analysis")
    tot_bil = st.number_input("Total Bilirubin", 0.0, 10.0, 1.0)
    sgpt = st.number_input("SGPT Level", 5, 200, 30)
    
    if st.button("Analyze Liver"):
        if tot_bil > 1.2 or sgpt > 40:
            st.error("Result: Liver Stress Detected")
            st.markdown("""
            ### 💡 Liver Health Tips:
            * **Paani ka istemal:** Liver se zehreele mada nikalne ke liye pani piyein.
            * **Processed Food:** Packaged aur processed food se parhez karein.
            * **Green Tea:** Liver ki safayi mein madad deti hai.
            """)
        else:
            st.success("Result: Normal")

# --- 8. Parkinson's Check ---
elif selection == "🧠 Parkinson's Check":
    st.title("🧠 Parkinson's Analysis")
    jitter = st.number_input("MDVP:Jitter(%)", 0.0, 0.1, 0.005, format="%.5f")
    
    if st.button("Analyze"):
        if jitter > 0.01:
            st.error("Result: Neurological Indicators Found")
            st.write("💡 **Tip:** Demaaghi sukoon ke liye Yoga aur Meditation karein.")
        else:
            st.success("Result: Normal")

# --- 9. NEW SECTION: General Health Tips ---
elif selection == "💡 Health Tips":
    st.title("💡 General Health & Wellness Tips")
    st.subheader("Sehatmand Zindagi ke Sunheri Usool")
    
    tab1, tab2, tab3 = st.tabs(["Diet Plan", "Exercise", "Mental Health"])
    
    with tab1:
        st.write("🍎 **Dietary Advice:**")
        st.write("- Rozana kam az kam 5 tarah ki sabziyan aur phal khayein.")
        st.write("- Pani ka zyada istemal karein (3 Liters daily).")
        st.write("- Raat ka khana sone se 3 ghante pehle khayein.")
    
    with tab2:
        st.write("🏃 **Physical Activity:**")
        st.write("- Hafta mein 150 minute ki exercise lazmi karein.")
        st.write("- Lift ke bajaye seedhiyon ka istemal karein.")
    
    with tab3:
        st.write("🧘 **Mental Well-being:**")
        st.write("- Rozana 7-8 ghante ki pur-sukoon neend lein.")
        st.write("- Gehre saans lene ki mashq (Deep Breathing) karein.")

# --- 10. About Me ---
elif selection == "👨‍💻 About Me":
    st.title("👨‍💻 Developer Profile")
    st.info("Developed by: **Imtiaz Hussain**")
    st.write("AI Solutions for Healthcare.")

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 AI Pro Medical Hub")
