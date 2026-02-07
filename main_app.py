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
elif selection == "Diabetes Prediction":
    st.title("Diabetes Page is under maintenance")
elif selection == "Heart Disease":
    st.title("Heart Disease Page is under maintenance")

