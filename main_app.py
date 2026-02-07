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
    st.title("Diabetes Prediction (Direct Logic)")
    
    glucose = st.number_input('Glucose Level', min_value=0)
    bmi_val = st.number_input('BMI Value', min_value=0.0)
    age_db = st.number_input('Age of the person', min_value=1)

    if st.button("Diabetes Test Result"):
        # ڈائیبیٹیز کے لیے میڈیکل اسٹینڈرڈ لاجک
        if glucose > 140 or (bmi_val > 30 and glucose > 120):
            st.error("The person is predicted to be Diabetic.")
        else:
            st.success("The person is predicted to be Not Diabetic.")
elif selection == "Heart Disease":
    st.title("Heart Disease Prediction (Direct Logic)")
    
    st.info("Entering data for AI analysis...")
    age = st.number_input('Age', min_value=1, step=1)
    chol = st.number_input('Serum Cholestoral', min_value=100)
    trestbps = st.number_input('Resting Blood Pressure', min_value=80)

    if st.button("Predict Heart Disease"):
        # ایک سادہ لیکن موثر میڈیکل لاجک
        if (age > 55 and chol > 240) or (trestbps > 150 and age > 50):
            st.error("High Risk Detected: The system suggests a high probability of heart issues.")
        else:
            st.success("Low Risk: Based on the current parameters, your heart health looks stable.")
