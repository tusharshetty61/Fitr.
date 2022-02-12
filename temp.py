import streamlit as st 
import pandas as pd

food = pd.read_csv('C:/Users/anany/Documents/GitHub/Hashcode_2022/data/calories.csv')


def calc_calories(breakfast,lunch,dinner):
    cal = 0
    df_cal = pd.read_csv("C:/Users/anany/Documents/GitHub/Hashcode_2022/data/calories.csv")
    df_cal['Cals_per100grams'] = df_cal['Cals_per100grams'].str.replace(' cal','')
    i = 0
    for food in breakfast:
        if (df_cal['FoodItem'][i] == food):
            cal = cal + int(df_cal['Cals_per100grams'][i])
            i = i + 1
    i = 0
    for food in lunch:
        if (df_cal['FoodItem'][i] == food):
            cal = cal + int(df_cal['Cals_per100grams'][i])
            i = i + 1
    i = 0 
    for food in dinner:
        if (df_cal['FoodItem'][i] == food):
            cal = cal + int(df_cal['Cals_per100grams'][i])
            i = i + 1
    return cal

fdu = food.FoodItem.unique()
with st.form("Food habits"):
    # bf=st.radio("Did you eat breakfast today?", ["1:yes","2:no"])
    breakfast=st.multiselect(label="Choose your food",options=fdu,key=1)
    lunch=st.multiselect("Choose your food",fdu,key=2)
    dinner=st.multiselect("Choose your food",fdu,key=3)
    submi2 = st.form_submit_button("submit")
if(submi2):
    cal = calc_calories(breakfast,lunch,dinner)
    print(cal)
    # temp=bf.split(":")
    # boolBf= int(temp[0])-1
    # rate=1
    # hoursSlept=1
    # StepsWalked=1
    # user.update_user_progress(boolBf,breakfast,lunch,dinner,rate,hoursSlept,StepsWalked)