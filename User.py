import streamlit as st

class User:

    def __init__(self, username):
        self.user=username
        self.goals= {}
        self.uinfo={}
        
    def update_user_goals(self,steps,calories,wellnessgoals,screentimegoals):
        self.goals['steps']=steps 
        self.goals['calories']=calories
        self.goals['wellnessgoals']=wellnessgoals
        self.goals['screentimegoals']=screentimegoals
    
    def update_user_(self,ht,wt,activity,gender,age,hours):
        self.uinfo['ht']=ht
        self.uinfo['wt']=wt
        self.uinfo['activity']=activity
        self.uinfo['gender']=gender
        self.uinfo['age']=age
        self.uinfo['hours']=hours
    
    def update_obese_state(self):
        bmi=self.uinfo['wt']*100*100/(self.uinfo['ht']*self.uinfo['ht'])
        status=""
        if(bmi<18.5):
            status='underweight'
        elif bmi>18.5 and bmi<=24.9:
            status="normal"
        elif bmi>=25 and bmi<=29.9:
            status="overweight"
        else:
            status="obese"