import json,os,sys
def parseJSON(filePath):
    file = open(filePath)
    data = file.read()
    j = json.loads(data)
    return j


data = parseJSON(sys.argv[1])
 #print(data)

listEntites = []
# Recuperation de la liste des entités

for i in range(len(data)):
    keys = data[i].keys()
    key = next(iter(keys))
    listEntites.append(key)
  #  print(key)

for i in range(len(listEntites)):
    listAttributs = []
    listAssocs = []

   # print('\t' + listEntites[i])

    # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
    nbAttributs = len(data[i][listEntites[i]][0].keys())
    
    for key in data[i][listEntites[i]][0].keys():
        listAttributs.append(key)
    #    print('\t\t' + key)

