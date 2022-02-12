import streamlit as st

with st.form('initial input'):
    ht=st.number_input("Enter height in cm")
    wt=st.number_input("Enter weight in kgs")
    activity=st.number_input("Enter number of days you exercise in a week")
    gender=st.text_input("Enter gender M/F")
    age=st.number_input("Enter age")
    hours=st.number_input("Enter number of hours")
    submit=st.submit_form_button("Calculate wellness score")
if submit:
    User.update_user_stats(ht,wt,activity,gender,age,hours)