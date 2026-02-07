import streamlit as st
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
  elif selection == "Diabetes Prediction":
    st.title("Diabetes Prediction")
    st.info("Coming Soon: Integrating your Diabetes Model here.")

# Placeholder for Heart Disease App
  elif selection == "Heart Disease":
    st.title("Heart Disease Prediction")
    st.info("Coming Soon: Integrating your Heart Disease Model here.")





