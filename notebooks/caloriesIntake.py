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
    

