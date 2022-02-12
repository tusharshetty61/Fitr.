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
     

