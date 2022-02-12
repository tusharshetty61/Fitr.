import streamlit as st

with st.form('initial input'):
    ht=st.number_input("Enter height in cm")
    wt=st.number_input("Enter weight in kgs")
    activity=st.radio("Enter ypur activity level", ["1:Little to no exercise", "2:Exercise 1-3 days","3:3-5 days of exercise","4:Exercise 6-7 days","5:Physical job/training"])
    temp=activity.split(":")
    act=int(temp[0])
    gender=st.text_input("Enter gender M/F")
    age=st.number_input("Enter age")
    hours=st.number_input("Enter number of hours")
    submit=st.submit_form_button("Calculate wellness score")
if submit:
    User.update_user_stats(ht,wt,act,gender,age,hours)