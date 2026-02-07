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
      st.write(f"### Your BMI is: {bmi:.2f}")
      if bmi < 18.5:
          st.warning("Underweight")
      elif 18.5 <= bmi < 25:
          st.success("Healthy")
      elif 25 <= bmi < 30:
          st.info("Overweight")
      else:
          st.error("Obesity")

# اب ڈائیبیٹیز والا حصہ بالکل بائیں طرف (Margin پر) ہونا چاہیے
elif selection == "Diabetes Prediction":
    st.title("Diabetes Page is under maintenance")

elif selection == "Heart Disease":
    st.title("Heart Disease Prediction")
    
    try:
        # ماڈل لوڈ کرنے کی کوشش
        heart_model = pickle.load(open('heart_model.pkl', 'rb'))
        
        st.info("Please enter the patient details below:")
        
        # ان پٹ فیلڈز
        age = st.number_input('Age', min_value=1, step=1)
        sex = st.selectbox('Sex', [0, 1], help="1 = Male, 0 = Female")
        cp = st.selectbox('Chest Pain Type (0-3)', [0, 1, 2, 3])
        trestbps = st.number_input('Resting Blood Pressure', min_value=50)
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value=100)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1])
        restecg = st.number_input('Resting ECG results (0-2)', min_value=0, max_value=2)
        thalach = st.number_input('Maximum Heart Rate achieved', min_value=50)
        exang = st.selectbox('Exercise Induced Angina', [0, 1])
        oldpeak = st.number_input('ST depression', min_value=0.0)
        slope = st.number_input('Slope (0-2)', min_value=0, max_value=2)
        ca = st.number_input('Major vessels (0-3)', min_value=0, max_value=3)
        thal = st.number_input('thal (0-2)', min_value=0, max_value=2)

        if st.button("Predict Heart Disease"):
            features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            prediction = heart_model.predict([features])
            
            if prediction[0] == 1:
                st.error("Warning: The model predicts a high risk of Heart Disease.")
            else:
                st.success("Good News: The model predicts a low risk of Heart Disease.")
                
    except Exception as e:
        st.warning("Heart Disease model file is missing or corrupted. Please check 'heart_model.pkl'.")
        st.error(f"Error details: {e}")

