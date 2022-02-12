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