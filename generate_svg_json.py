import pip,sys,os
import svgwrite
import validation
import extractionJSON,XJ_Convertor
import requests

if XJ_Convertor.fflag == 1 and XJ_Convertor.json == 1:
    myJsonData = extractionJSON.parseJSON(XJ_Convertor.fichierInput)
elif XJ_Convertor.hflag == 1 and XJ_Convertor.json == 1:
    response = requests.get(url = XJ_Convertor.url)
    myJsonData = response.json() 

#myJsonData = extractionJSON.parseJSON(XJ_Convertor.fichierInput)
# Recuperons la liste des entites, en appelant la fonction getEntites() dans extractionJSON
listEntites = extractionJSON.getEntites(myJsonData)

# Creation du contexte du fichier SVG
svg_document = svgwrite.Drawing(filename = XJ_Convertor.fichierOutput,
                                debug = True)
coordsEntiteList = []   # les coordonnees des entites

for i in range(len(listEntites)):
    listAttributs = []
    listAssocs = []
    # Recuperons les noms des attributs et stockons les dans listAttributs
    nbAttributs = len(myJsonData[i][listEntites[i]][0].keys())
    
    for key in myJsonData[i][listEntites[i]][0].keys():
        listAttributs.append(key)
        #print('\t\t' + key)

    if (i % 2 == 0 ): # Pour les entites sur la premiere colonne
        # Rectangle contenant l'ensemble des attributs de chacun des entites
        svg_document.add(svg_document.rect(insert = (40, i*(i+150) + 10),
                                           size = ("150px", "150px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "#B0C4DE"))
        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 10,
            "coordY": i*(i+150) + 10
        }
        coordsEntiteList.append(entityCoords)          
        # Rectangle contenant le nom de l'entite
        svg_document.add(svg_document.rect(insert = (40, i*(i+150) + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "#B0C4DE"))
        

        # Affichage du nom de l'entité
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
                fill="rgb(15, 15, 15)", #couleur de
                font_size='15px',
                font_weight="bold")
            )
    
    else: #Pour les entites sur la deuxieme colonne
        # Rectangle contenant l'ensemble des attributs de chacun des entites
        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "150px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "#B0C4DE"))

        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 400,
            "coordY": (i - 1)*150 + 10
        }
        coordsEntiteList.append(entityCoords)

        #Rectangle contenant le nom de l'entite
        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "#B0C4DE"))

        # Affichage du nom de l'entité
        svg_document.add(svg_document.text(listEntites[i],
            insert=(410, (i - 1)*150 + 30),
            stroke='none',
            fill="rgb(15, 15, 15)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichons l'ensemble des attributs de chacun des entites
        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(410, (i - 1)*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
svg_document.save()
print("-------------------------------------------------------------------------")
print("le fichier ",XJ_Convertor.fichierOutput," a ete bien generer" )
print("-------------------------------------------------------------------------")
