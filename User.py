import streamlit as st

class User:

    def __init__(self, username,milestone1,milestone2):
        self.user=username
        self.goals= {}
        self.uinfo={}
        self.milestone_steps=milestone1
        self.milestone_screentime=milestone2
        self.status=""
        
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
        return status

    def cintake(self):
        x=0.0
        if(self.uinfo['gender']=='M'):
            x=9.99*self.uinfo['wt']+6.25*self.uinfo['ht']-4.92*self.uinfo['age']+5
        else:
            x=9.99*self.uinfo['wt']+6.25*self.uinfo['ht']-4.92*self.uinfo['age']-161
        

        if(self.uinfo['activity']==1):
            return x*1.2
        elif self.uinfo['activity']==2:
            return x*1.375
        elif self.uinfo['activity']==3:
            return x*1.55
        elif self.uinfo['activity']==4:
            return x*1.725
        else:
            x*1.9
        
    #need to write function for self.uinfo['activity']ivity levelhuhuhu


def heartScore(self,rate):
    score=10
    max_rate=220-self.uinfo['age']
    min_range=0.5*max_rate
    max_range=0.85*max_rate
    if self.uinfo['activity']<3:
        if rate<min_range and rate>max_range:
            score=score-2
        if rate>max_rate:
            score =score -1
    
    else:
        if rate<min_range and rate>max_rate:
            score=score-2
    return score

#breakfast bool value
#scores - if good then
# best score 10, worst score 6, mid way score 8
def sleep_score(hours, breakfast,age):
    score=10
    if(age>=13 and age<=18):
        if(hours>=10 or hours<=8):
            score = score - 2    

    if(age>18 or age<=64):
        if(hours>9 or hours<7):
            score = score - 2

    if(age>64):
        if(hours>8 or hours<7):
            score = score - 2; 
    if breakfast:
        score=score-2
    return score

def calc_calories(food):
    return 1
    
def update_score(self):
    bmi=self.uinfo['wt']*100*100/(self.uinfo['ht']*self.uinfo['ht'])
    self.status=""
    if(bmi<18.5):
        self.status='underweight'
    elif bmi>18.5 and bmi<=24.9:
        self.status="normal"
    elif bmi>=25 and bmi<=29.9:
        self.status="overweight"
    else:
        self.status="obese"
    
    calorie=cintake(wt,ht,gender,age,self.uinfo['activity'])
    heart=heartRate(age,rate,self.uinfo['activity'])
    sleep=sleep_score(hours,bf,age)
    cal_score= calorie- calc_calories(food)
    phy_wellness= heart*100 + sleep*100 - cal_score
    #men_health= load model and give output
