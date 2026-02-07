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
elif selection=="BMI Calculator":
  st.title("BMI Calculator")
  weight=st.number_input("Enter your Weight (kg)",min_value=0.1)
  height=st.number_input("Enter your Height (meters)",min_value=0.1)
  if height > 0:
      bmi=weight / (height * height)
      st.write(f"### Your BMI is: {bmi:,2f}")
      if bmi < 18.5:
        st.warning("Underweight")
      elif 18.5 <= bmi < 25:
        st.success("Healthy")
      elif 25 <= bmi < 30:
        st.info("Overweight")
      else:
        st.error("Obesity")
# Placeholder for Diabetes App
 # Diabetes Prediction Page
elif selection == "Diabetes Prediction":
    st.title("Diabetes Prediction using AI")
    
    # Load the model
    diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))
    # Input fields for user (English)
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0)
        Glucose = st.number_input("Glucose Level", min_value=0)
        BloodPressure = st.number_input("Blood Pressure value", min_value=0)
        SkinThickness = st.number_input("Skin Thickness value", min_value=0)
    with col2:
        Insulin = st.number_input("Insulin Level", min_value=0)
        BMI = st.number_input("BMI value", min_value=0.0)
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0)
        Age = st.number_input("Age of the Person", min_value=0)

    # Prediction Button
    if st.button("Diabetes Test Result"):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        diab_prediction = diabetes_model.predict([user_input])
        
        if diab_prediction[0] == 1:
              st.error("The person is Diabetic")
        else:
              st.success("The person is Not Diabetic")

# Placeholder for Heart Disease App
    elif selection == "Heart Disease":
              st.title("Heart Disease Prediction")
              st.info("Coming Soon: Integrating your Heart Disease Model here.")





