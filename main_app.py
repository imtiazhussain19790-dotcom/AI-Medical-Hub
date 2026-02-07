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
with open('diabetes_model.pkl', 'rb') as f:
    diabetes_model = pickle.load(f)
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

# Heart Disease Prediction Page
elif selection == "Heart Disease":
    st.title("Heart Disease Prediction using AI")

    # ماڈل لوڈ کریں
    try:
        # آپ کی فائل کا نام 'heart_model.pkl' ہے، اسے یہاں استعمال کریں
        heart_model = pickle.load(open('heart_model.pkl', 'rb'))
        
        st.write("Please enter the following details:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=1, step=1)
            trestbps = st.number_input('Resting Blood Pressure', min_value=1, step=1)
            chol = st.number_input('Serum Cholestoral in mg/dl', min_value=1, step=1)
            fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)', min_value=0, max_value=1)
        with col2:
            sex = st.number_input('Sex (1 = male; 0 = female)', min_value=0, max_value=1)
            restecg = st.number_input('Resting ECG results', min_value=0, max_value=2)
            thalach = st.number_input('Max Heart Rate achieved', min_value=1, step=1)
            exang = st.number_input('Exercise Induced Angina (1=Yes, 0=No)', min_value=0, max_value=1)
        with col3:
            cp = st.number_input('Chest Pain types (0-3)', min_value=0, max_value=3)
            oldpeak = st.number_input('ST depression induced by exercise', min_value=0.0)
            slope = st.number_input('Slope of the peak exercise ST segment', min_value=0, max_value=2)
            ca = st.number_input('Major vessels colored by flourosopy (0-3)', min_value=0, max_value=3)
            thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value=0, max_value=2)

        # Prediction Button
        if st.button('Heart Disease Test Result'):
            # ماڈل کو 13 ویلیوز درکار ہیں
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            prediction = heart_model.predict([user_input])
            
            if prediction[0] == 1:
                st.error('The person is predicted to have heart disease')
            else:
                st.success('The person is predicted to be healthy')
                
    except Exception as e:
        st.error(f"Error loading Heart Model: {e}")
