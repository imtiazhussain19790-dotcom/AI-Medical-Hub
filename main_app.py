import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="AI Pro Medical Hub", page_icon="🏥", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("🏥 AI Pro Medical Hub")
st.sidebar.subheader("Advanced Diagnosis System")
selection = st.sidebar.selectbox(
    "Select a Service:", 
    ["🏠 Home", "⚖️ BMI Calculator", "🩸 Diabetes Prediction", "❤️ Heart Disease", "🧪 Liver Function", "🧠 Parkinson's Check", "👨‍💻 About Me"]
)

# --- 3. Home Page ---
if selection == "🏠 Home":
    st.title("🏥 Welcome to AI Pro Medical Hub")
    st.subheader("Professional Grade Health Screening Tool")
    st.markdown("""
    Ye app medical standards ke mutabiq design ki gayi hai. 
    Aap sidebar se test select karein aur apni detail reports enter karein.
    """)
    st.info("📢 **Updates:** Ab har test mein advanced parameters shamil kar diye gaye hain.")

# --- 4. BMI Calculator (Advanced) ---
elif selection == "⚖️ BMI Calculator":
    st.title("⚖️ Advanced BMI & Body Analysis")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("Select Gender", ["Male", "Female"])
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
        weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
    with col2:
        st.write("Height Input:")
        feet = st.number_input("Feet", min_value=1, max_value=8, value=5)
        inches = st.number_input("Inches", min_value=0, max_value=11, value=7)
    
    if st.button("Calculate Detailed BMI"):
        # Height conversion to meters
        total_inches = (feet * 12) + inches
        height_m = total_inches * 0.0254
        bmi = weight / (height_m * height_m)
        
        st.divider()
        st.subheader(f"Your BMI: {bmi:.2f}")
        
        if bmi < 18.5: st.warning("Category: Underweight")
        elif 18.5 <= bmi < 25: st.success("Category: Healthy")
        elif 25 <= bmi < 30: st.info("Category: Overweight")
        else: st.error("Category: Obese")
        
        # Ideal Weight Logic
        ideal_weight = 22 * (height_m * height_m)
        st.write(f"💡 Your Ideal Weight should be around: **{ideal_weight:.1f} kg**")

# --- 5. Diabetes Prediction (Clinical Parameters) ---
elif selection == "🩸 Diabetes Prediction":
    st.title("🩸 Clinical Diabetes Risk Analysis")
    st.write("Please enter your latest lab report values:")
    
    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input("Pregnancies (0 if Male)", 0, 20, 0)
        glucose = st.number_input("Glucose Level (mg/dL)", 0, 500, 100)
        bp = st.number_input("Blood Pressure (Diastolic)", 0, 150, 80)
    with col2:
        skin = st.number_input("Skin Thickness (mm)", 0, 100, 20)
        insulin = st.number_input("Insulin Level (mu U/ml)", 0, 900, 80)
        pedigree = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)

    if st.button("Predict Diabetes Risk"):
        if glucose > 140 or insulin > 160 or pedigree > 0.8:
            st.error("Result: High Risk Indicators. Please consult a doctor.")
        else:
            st.success("Result: Low Risk. Your parameters are within normal clinical range.")

# --- 6. Heart Disease (Cardiology Parameters) ---
elif selection == "❤️ Heart Disease":
    st.title("❤️ Advanced Heart Health Analysis")
    col1, col2 = st.columns(2)
    with col1:
        age_h = st.number_input("Age", 1, 120, 45)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
        trestbps = st.number_input("Resting BP (mm Hg)", 80, 200, 120)
    with col2:
        chol = st.number_input("Serum Cholestoral (mg/dl)", 100, 600, 200)
        fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", ["True", "False"])
        thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
        oldpeak = st.number_input("ST Depression induced by exercise", 0.0, 6.0, 1.0)

    if st.button("Analyze Heart Health"):
        if trestbps > 140 or chol > 240 or thalach < 100:
            st.error("Result: Cardiovascular Risk Detected. Specialist consultation recommended.")
        else:
            st.success("Result: Heart indicators appear healthy.")

# --- 7. Liver Function (Hepatology Parameters) ---
elif selection == "🧪 Liver Function":
    st.title("🧪 Full Liver Function Analysis (LFT)")
    col1, col2 = st.columns(2)
    with col1:
        tot_bil = st.number_input("Total Bilirubin", 0.0, 10.0, 1.0)
        dir_bil = st.number_input("Direct Bilirubin", 0.0, 10.0, 0.3)
        alkphos = st.number_input("Alkaline Phosphatase", 10, 500, 100)
    with col2:
        sgpt = st.number_input("Alamine Aminotransferase (SGPT)", 5, 200, 30)
        sgot = st.number_input("Aspartate Aminotransferase (SGOT)", 5, 200, 30)
        prot = st.number_input("Total Proteins", 1.0, 10.0, 7.0)
        alb = st.number_input("Albumin", 1.0, 10.0, 4.0)

    if st.button("Run Liver Diagnosis"):
        if tot_bil > 1.2 or sgpt > 40 or sgot > 40:
            st.error("Result: Liver Enzymes/Bilirubin are High. Possible Liver Stress.")
        else:
            st.success("Result: Liver Function is Normal.")

# --- 8. Parkinson's Check (Neurological Voice Analysis) ---
elif selection == "🧠 Parkinson's Check":
    st.title("🧠 Parkinson's Voice Stability Analysis")
    st.write("Advanced Voice Frequency (MDVP) Parameters:")
    col1, col2 = st.columns(2)
    with col1:
        fo = st.number_input("Average Vocal Fundamental Frequency (Hz)", 50.0, 300.0, 150.0)
        hi = st.number_input("Maximum Vocal Fundamental Frequency (Hz)", 50.0, 500.0, 200.0)
        lo = st.number_input("Minimum Vocal Fundamental Frequency (Hz)", 50.0, 300.0, 100.0)
    with col2:
        jitter = st.number_input("MDVP:Jitter(%)", 0.0, 0.1, 0.005, format="%.5f")
        shimmer = st.number_input("MDVP:Shimmer", 0.0, 0.2, 0.02, format="%.5f")
        hnr = st.number_input("HNR (Harmonics-to-Noise Ratio)", 0.0, 50.0, 20.0)

    if st.button("Run Neurological Analysis"):
        if jitter > 0.01 or hnr < 15 or shimmer > 0.05:
            st.error("Result: High Jitter/Shimmer detected. Possible Neurological Indicators.")
        else:
            st.success("Result: Voice stability is within healthy range.")

# --- 9. About Me ---
elif selection == "👨‍💻 About Me":
    st.title("👨‍💻 Developer Information")
    st.info("Developed by: **Imtiaz Hussain**")
    st.write("This application uses clinical ranges to provide preliminary health assessments.")
    st.divider()
    st.caption("⚠️ **Medical Disclaimer:** This app is for informational purposes. It does NOT replace professional medical advice, diagnosis, or treatment.")

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.caption("© 2026 AI Pro Medical Hub | v2.0")
