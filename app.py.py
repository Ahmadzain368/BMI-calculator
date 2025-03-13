import streamlit as st
import pandas as pd

# title of the web app
st.title("BMI calculator")
height = st.number_input("Enter your height in meters (e.g,1.4): ",min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight in kg (e.g,40): ",min_value=0.0, format="%.2f")
if st.button("calculate BMI"):
  if height > 0 and weight > 0:
    bmi = weight / (height**2)
    st.success(f"Your BMI is : {bmi: .2f}")

    #bmi category
    if bmi<18.5:
      st.info("you are underweight")
    elif 18.5<= bmi < 24.9:
      st.success("you are not normal age")
    elif 25 <= bmi<29.9:
      st.warning("you are overweight")
    else:
      st.error("you are obese")
  else:
    st.error("please enter valid height and weight.")







