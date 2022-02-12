import streamlit as st
import pandas as pd
import numpy as np
from multiapp import MultiApp
import Goal,Progress,Contact


app= MultiApp()
app.add_app("Contact us",Contact.app)
app.add_app("Progress",Progress.app)
app.add_app("Set Monthly Goal",Goal.app)
st.header("Fitr.")
st.subheader("Welcome user")
st.sidebar.write("How can we help you :D?")
progress = st.sidebar.button("Progress")
screentime = st.sidebar.button("Screentime")
goal = st.sidebar.button("Monthly set goal")
contact = st.sidebar.button("Contact us")


container = st.container()
container.write("Heyy welcome to Fitr !  Feel free to explore the app as you wish. Use the sidebar to navigate through the app. The current page shows your current activity stats for the day")

col1,col2,col3 = st.columns(3)
col1.write("Steps:")
col2.write("Screen Time:")
col3.write("Mood:")
app.run()


