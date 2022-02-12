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
    
    def update_user_stats(self,ht,wt,activity,gender,age,hours):
        self.uinfo['ht']=ht
        self.uinfo['wt']=wt
        self.uinfo['activity']=activity
        self.uinfo['gender']=gender
        self.uinfo['age']=age
        self.uinfo['hours']=hours
        