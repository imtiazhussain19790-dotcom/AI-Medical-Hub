import streamlit as st
import pickle
# Sidebar for Navigation
st.sidebar.title("Main Menu")
selection=st.sidebar.selectbox("Choose an App",["Home", "BMI Calculator", "Diabetes Prediction", "Heart Disease"])
# Home Page
if selection == "Home":
  st.title("Welcome to AI Medical Hub")
  st.subheader("Your All-in-One Health Monitoring System") 
  st.write("This Portal allows you to check your health statususing various AI tools.")
  # BMI Calculator Page
elif selection == "BMI Calculator":
    st.title("Advanced BMI Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input("Enter your Weight (in kg)", min_value=1.0)
        age = st.number_input("Enter your Age", min_value=1, max_value=120)
        
    with col2:
        height = st.number_input("Enter your Height (in meters)", min_value=0.1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    if st.button("Calculate BMI"):
        if height > 0:
            bmi = weight / (height * height)
            st.write(f"### Your BMI is: {bmi:.2f}")
            
            # Age ke mutabiq thoda farq padta hai, lekin standard range ye hai:
            if bmi < 18.5:
                st.warning(f"Age {age}: You are Underweight")
            elif 18.5 <= bmi < 25:
                st.success(f"Age {age}: You are Healthy/Normal")
            elif 25 <= bmi < 30:
                st.info(f"Age {age}: You are Overweight")
            else:
                st.error(f"Age {age}: Obesity detected")
        else:
            st.error("Height must be greater than 0")

# اب ڈائیبیٹیز والا حصہ بالکل بائیں طرف (Margin پر) ہونا چاہیے
elif selection == "Diabetes Prediction":
    st.title("Diabetes Prediction (Detailed Analysis)")
    
    col1, col2 = st.columns(2)
    with col1:
        glucose = st.number_input('Glucose Level', min_value=0)
        blood_pressure = st.number_input('Blood Pressure Value', min_value=0)
        insulin = st.number_input('Insulin Level', min_value=0)
    with col2:
        bmi_val = st.number_input('BMI Value', min_value=0.0)
        age_db = st.number_input('Age', min_value=1)
        pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)

    if st.button("Diabetes Test Result"):
        # بہتر لاجک
        if (glucose > 140 and age_db > 40) or (glucose > 170) or (bmi_val > 35 and glucose > 125):
            st.error("The system predicts a High Risk of Diabetes.")
        elif glucose > 100:
            st.warning("Pre-diabetic stage: Please control your sugar intake.")
        else:
            st.success("Result: Healthy (Not Diabetic)")
elif selection == "Heart Disease":
    st.title("Heart Disease Analysis")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input('Age', min_value=1)
        sex = st.selectbox('Sex', ['Male', 'Female'])
    with col2:
        trestbps = st.number_input('Resting BP', min_value=50)
        chol = st.number_input('Cholesterol', min_value=100)
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120', ['Yes', 'No'])
        cp = st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3])

    if st.button("Check Heart Health"):
        # اسمارٹ لاجک
        is_male = 1 if sex == 'Male' else 0
        has_fbs = 1 if fbs == 'Yes' else 0
        
        if (age > 50 and chol > 240) or (trestbps > 150) or (cp > 1 and age > 45):
            st.error("High Risk: Significant indicators of heart issues detected.")
        else:
            st.success("Low Risk: Your heart parameters seem within normal range.")
