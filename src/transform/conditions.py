def temperature_category(tem):
    if tem < 10 :
        return 20
    elif tem > 10 and tem < 18:
        return 10
    elif tem > 18 and tem < 25:
        return 0
    elif tem > 25 and tem < 35:
        return 15
    else : 
        return 25


def precipitation_category(pre):
    if pre == 0:
        return 0
    elif pre > 0 and pre < 2:
        return 5
    elif pre > 2 and pre < 10:
        return 15
    else : 
        return 25



def wind_category(wind):
    if wind < 10 :
        return 0
    elif  wind > 10 and wind < 30 :
        return 5
    elif wind > 30 and wind < 50:
        return 10
    else :
        return 25



def precipitation_probability(pro):

    if pro < 20:
        return 0
    elif pro < 50:
        return 5
    elif pro < 80:
        return 15
    else:
        return 25



def risk_level(score):
    if score <= 30:
        return "LOW"
    elif score <= 60:
        return "MEDIUM"
    elif score <= 80:
        return "HIGH"
    else:
        return "CRITICAL"


