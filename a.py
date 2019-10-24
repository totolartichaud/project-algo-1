from villes import villes

depart = input("Quelle est la ville de départ ? :")
arriver = input("Quelle est la ville d'arriver ? :")
etapes = input('Quelles sont les étapes (séparé par un espace)').split(' ')
distance = []
if etapes == ['']:
    distance.append(villes[depart.capitalize()][arriver.capitalize()])
else:
    distance = []
    distance.append(villes[depart.capitalize()][etapes[0].capitalize()])
    for i in range(1, len(etapes)):
        distance.append(villes[etapes[i-1].capitalize()][etapes[i].capitalize()])
    distance.append(villes[etapes[-1].capitalize()][arriver.capitalize()])

def calcul(distance):
    vitesse = 0
    heure = 0
    minute = 0
    distanceTotal = 0
    pause = False

    tempsDePause = 0

    while distanceTotal < distance:
        minute += 1
        if minute == 60:
            minute = 0
            heure += 1
        distanceTotal += vitesse / 60

        if heure % 2 == 1 and minute > 50:
            vitesse -= 10
        elif heure % 2 == 0 and minute == 0:
            pause = True 
        elif vitesse < 90:
            vitesse += 10
        
        if pause == True:
            tempsDePause += 15
            pause = False

    return heure, minute, tempsDePause

heureTotal = 0
minutesTotal = 0
pauseTotal = 0
tempsEtape = 0

for dist in distance:
    heure, minute, pause = calcul(dist)
    heureTotal += heure
    minutesTotal += minute
    pauseTotal += pause
    if minutesTotal >= 60:
        heureTotal += minutesTotal // 60
        minutesTotal = minutesTotal % 60

tempsEtape += 45 * (len(distance) - 1)

minutesTotal += pauseTotal + tempsEtape

if minutesTotal > 60:
    heureTotal += minutesTotal // 60
    minutesTotal = minutesTotal % 60


print(f'Distance total : {sum(distance)} km pour un temps de {heureTotal} heure et {minutesTotal} minutes')
print(f'Avec {pauseTotal // 15} pauses et {tempsEtape // 45} étapes')


