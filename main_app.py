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
    st.subheader("Smart Health Monitoring with Built-in Medical Guidance")
    st.image("https://img.icons8.com/fluency/150/medical-heart.png")
    st.info("📢 **New Feature:** Har input box ke sath bane ہوئے (?) icon par click karke uski tafseel parhein.")

# --- 4. BMI Calculator ---
elif selection == "⚖️ BMI Calculator":
    st.title("⚖️ BMI & Body Composition")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("Gender", ["Male", "Female"], help="Aapki jins metabolism aur body fat distribution par asar andaz hoti hai.")
        age = st.number_input("Age", 1, 120, 25, help="Umar ke sath sath sahi BMI ki range badal sakti hai.")
        weight = st.number_input("Weight (kg)", 1.0, 300.0, 70.0, help="Apna wazan kilogram mein darj karein.")
    with col2:
        feet = st.number_input("Height: Feet", 1, 8, 5)
        inches = st.number_input("Height: Inches", 0, 11, 7)
    
    if st.button("Analyze BMI"):
        height_m = ((feet * 12) + inches) * 0.0254
        bmi = weight / (height_m * height_m)
        st.subheader(f"Your BMI: {bmi:.2f}")
        if bmi < 18.5: st.warning("Category: Underweight")
        elif 18.5 <= bmi < 25: st.success("Category: Healthy")
        else: st.error("Category: Overweight/Obese")

# --- 5. Diabetes Prediction (With Detailed Info) ---
elif selection == "🩸 Diabetes Prediction":
    st.title("🩸 Clinical Diabetes Analysis")
    col1, col2 = st.columns(2)
    with col1:
        age_d = st.number_input("Age", 1, 120, 25)
        glucose = st.number_input("Glucose Level", 0, 500, 100, help="Khoon mein mojood cheeni ki miqdar. Normal fasting range 70-100 mg/dL hoti hai.")
        ins = st.number_input("Insulin Level", 0, 900, 80, help="Wo hormone jo sugar control karta hai. Iska level lulba (Pancreas) ki karkardagi batata hai.")
        bmi_val = st.number_input("BMI Value", 10.0, 70.0, 22.5, help="Body Mass Index. Zyada BMI sugar ke khatre ko badha deta hai.")
    with col2:
        bp_d = st.number_input("Blood Pressure", 0, 150, 80, help="Diastolic BP (niche wala number).")
        skin = st.number_input("Skin Thickness", 0, 100, 20, help="Triceps ki jild ki motayi, jo jism mein charbi (Fat) ka andaza deti hai.")
        pedi = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5, help="Khandani history ka score. Agar family mein sugar hai to ye score zyada hota hai.")

    if st.button("Predict Diabetes Risk"):
        if glucose > 140 or bmi_val > 30:
            st.error("Result: High Risk Indicators")
        else: st.success("Result: Healthy Range")

# --- 6. Heart Disease (With Info) ---
elif selection == "❤️ Heart Disease":
    st.title("❤️ Heart Health Analysis")
    col1, col2 = st.columns(2)
    with col1:
        trestbps = st.number_input("Resting BP", 80, 200, 120, help="Sukun ki halat mein dil ka dabao.")
        chol = st.number_input("Cholesterol", 100, 600, 200, help="Khoon mein mojood charbi. 240 se zyada khatarnak ho sakta hai.")
    with col2:
        thalach = st.number_input("Max Heart Rate", 60, 220, 150, help="Exercise ke doran dil ki maximum raftaar.")
        oldpeak = st.number_input("ST Depression", 0.0, 6.0, 1.0, help="ECG mein anay wali tabdeeli jo dil ki kamzori zahir karti hai.")

    if st.button("Analyze Heart"):
        if chol > 240 or trestbps > 140: st.error("Result: Potential Risk")
        else: st.success("Result: Healthy")

# --- 7. Liver Function (With Info) ---
elif selection == "🧪 Liver Function":
    st.title("🧪 Liver Function Analysis (LFT)")
    col1, col2 = st.columns(2)
    with col1:
        tot_bil = st.number_input("Total Bilirubin", 0.0, 10.0, 1.0, help="Piliya (Jaundice) check karne ke liye. Normal range 1.2 tak hoti hai.")
        sgpt = st.number_input("SGPT (ALT)", 5, 200, 30, help="Liver enzyme. Iska badhna liver mein sozish (Inflammation) zahir karta hai.")
    with col2:
        alkphos = st.number_input("Alkaline Phosphatase", 10, 500, 100, help="Hadiyon aur liver ki sehat ka indicator.")
        alb = st.number_input("Albumin", 1.0, 10.0, 4.0, help="Liver mein banne wala protein.")

    if st.button("Run Liver Diagnosis"):
        if tot_bil > 1.2 or sgpt > 40: st.error("Result: Abnormal Values")
        else: st.success("Result: Normal")

# --- 8. Parkinson's Check (With Info) ---
elif selection == "🧠 Parkinson's Check":
    st.title("🧠 Parkinson's Voice Analysis")
    col1, col2 = st.columns(2)
    with col1:
        jit = st.number_input("MDVP:Jitter(%)", 0.0, 0.1, 0.005, format="%.5f", help="Awaz mein larzish (Frequency variation). Parkinson's mein ye badh jati hai.")
        shim = st.number_input("MDVP:Shimmer", 0.0, 0.2, 0.02, format="%.5f", help="Awaz ki bulandi (Amplitude) mein ghair-mustahkam tabdeeli.")
    with col2:
        hnr = st.number_input("HNR", 0.0, 50.0, 20.0, help="Awaz ki safayi (Harmonics-to-Noise Ratio). Kam HNR khurduri awaz zahir karta hai.")

    if st.button("Analyze Voice"):
        if jit > 0.01 or hnr < 15: st.error("Result: Risk Detected")
        else: st.success("Result: Stable")

# --- 9. Health Tips & 10. About Me ---
elif selection == "💡 Health Tips":
    st.title("💡 Daily Health Guide")
    st.write("✅ Pani ka kasrat se istemal karein.\n✅ Namak aur cheeni kam karein.\n✅ Rozana 30 minute exercise karein.")

elif selection == "👨‍💻 About Me":
    st.title("👨‍💻 Developer")
    st.info("Imtiaz Hussain - AI Medical Hub")

st.sidebar.markdown("---")
st.sidebar.caption("v4.0 - Integrated Clinical Help")
