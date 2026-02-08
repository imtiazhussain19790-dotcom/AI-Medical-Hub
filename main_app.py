import streamlit as st

# 1. Page Configuration (Browser tab settings)
st.set_page_config(page_title="AI Pro Medical Hub", page_icon="🏥", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("🏥 AI Pro Medical Hub")
st.sidebar.markdown("---")
selection = st.sidebar.selectbox(
    "Select a Service:", 
    ["🏠 Home", "⚖️ BMI Calculator", "🩸 Diabetes Prediction", "❤️ Heart Disease", "🧪 Liver Function", "🧠 Parkinson's Check", "💡 Health Tips", "👨‍💻 About Me"]
)

# --- 3. Home Page ---
if selection == "🏠 Home":
    st.title("🏥 Welcome to AI Pro Medical Hub")
    st.subheader("Advanced Health Monitoring & AI Diagnosis System")
    st.image("https://img.icons8.com/fluency/150/medical-heart.png")
    st.markdown("""
    Ye system aapki makhsoos report values ke mutabiq design kiya gaya hai. 
    Aap sidebar se test select karein aur tamam darj shuda parameters fill karein.
    
    ### **Available Services:**
    * **BMI Analysis:** Full body mass index with ideal weight.
    * **Diabetes Check:** Clinical analysis including Glucose, Insulin & BMI.
    * **Heart Health:** Cardio parameters like Cholesterol & BP.
    * **Liver Function:** Detailed LFT (Bilirubin, SGPT, Proteins).
    * **Parkinson's:** Neurological voice stability analysis.
    """)
    st.success("📢 **Status:** All systems are active and updated (v3.5)")

# --- 4. BMI Calculator (Full Parameters) ---
elif selection == "⚖️ BMI Calculator":
    st.title("⚖️ Advanced BMI & Body Analysis")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("Select Gender", ["Male", "Female"])
        age = st.number_input("Enter Your Age", 1, 120, 25)
        weight = st.number_input("Weight (kg)", 1.0, 300.0, 70.0)
    with col2:
        st.write("Enter Height:")
        feet = st.number_input("Feet", 1, 8, 5)
        inches = st.number_input("Inches", 0, 11, 7)
    
    if st.button("Calculate Detailed BMI"):
        height_m = ((feet * 12) + inches) * 0.0254
        bmi = weight / (height_m * height_m)
        st.divider()
        st.subheader(f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5:
            st.warning("Category: Underweight")
            st.info("💡 **Tip:** Protein rich diet lein aur muscle building exercises karein.")
        elif 18.5 <= bmi < 25:
            st.success("Category: Healthy Weight")
            st.info("💡 **Tip:** Bohat achay! Isi tawazun ko barkarar rakhein.")
        elif 25 <= bmi < 30:
            st.info("Category: Overweight")
            st.info("💡 **Tip:** Rozana 30 mins brisk walk aur sugar kam karein.")
        else:
            st.error("Category: Obese")
            st.info("💡 **Tip:** Proper diet plan aur cardio exercises ko tarjeeh dein.")

# --- 5. Diabetes Prediction (With Clinical BMI Input) ---
elif selection == "🩸 Diabetes Prediction":
    st.title("🩸 Clinical Diabetes Risk Analysis")
    st.write("Lab Report ke mutabiq values enter karein:")
    col1, col2 = st.columns(2)
    with col1:
        age_d = st.number_input("Enter Age", 1, 120, 25)
        preg = st.number_input("Pregnancies (0 if Male)", 0, 20, 0)
        glucose = st.number_input("Glucose Level (mg/dL)", 0, 500, 100)
        bmi_val = st.number_input("Your BMI Value (if known)", 10.0, 70.0, 22.5) # BMI Input Added Here
    with col2:
        bp_d = st.number_input("Blood Pressure (Diastolic)", 0, 150, 80)
        skin = st.number_input("Skin Thickness (mm)", 0, 100, 20)
        ins = st.number_input("Insulin Level", 0, 900, 80)
        pedi = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)

    if st.button("Predict Diabetes Risk"):
        # Risk logic based on glucose and obesity (BMI)
        if glucose > 140 or ins > 160 or bmi_val > 30:
            st.error("Result: High Risk Indicators Detected")
            st.markdown("💡 **Diabetes Tip:** Meethi cheezon se parhez karein aur fiber wali gaza (sabziyan) zyada lein.")
        else:
            st.success("Result: Indicators are within Normal Range")

# --- 6. Heart Disease (Cardiology Inputs) ---
elif selection == "❤️ Heart Disease":
    st.title("❤️ Cardiology Health Analysis")
    col1, col2 = st.columns(2)
    with col1:
        age_h = st.number_input("Age of Patient", 1, 120, 45)
        sex = st.selectbox("Sex (Male=1, Female=0)", [1, 0])
        cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
        trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
    with col2:
        chol = st.number_input("Serum Cholestoral (mg/dl)", 100, 600, 200)
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
        thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
        oldpeak = st.number_input("ST Depression induced by exercise", 0.0, 6.0, 1.0)

    if st.button("Analyze Heart Health"):
        if chol > 240 or trestbps > 140 or thalach < 100:
            st.error("Result: Potential Cardiovascular Risk")
            st.markdown("💡 **Heart Tip:** Namak aur talay hue khanay kam karein. Rozana walk lazmi karein.")
        else:
            st.success("Result: Heart Indicators look Stable")

# --- 7. Liver Function (Full LFT Inputs) ---
elif selection == "🧪 Liver Function":
    st.title("🧪 Full Liver Function Analysis (LFT)")
    col1, col2 = st.columns(2)
    with col1:
        age_l = st.number_input("Patient Age", 1, 120, 30)
        l_gender = st.selectbox("Gender", ["Male", "Female"])
        tot_bil = st.number_input("Total Bilirubin", 0.0, 10.0, 1.0)
        alkphos = st.number_input("Alkaline Phosphatase", 10, 500, 100)
    with col2:
        sgpt = st.number_input("SGPT (ALT) Level", 5, 200, 30)
        sgot = st.number_input("SGOT (AST) Level", 5, 200, 30)
        prot = st.number_input("Total Proteins", 1.0, 10.0, 7.0)
        alb = st.number_input("Albumin Level", 1.0, 10.0, 4.0)

    if st.button("Run Liver Diagnosis"):
        if tot_bil > 1.2 or sgpt > 40 or sgot > 40:
            st.error("Result: Liver Enzymes/Bilirubin are Abnormal")
            st.markdown("💡 **Liver Tip:** Alcohol/Processed food band karein. Pani zyada piyein.")
        else:
            st.success("Result: Liver Function is Normal")

# --- 8. Parkinson's Check (Neurological Inputs) ---
elif selection == "🧠 Parkinson's Check":
    st.title("🧠 Parkinson's Neurological Check")
    col1, col2 = st.columns(2)
    with col1:
        age_p = st.number_input("Patient's Age", 1, 120, 60)
        fo = st.number_input("Average Vocal Freq (Hz)", 50.0, 300.0, 150.0)
        fhi = st.number_input("Maximum Vocal Freq (Hz)", 50.0, 500.0, 200.0)
    with col2:
        jit = st.number_input("MDVP:Jitter(%)", 0.0, 0.1, 0.005, format="%.5f")
        shim = st.number_input("MDVP:Shimmer", 0.0, 0.2, 0.02, format="%.5f")
        hnr = st.number_input("HNR (Noise Ratio)", 0.0, 50.0, 20.0)

    if st.button("Analyze Voice Stability"):
        if jit > 0.01 or hnr < 15:
            st.error("Result: Indicators of Parkinson's Found")
            st.markdown("💡 **Health Tip:** Specialist Doctor (Neurologist) se ruju karein.")
        else:
            st.success("Result: No Significant Indicators Found")

# --- 9. Health Tips Section ---
elif selection == "💡 Health Tips":
    st.title("💡 General Health & Wellness Guide")
    t1, t2, t3 = st.tabs(["🍎 Daily Diet", "🏃 Physical Activity", "🧘 Mental Health"])
    with t1:
        st.write("✅ **Proteins:** Eggs, Fish, aur Daalein apni gaza mein shamil karein.")
        st.write("✅ **Sugar:** White sugar aur cold drinks se mukammal parhez karein.")
        st.write("✅ **Hydration:** Din mein kam az kam 10 glass pani piyein.")
    with t2:
        st.write("✅ **Brisk Walk:** Rozana 30 minute tez chalna dil ke liye behtareen hai.")
        st.write("✅ **Strength:** Hafte mein do bar halki wazan uthane wali exercise karein.")
    with t3:
        st.write("✅ **Sleep:** Rozana 7 se 8 ghante ki neend lazmi hai.")
        st.write("✅ **Stress:** Deep breathing aur meditation ke liye 10 minute nikaalein.")

# --- 10. About Me ---
elif selection == "👨‍💻 About Me":
    st.title("👨‍💻 Developer Information")
    st.info("Developed by: **Imtiaz Hussain**")
    st.write("Ye application health metrics ko analyze karne ke liye banayi gayi hai.")
    st.warning("⚠️ **Disclaimer:** Ye sirf screening tool hai. Asli ilaj ke liye Doctor se mashwara karein.")

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 AI Pro Medical Hub | Secure v3.5")
