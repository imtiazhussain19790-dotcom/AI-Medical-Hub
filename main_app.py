import streamlit as st

# 1. Page Configuration (App ka title aur icon browser tab ke liye)
st.set_page_config(page_title="AI Medical Hub", page_icon="🏥")

# 2. Sidebar Navigation (Sirf ye ek menu rahega)
st.sidebar.title("📌 Main Menu")
selection = st.sidebar.selectbox(
    "Select a Service:", 
    ["Home", "BMI Calculator", "Diabetes Prediction", "Heart Disease", "About Me"]
)

# --- 3. Home Page ---
if selection == "Home":
    st.title("🏥 AI Medical Hub")
    st.subheader("Your Intelligent Health Companion")
    st.image("https://img.icons8.com/fluency/150/medical-heart.png")
    st.write("""
    Welcome! This AI-powered tool helps you monitor your health status based on medical logic. 
    Select a tool from the sidebar to get started.
    """)
    st.info("💡 **Note:** Stay active and eat healthy for a better lifestyle!")

# --- 4. BMI Calculator ---
elif selection == "BMI Calculator":
    st.title("⚖️ BMI Calculator")
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
    with col2:
        height = st.number_input("Height (meters)", min_value=0.1, value=1.7)
    
    if st.button("Calculate BMI"):
        bmi = weight / (height * height)
        st.subheader(f"Your BMI: {bmi:.2f}")
        if bmi < 18.5:
            st.warning("Category: Underweight")
            st.write("👉 Focus on a protein-rich diet.")
        elif 18.5 <= bmi < 25:
            st.success("Category: Healthy")
            st.write("👉 Keep up the good work!")
        elif 25 <= bmi < 30:
            st.info("Category: Overweight")
            st.write("👉 Try adding 30 mins of daily exercise.")
        else:
            st.error("Category: Obese")
            st.write("👉 Consult a specialist for a weight management plan.")

# --- 5. Diabetes Prediction ---
elif selection == "Diabetes Prediction":
    st.title("🩸 Diabetes Risk Check")
    glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, value=100)
    age = st.number_input('Age', min_value=1, value=25)
    
    if st.button("Predict"):
        if glucose > 140:
            st.error("Status: High Risk Indicators")
            st.write("⚠️ High glucose detected. Reduce sugar and consult a doctor.")
        else:
            st.success("Status: Normal")
            st.write("✅ Your glucose levels are within the safe range.")

# --- 6. Heart Disease ---
elif selection == "Heart Disease":
    st.title("❤️ Heart Health Analysis")
    chol = st.number_input('Cholesterol Level', min_value=100, value=200)
    bp = st.number_input('Resting Blood Pressure', min_value=80, value=120)
    
    if st.button("Analyze"):
        if chol > 240 or bp > 140:
            st.error("Status: Risk Factors Detected")
            st.write("⚠️ High cholesterol or BP can affect heart health. Take less salt.")
        else:
            st.success("Status: Healthy Indicators")
            st.write("✅ Your heart indicators look stable.")

# --- 7. About Me ---
elif selection == "About Me":
    st.title("👨‍💻 About the Project")
    st.markdown("### **Developer: Imtiaz Hussain**")
    st.write("This app is developed to provide quick health insights using Python and Streamlit.")
    st.divider()
    st.caption("⚠️ Disclaimer: This is an AI tool for educational purposes. Always consult a real doctor for medical decisions.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2026 AI Medical Hub")
