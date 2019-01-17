import xml.etree.cElementTree as ET 
import pip,sys
import svgwrite
import extractionXML
import XJ_Convertor

if XJ_Convertor.fflag == 1 and XJ_Convertor.xml == 1:
    fichierXML = XJ_Convertor.fichierInput
elif XJ_Convertor.hflag ==1 and XJ_Convertor.xml==1 :
    fichierXML = XJ_Convertor.fichierInput



lesEntites = extractionXML.getEntites(fichierXML)
relations  = extractionXML.getRelations(fichierXML)
if(XJ_Convertor.xml == 1 and XJ_Convertor.tflag == 1) :
    print("La liste des entites et leurs attributs : ")
    print(lesEntites)
    print("La liste des relations et leurs attributs :")
    print(relations)

listEntites = []


# Recuperation de la liste des entites
for entite in lesEntites:
    listEntites.append(entite)

# Creation du contexte du fichier SVG :  
svg_document = svgwrite.Drawing(filename = XJ_Convertor.fichierOutput,
                                debug = True)

entityCoordsList = []
for entite in lesEntites:
    listAttributs = []
    for key in lesEntites[entite]['attributs']:
        listAttributs.append(key)
#print(listAttributs)

entityCoordsList = []
for i in range(len(listEntites)):
    listAttributs = ['P1','P2']
    listAssocs = []

    # Recuperons les noms des attributs et stockons les dans listAttributs
    nbAttributs = len(lesEntites[listEntites[i]]['attributs'])

    if (i % 2 == 0): # Pour les entites sur la premiere colonne
        # Rectangle contenant l'ensemble des attributs de chacun des entites
        svg_document.add(svg_document.rect(insert = (40, i*(i+150) + 10),
                                           size = ("150px", "150px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))
        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 10,
            "coordY": i*(i+150) + 10
        }
        entityCoordsList.append(entityCoords)           
        # Rectangle contenant le nom de l'entite
        svg_document.add(svg_document.rect(insert = (40, i*(i+150) + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))


        # Affichage du nom de l'entite
        svg_document.add(svg_document.text(listEntites[i],
            insert=(44, i*(i+150) + 30),
            stroke='none',
            fill="rgb(42, 42, 42)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichons l'ensemble des attributs de chacun des entites
        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(44, i*(i+150) + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    else:
        # Creation du rectangle contenant les infos de l'entite
        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "150px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))

        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 400,
            "coordY": (i - 1)*150 + 10
        }
        entityCoordsList.append(entityCoords)

        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))


        svg_document.add(svg_document.text(listEntites[i],
            insert=(410, (i - 1)*150 + 30),
            stroke='none',
            fill="rgb(15, 15, 15)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(410, (i - 1)*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    i+=1
svg_document.save()

print("-------------------------------------------------------------------------")
print("le fichier ",XJ_Convertor.fichierOutput," a ete bien generer" )
print("-------------------------------------------------------------------------")
