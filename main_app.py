import streamlit as st
selection = st.sidebar.selectbox("Select Page", ["Home", "BMI Calculator", "Diabetes Prediction", "Heart Disease"])

if selection == "Home":
    st.title("Welcome to AI Medical Hub")
# --- BMI Calculator Section ---
if selection == "BMI Calculator":
    st.title("Advanced BMI Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Weight (kg)", min_value=1.0)
        age = st.number_input("Age", min_value=1)
    with col2:
        height = st.number_input("Height (meters)", min_value=0.1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / (height * height)
            st.write(f"### Your BMI is: {bmi:.2f}")
            
            if bmi < 18.5:
                st.warning("Underweight")
                st.info("💡 **Health Tips:**\n* Increase calorie intake with nutrient-dense foods.\n* Include protein-rich snacks like nuts and yogurt.\n* Consult a nutritionist for a weight gain plan.")
            elif 18.5 <= bmi < 25:
                st.success("Healthy Weight")
                st.info("💡 **Health Tips:**\n* Maintain your current lifestyle with a balanced diet.\n* Aim for at least 150 minutes of moderate exercise per week.")
            elif 25 <= bmi < 30:
                st.info("Overweight")
                st.info("💡 **Health Tips:**\n* Reduce intake of processed sugars and fried foods.\n* Focus on portion control and fiber-rich vegetables.\n* Regular cardio exercises are highly recommended.")
            else:
                st.error("Obesity")
                st.info("💡 **Health Tips:**\n* Consult a healthcare professional immediately.\n* Start with low-impact exercises like swimming or walking.\n* Limit refined carbohydrates and high-fat dairy.")

# --- Diabetes Prediction Section ---
elif selection == "Diabetes Prediction":
    st.title("Diabetes Prediction (Analysis)")
    
    col1, col2 = st.columns(2)
    with col1:
        glucose = st.number_input('Glucose Level', min_value=0)
        bp = st.number_input('Blood Pressure', min_value=0)
    with col2:
        bmi_val = st.number_input('BMI Value', min_value=0.0)
        age_db = st.number_input('Age', min_value=1)

    if st.button("Diabetes Test Result"):
        if glucose > 140:
            st.error("High Risk of Diabetes")
            st.info("💡 **Health Advice:**\n* Avoid sugary drinks, white bread, and pasta.\n* Monitor your blood sugar levels regularly.\n* Stay hydrated and increase physical activity.")
        else:
            st.success("Result: Healthy")
            st.info("💡 **Health Advice:**\n* Maintain a fiber-rich diet with whole grains.\n* Get regular health check-ups even if you feel fine.")

# --- Heart Disease Section ---
elif selection == "Heart Disease":
    st.title("Heart Disease Analysis")
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input('Patient Age', min_value=1)
        chol = st.number_input('Cholesterol Level', min_value=100)
    with col2:
        trestbps = st.number_input('Resting BP', min_value=50)
        cp = st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3])

    if st.button("Check Heart Health"):
        if (age > 50 and chol > 240) or (trestbps > 150):
            st.error("Potential Heart Risk Detected")
            st.info("💡 **Heart Care Tips:**\n* Switch to a low-sodium (salt) diet.\n* Avoid trans fats found in baked and fried goods.\n* Manage stress through meditation or light exercise.")
        else:
            st.success("Heart Risk is Low")
            st.info("💡 **Heart Care Tips:**\n* Include heart-healthy fats like olive oil and walnuts.\n* Ensure 7-8 hours of quality sleep for heart recovery.")
