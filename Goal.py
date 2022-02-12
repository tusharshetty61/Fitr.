import streamlit as st

def app():
    with st.form("set goals"):
        steps = st.mumber_input("Averahge daily steps")
        calories = st.number_input("Average calories per day")
        wellnessgoal = st.number_input("Score goal")
        screentimegoal=st.number_input("screen time goal in hours")
        submit_button = st.form_submit_button("submit")
    if(submit_button):
        User.user_goals_update(steps,calories,wellnessgoal,screentimegoal)    