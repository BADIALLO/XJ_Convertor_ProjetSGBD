import xml.etree.cElementTree as ET 
import sys

"""
La fonction def getEntites nous permet de recuperer la liste des entites et attributs
puis les mettre dans un dictionnaire entites{}.

La fonction parcourt tous le doc et recuperer chacune des entites et ses attributs 
et les stockent dans un dictionnaire
"""

def getEntites(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()					# On recupere la racine du document XML
    entites = {}							# un dictionnaire pour contenir l'ensemble des entites
    for nodes in root.iter('entite') : 		# On parcours le doc en iterant d'une balise ('entite') [qui est un noeud] a une autre
        for child in nodes:					# On parcours les balises enfants 
            if child.tag == "proprietes":   # On verifie le nom de la balise enfant si c'est "proprietes" pour recuperer l'ensemble des attr 
                entites.update({nodes.attrib['nom']:{'attributs':{}}}) #inserer le nom de l'entite dans entites en initialisants ses attibuts a vide
                for attribut in child:
                    entites[nodes.attrib['nom']]['attributs'].update({attribut.attrib['nom']:attribut.attrib['type']}) #recupere l'ensemble de ses attributs
                   
    return entites


"""
La fonction def getRelations nous permet de recuperer la liste des relations et attributs
puis les mettre dans un dictionnaire relations{}.

La fonction parcourt tous le document et recuperer chacune des entites et ses attributs
et les stockent dans un dictionnaire

"""

def getRelations(fichier):
    files = ET.ElementTree(file = fichier)
    root = files.getroot()
    relations = {}
    for nodes in root.iter('relation') : 
        for child in nodes:
            if child.tag == "proprietes": # 
                relations.update({nodes.attrib['nom']:{'attributs':{}}}) #inserer le nom dans entites en initialisants ses attibuts a vide
                for attribut in child:
                    relations[nodes.attrib['nom']]['attributs'].update({attribut.attrib['nom']:(attribut.attrib['cardMin'],attribut.attrib['cardMax'])}) #recupere l'ensemble de ses attributs
                   
    return relations


#fin de la fonction


# a = getEntites(sys.argv[1])
# print(a)
# b=getRelations(sys.argv[1])
# print("\n")
# print(b)
