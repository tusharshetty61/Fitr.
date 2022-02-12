import streamlit as st
import pandas as pd

food=pd.read_csv('/mnt/d/Hashcode/Hashcode_2022/data/calories.csv')
class User:

    def __init__(self, username):
        self.user=username
        self.status = " "
        self.goals= {'steps':0,'calories':0,'wellnessgoals':0,'screentimegoals':0}
        self.uinfo={'ht':0,'wt':0,'activity':0,'gender':"F",'age':0,'hours':0}
        self.tinfo={'boolBF':False,'breakfast':[],'lunch':[],'dinner':[],'heartRate':0,'hours':0,'stepsWalked':0,'phy_wellness':0}
        
    def update_user_goals(self,steps,calories,wellnessgoals,screentimegoals):
        self.goals['steps']=steps 
        self.goals['calories']=calories
        self.goals['wellnessgoals']=wellnessgoals
        self.goals['screentimegoals']=screentimegoals
    
    def update_user_stats(self,ht,wt,activity,gender,age,hours):
        self.uinfo['ht']=ht
        self.uinfo['wt']=wt
        # print(self.uinfo['wt'])
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

    def update_user_progress(self,boolBf,breakfast,lunch,dinner,rate,hoursSlept,stepsWalked):
        self.tinfo['boolBf']=boolBf
        self.tinfo['breakfast']=breakfast
        self.tinfo['lunch']=lunch
        self.tinfo['dinner']=dinner
        self.tinfo['heartRate']=rate
        self.uinfo['hours']=hoursSlept
        self.tinfo['stepsWalked']=stepsWalked
        self.update_score()

    def heartScore(self):
        score=10
        max_rate=220-self.uinfo['age']
        min_range=0.5*max_rate
        max_range=0.85*max_rate
        if int(self.uinfo['activity'])<3:
            if self.tinfo['heartRate']<min_range and self.tinfo['heartRate']>max_range:
                score=score-2
            if self.tinfo['heartRate']>max_rate:
                score =score -1
        
        else:
            if self.tinfo['heartRate']<min_range and self.tinfo['heartRate']>max_rate:
                score=score-2
        return score

    #breakfast bool value
    #scores - if good then
    # best score 10, worst score 6, mid way score 8
    def sleep_score(self):
        score=10
        if(self.uinfo['age']>=13 and self.tinfo['heartRate']<=18):
            if(self.uinfo['hours']>=10 or self.uinfo['hours']<=8):
                score = score - 2    

        if(self.tinfo['heartRate']>18 or self.tinfo['heartRate']<=64):
            if(self.uinfo['hours']>9 or self.uinfo['hours']<7):
                score = score - 2

        if(self.tinfo['heartRate']>64):
            if(self.uinfo['hours']>8 or self.uinfo['hours']<7):
                score = score - 2; 
        if self.tinfo['boolBf']==1:
            score=score-2
        return score

    def calc_calories(self):
        cal = 0
        df_cal = pd.read_csv("/mnt/d/Hashcode/Hashcode_2022/data/calories.csv")
        df_cal['Cals_per100grams'] = df_cal['Cals_per100grams'].str.replace(' cal','')
        i = 0
        for food in self.uinfo['breakfast']:
            if (df_cal['FoodItem'][i] == food):
                cal = cal + df_cal['Cals_per100grams'][i]
                i = i + 1
        i = 0
        for food in self.uinfo['lunch']:
            if (df_cal['FoodItem'][i] == food):
                cal = cal + df_cal['Cals_per100grams'][i]
                i = i + 1
        i = 0 
        for food in self.uinfo['dinner']:
            if (df_cal['FoodItem'][i] == food):
                cal = cal + df_cal['Cals_per100grams'][i]
                i = i + 1
        
        return cal
             
        
    def update_score(self):
        print(self.uinfo['wt'])
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
        
        calorie=self.cintake()
        heart=self.heartScore()
        sleep=self.sleep_score()
        cal_score= calorie- self.calc_calories()
        phy_wellness= heart*100 + sleep*100 - cal_score
        #men_health= load model and give output
        self.tinfo['phy_wellness'] = phy_wellness
