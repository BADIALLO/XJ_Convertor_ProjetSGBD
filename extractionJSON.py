import json,os,sys
def parseJSON(filePath):
    file = open(filePath)
    data = file.read()
    j = json.loads(data)
    return j

listEntites = []

# Recuperation de la liste des entités
def getEntites(data) :
    for i in range(len(data)) :
        keys = data[i].keys()
        key = next(iter(keys))
        listEntites.append(key)
    return listEntites
#print("La liste des entites et leurs attributs : ")

for i in range(len(listEntites)):
    listAttributs = []
    listAssocs = []
    #print('\t' + listEntites[i])
    # Recuperons les nom des attributs et on les stockes dans listAttributs
    nbAttributs = len(data[i][listEntites[i]][0].keys())
    
    for key in data[i][listEntites[i]][0].keys():
        listAttributs.append(key)
        #print('\t\t' + key)

