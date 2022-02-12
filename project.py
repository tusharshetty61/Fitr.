# Modules
import pyrebase
import streamlit as st
from datetime import datetime
import Contact
from User import User
import pandas as pd

# Configuration Key
firebaseConfig = {
  'apiKey': "AIzaSyDLwwPS414RzjHi9-7gCFYs7m0oaqPjZiQ",
  'authDomain': "hashcode-test.firebaseapp.com",
  'projectId': "hashcode-test",
  'storageBucket': "hashcode-test.appspot.com",
  'messagingSenderId': "285406807460",
  'appId': "1:285406807460:web:0cb1206806800c37eead31",
  'measurementId': "G-Z60LBC3GDG",
  'databaseURL': "https://hashcode-test-default-rtdb.asia-southeast1.firebasedatabase.app/"
}


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

db = firebase.database()
storage = firebase.storage()
st.sidebar.title("Fitr.")

choice = st.sidebar.selectbox('login/Signup', ['Login', 'Sign up'])


email = st.sidebar.text_input('Please enter your email address')
password = st.sidebar.text_input('Please enter your password',type = 'password')

food = pd.read_csv('/mnt/d/Hashcode/Hashcode_2022/data/calories.csv')

if choice == 'Sign up':
    handle = st.sidebar.text_input(
        'Please input your app handle name', value='Default')
    submit = st.sidebar.button('Create my account')

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.success('Your account is created suceesfully!')
        st.balloons()
       
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user['localId']).child("Handle").set(handle)
        db.child(user['localId']).child("ID").set(user['localId'])
        st.title('Welcome' + handle)
        st.info('Login via login drop down selection')


if choice == 'Login':
    login = st.sidebar.checkbox('Login')
    if login:
        user = auth.sign_in_with_email_and_password(email,password)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        bio = st.radio('How can we help you :DD ? ',['Contact','Let us know you a bit better','Goal', 'Progress'])
        user=User('sup',10000,5)
        
        if bio == 'Contact':
            col1,col2,col3=st.columns(3)    
            col1.write("Anisha")
            col2.write("Ananya")
            col3.write("Tushar")

        elif bio=='Let us know you a bit better':
                
            with st.form('initial input'):
                ht=st.number_input("Enter height in cm")
                wt=st.number_input("Enter weight in kgs")
                activity=st.radio("Enter number of days you exercise in a week",["1:<1 days","2:1-3 days","3:3-5 days","4:6-7 days","5:physical job"])
                gender=st.text_input("Enter gender M/F")
                age=st.number_input("Enter age")
                hours=st.number_input("Enter number of hours")
                submit=st.submit_form_button("Calculate wellness score")
            if submit:
                temp=activity.split(":")
                act=int(temp[0])
                user.update_user_stats(ht,wt,act,gender,age,hours)

        elif bio == 'Goal':
            st.subheader("This month's incentives")
            st.write("Average steps mile stone and win a vacation:10000")
            st.write("Average screen time milestone and win an extended leave: 5")
            with st.form("set goals"):
                steps = st.number_input("Average daily steps")
                calories = st.number_input("Average calories per day")
                wellnessgoal = st.number_input("Score goal")
                screentimegoal=st.number_input("screen time goal in hours")
                submit_button = st.form_submit_button("submit")
            if(submit_button):
                user.update_user_goals(steps,calories,wellnessgoal,screentimegoal)  

        elif bio == 'Progress':
            fdu = food.FoodItem.unique()
            with st.form("Food habits"):
                bf=st.radio("Did you eat breakfast today?", ["1:yes","2:no"])
                breakfast=st.multiselect(label="Choose your food",options=fdu,key=1)
                lunch=st.multiselect("Choose your food",fdu,key=2)
                dinner=st.multiselect("Choose your food",fdu,key=3)
                submi2 = st.form_submit_button("submit")
            if(submi2):
                temp=bf.split(":")
                boolBf= int(temp[0])-1
                user.update_user_progress(boolBf,breakfast,lunch,dinner)
            col1,col2,col3=st.columns(3)
            col1.write("Steps:")
            col2.write("Screen Time:")
            col3.write("Mood:")
  
