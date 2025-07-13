import streamlit as st
st.title("BMI Calculator")

 
weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.1, format="%.2f")


if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    
     
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    
    st.success(f"Your BMI is: {bmi:.2f}")
    st.info(f"Category: {category}")
