#activity levels(act):
# from multiprocessing.dummy import active_children


# 1=sedentary
# 2=lightly active
# 3=moderately active
# 4=very active
# 5= extra active
def cintake(wt,ht,gender,age,act):
    x=0.0
    if(gender=='M'):
        x=9.99*wt+6.25*ht-4.92*age+5
    else:
        x=9.99*wt+6.25*ht-4.92*age-161
    

    if(act==1):
        return x*1.2
    elif act==2:
        return x*1.375
    elif act==3:
        return x*1.55
    elif act==4:
        return x*1.725
    else:
        x*1.9
    
#need to write function for activity levelhuhuhu


def heartScore(age,rate,act):
    score=10
    max_rate=220-age
    min_range=0.5*max_rate
    max_range=0.85*max_rate
    if act<3:
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
    
def update_score(ht,wt,act,gender,age,hours,rate,bf,food):
    bmi=wt*100*100/(ht*ht)
    status=""
    if(bmi<18.5):
        status='underweight'
    elif bmi>18.5 and bmi<=24.9:
        status="normal"
    elif bmi>=25 and bmi<=29.9:
        status="overweight"
    else:
        status="obese"
    
    calorie=cintake(wt,ht,gender,age,act)
    heart=heartRate(age,rate,act)
    sleep=sleep_score(hours,bf,age)
    cal_score= calorie- calc_calories(food)
    phy_wellness= heart*100 + sleep*100 - cal_score
    #men_health= load model and give output

    

