from turtle import color
import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 
import seaborn as sns

daily_activity_merged_df = pd.read_csv("C:/Users/anany/Documents/GitHub/Hashcode_2022/data/dailyActivity_merge.csv")
sleep_day_merged_df = pd.read_csv("C:/Users/anany/Documents/GitHub/Hashcode_2022/data/sleepDay_merged.csv")
def graph1():
    i = 0
    daily_step = []
    daily_activity = []
    while(daily_activity_merged_df['Id'][i]==1503960366):
        daily_step.append(daily_activity_merged_df['TotalSteps'][i])
        daily_activity.append(daily_activity_merged_df['ActivityDate'][i])
        i = i + 1
    st.subheader("Daily Steps VS Daily Activity")


    daily_step = np.asarray(daily_step)
    daily_activity = np.asarray(daily_activity)

    fig = plt.figure(figsize=(7,5))
    sns.set_style("darkgrid")
    sns.set(rc={'axes.facecolor':'black', 'figure.facecolor':'black'})
    bx = sns.barplot(x=daily_activity,y=daily_step,palette = "magma")
    bx.axhline(10000,color="yellow",linewidth=3.0)
    st.pyplot(fig)

def graph2():
    i = 0
    daily_sleep = []
    date = []
    while(sleep_day_merged_df['Id'][i]==1503960366):
        date.append(sleep_day_merged_df['SleepDay'][i])
        daily_sleep.append(sleep_day_merged_df['TotalMinutesAsleep'][i])
        i = i + 1
    st.subheader("Daily Sleep VS Date")

    fig = plt.figure(figsize=(7,5))
    sns.set_style("darkgrid")
    sns.set(rc={'axes.facecolor':'black', 'figure.facecolor':'black'})
    bx = sns.barplot(x=date,y=daily_sleep,palette = "mako")
    bx.axhline(360,color="yellow",linewidth=3.0)
    st.pyplot(fig)

# graph1()
# graph2()