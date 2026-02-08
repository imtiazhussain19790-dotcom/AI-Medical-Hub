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
    st.subheader("Advanced Health Monitoring & Recommendations")
    st.image("https://img.icons8.com/fluency/150/medical-heart.png")
    st.markdown("""
    Ye system aapki makhsoos report values ke mutabiq design kiya gaya hai. 
    Aap sidebar se test select karein aur tamam darj shuda parameters fill karein.
    """)
    st.success("📢 **Status:** Tamam Advanced Inputs aur Health Tips ab active hain!")

# --- 4. BMI Calculator (Advanced Inputs + Tips) ---
elif selection == "⚖️ BMI Calculator":
    st.title("⚖️ Advanced BMI Analysis")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("Select Gender", ["Male", "Female"])
        age = st.number_input("Age", 1, 120, 25)
        weight = st.number_input("Weight (kg)", 1.0, 300.0, 70.0)
    with col2:
        feet = st.number_input("Height: Feet", 1, 8, 5)
        inches = st.number_input("Height: Inches", 0, 11, 7)
    
    if st.button("Calculate BMI"):
        height_m = ((feet * 12) + inches) * 0.0254
        bmi = weight / (height_m * height_m)
        st.subheader(f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("Category: Underweight")
            st.info("💡 **Health Tip:** Protein-rich diet (eggs, milk, nuts) aur muscle-building exercise karein.")
        elif 18.5 <= bmi < 25:
            st.success("Category: Healthy")
            st.info("💡 **Health Tip:** Isi tarah protein aur exercise ka tawazun barkarar rakhein.")
        elif 25 <= bmi < 30:
            st.info("Category: Overweight")
            st.info("💡 **Health Tip:** Rozana 30-45 mins walk karein aur sugary drinks se parhez karein.")
        else:
            st.error("Category: Obese")
            st.info("💡 **Health Tip:** Proper diet plan follow karein aur cardio exercises ko tarjeeh dein.")

# --- 5. Diabetes Prediction (All Lab Parameters + Tips) ---
elif selection == "🩸 Diabetes Prediction":
    st.title("🩸 Clinical Diabetes Analysis")
    col1, col2 = st.columns(2)
    with col1:
        preg = st.number_input("Pregnancies (0 if Male)", 0, 20, 0)
        glucose = st.number_input("Glucose Level (mg/dL)", 0, 500, 100)
        bp = st.number_input("Blood Pressure (Diastolic)", 0, 150, 80)
    with col2:
        skin = st.number_input("Skin Thickness (mm)", 0, 100, 20)
        ins = st.number_input("Insulin Level", 0, 900, 80)
        pedi = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)

    if st.button("Predict Risk"):
        if glucose > 140 or ins > 160:
            st.error("Result: High Risk Detected")
            st.markdown("💡 **Diabetes Tip:** Carbs kam karein, fiber zyada lein aur pani ka istemal badhayein.")
        else:
            st.success("Result: Healthy Range")

# --- 6. Heart Disease (All Cardiology Inputs + Tips) ---
elif selection == "❤️ Heart Disease":
    st.title("❤️ Cardiology Health Analysis")
    col1, col2 = st.columns(2)
    with col1:
        h_age = st.number_input("Age", 1, 120, 45)
        trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
        chol = st.number_input("Serum Cholestoral (mg/dl)", 100, 600, 200)
    with col2:
        thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
        oldpeak = st.number_input("ST Depression (Exercise)", 0.0, 6.0, 1.0)
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])

    if st.button("Analyze Heart"):
        if chol > 240 or trestbps > 140:
            st.error("Result: Potential Cardiovascular Risk")
            st.markdown("💡 **Heart Tip:** Namak aur talay hue khanay band karein. Omega-3 rich food (Fish, Walnuts) lein.")
        else:
            st.success("Result: Heart Indicators Stable")

# --- 7. Liver Function (All LFT Inputs + Tips) ---
elif selection == "🧪 Liver Function":
    st.title("🧪 Full Liver Function Analysis (LFT)")
    col1, col2 = st.columns(2)
    with col1:
        tot_bil = st.number_input("Total Bilirubin", 0.0, 10.0, 1.0)
        alkphos = st.number_input("Alkaline Phosphatase", 10, 500, 100)
        sgpt = st.number_input("SGPT (ALT)", 5, 200, 30)
    with col2:
        sgot = st.number_input("SGOT (AST)", 5, 200, 30)
        prot = st.number_input("Total Proteins", 1.0, 10.0, 7.0)
        alb = st.number_input("Albumin Level", 1.0, 10.0, 4.0)

    if st.button("Analyze Liver"):
        if tot_bil > 1.2 or sgpt > 40:
            st.error("Result: Liver Enzymes Elevated")
            st.markdown("💡 **Liver Tip:** Alcohol/Processed food se parhez karein. Green tea aur Garlic ka istemal karein.")
        else:
            st.success("Result: Liver Indicators Normal")

# --- 8. Parkinson's Check (Advanced Voice Inputs + Tips) ---
elif selection == "🧠 Parkinson's Check":
    st.title("🧠 Parkinson's Neurological Analysis")
    col1, col2 = st.columns(2)
    with col1:
        fo = st.number_input("Avg Vocal Freq (Hz)", 50.0, 300.0, 150.0)
        fhi = st.number_input("Max Vocal Freq (Hz)", 50.0, 500.0, 200.0)
        flo = st.number_input("Min Vocal Freq (Hz)", 50.0, 300.0, 100.0)
    with col2:
        jit = st.number_input("MDVP:Jitter(%)", 0.0, 0.1, 0.005, format="%.5f")
        shim = st.number_input("MDVP:Shimmer", 0.0, 0.2, 0.02, format="%.5f")
        hnr = st.number_input("HNR", 0.0, 50.0, 20.0)

    if st.button("Run Analysis"):
        if jit > 0.01 or hnr < 15:
            st.error("Result: Indicators Found")
            st.markdown("💡 **Brain Health Tip:** Mental exercises (puzzles) karein aur Omega-3 diet ko tarjeeh dein.")
        else:
            st.success("Result: All Clear")

# --- 9. Health Tips Section ---
elif selection == "💡 Health Tips":
    st.title("💡 Complete Wellness Guide")
    t1, t2, t3 = st.tabs(["Daily Diet", "Exercise Plan", "Sleep & Mind"])
    with t1:
        st.write("✅ **Protein:** Har meal mein shamil karein.\n✅ **Sugar:** Kam se kam karein.\n✅ **Water:** 8-12 glass lazmi.")
    with t2:
        st.write("✅ **Cardio:** 30 mins (Brisk Walk).\n✅ **Strength:** Hafte mein 2 din weights.")
    with t3:
        st.write("✅ **Sleep:** 7-8 ghante.\n✅ **Stress:** Deep breathing aur meditation.")

# --- 10. About Me ---
elif selection == "👨‍💻 About Me":
    st.title("👨‍💻 Developer")
    st.info("Created by: **Imtiaz Hussain**")
    st.caption("Medical Disclaimer: This is for educational screening only.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("v2.5 - Professional Edition")
