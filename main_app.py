import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="AI Medical Hub", page_icon="🏥", layout="wide")

# 2. Sidebar Navigation with Icons
st.sidebar.title("🏥 AI Medical Hub")
selection = st.sidebar.selectbox(
    "Select a Service:", 
    ["🏠 Home", "⚖️ BMI Calculator", "🩸 Diabetes Prediction", "❤️ Heart Disease", "🧪 Liver Function", "🧠 Parkinson's Check", "👨‍💻 About Me"]
)

# --- 3. Home Page ---
if selection == "🏠 Home":
    st.title("🏥 Welcome to AI Medical Hub")
    st.subheader("A Complete AI-Powered Health Monitoring System")
    st.image("https://img.icons8.com/fluency/150/medical-heart.png")
    st.write("""
    Is app ke zariye aap mukhtalif bimariyon ka ibtedayi andaza laga sakte hain. 
    Bayen janib (Sidebar) se koi bhi test select karein aur apni reports ke mutabiq maloomat darj karein.
    """)
    st.success("✅ Sabhi tests ab active hain: BMI, Diabetes, Heart, Liver, aur Parkinson's.")

# --- 4. BMI Calculator ---
elif selection == "⚖️ BMI Calculator":
    st.title("⚖️ BMI Calculator")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
    with col2:
        height = st.number_input("Height (meters)", min_value=0.1, value=1.7)
    
    if st.button("Calculate BMI"):
        bmi = weight / (height * height)
        st.subheader(f"Your BMI: {bmi:.2f}")
        if bmi < 18.5: st.warning("Category: Underweight")
        elif 18.5 <= bmi < 25: st.success("Category: Healthy")
        elif 25 <= bmi < 30: st.info("Category: Overweight")
        else: st.error("Category: Obese")

# --- 5. Diabetes Prediction ---
elif selection == "🩸 Diabetes Prediction":
    st.title("🩸 Diabetes Prediction")
    glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, value=100)
    age = st.number_input('Age', min_value=1, value=25)
    
    if st.button("Check Diabetes"):
        if glucose > 140:
            st.error("Result: High Risk Indicators")
        else:
            st.success("Result: Low Risk / Normal")

# --- 6. Heart Disease ---
elif selection == "❤️ Heart Disease":
    st.title("❤️ Heart Disease Analysis")
    chol = st.number_input('Cholesterol Level', min_value=100, value=200)
    bp = st.number_input('Resting Blood Pressure', min_value=80, value=120)
    
    if st.button("Analyze Heart"):
        if chol > 240 or bp > 140:
            st.error("Result: Potential Risk Factors Detected")
        else:
            st.success("Result: Indicators are Stable")

# --- 7. Liver Function ---
elif selection == "🧪 Liver Function":
    st.title("🧪 Liver Function Test")
    bilirubin = st.number_input('Total Bilirubin', min_value=0.0, value=1.0)
    albumin = st.number_input('Albumin Level', min_value=0.0, value=4.0)
    
    if st.button("Analyze Liver"):
        if bilirubin > 1.2 or albumin < 3.4:
            st.error("Result: Abnormal Liver Indicators")
        else:
            st.success("Result: Liver Function looks Normal")

# --- 8. Parkinson's Check ---
elif selection == "🧠 Parkinson's Check":
    st.title("🧠 Parkinson's Disease Analysis")
    st.write("Voice frequency parameters and movement stability analysis.")
    jitter = st.number_input('MDVP:Jitter(%)', min_value=0.0, value=0.005, format="%.5f")
    shimmer = st.number_input('MDVP:Shimmer', min_value=0.0, value=0.02, format="%.5f")
    
    if st.button("Analyze Parkinson's"):
        if jitter > 0.01 or shimmer > 0.05:
            st.error("Result: Early Signs Detected (Consult Specialist)")
        else:
            st.success("Result: No Significant Indicators Found")

# --- 9. About Me ---
elif selection == "👨‍💻 About Me":
    st.title("👨‍💻 Developer Profile")
    st.markdown("### **Imtiaz Hussain**")
    st.info("AI & Health Tech Developer")
    st.write("Maine ye system is liye banaya taake log ghar baithe apni bunyadi sehat ka andaza laga sakein.")
    st.warning("⚠️ Disclaimer: Ye sirf educational purposes ke liye hai. Medical faislo ke liye doctor se ruju karein.")

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.caption("Powered by Streamlit | 2026")
