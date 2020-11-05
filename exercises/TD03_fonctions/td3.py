# temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return (((temps[0] * 24) + temps[1]) * 60 + temps[2]) * 60 + temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    temps = ()
    temps = list(temps)
    temps.insert(0, seconde // (3600 * 24))
    secondes_restantes = seconde % (3600 * 24)
    temps.insert(1, secondes_restantes // 3600)
    temps.insert(2, (secondes_restantes % 3600) // 60)
    temps.insert(3, (secondes_restantes % 3600) % 60)
    temps = tuple(temps)
    return temps
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

#fonction auxiliaire ici

def afficheTemps(temps):
    mots = ["jour","heure","minute","seconde"]  
    temps = list(temps) 
    for i in range(0,4):
        if temps[i] > 1:
            mots[i] += "s"
            print(temps[i], mots[i], '', end="")
        elif temps[i] == 0:
            print('', end="")
        elif temps[i] == 1:
            print(temps[i], mots[i], '', end="")
            

    
afficheTemps((1,0,14,23))    
