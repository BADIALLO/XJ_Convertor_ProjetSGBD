import xml.etree.cElementTree as ET 
import pip,sys,json
import svgwrite
import extractionXML




lesEntites = extractionXML.getEntites(sys.argv[1])
relations  = extractionXML.getRelations(sys.argv[1])
listEntites = []
#
#<<<<<<< HEAD
# Recuperation de la liste des entites
for entite in lesEntites:
    listEntites.append(entite)
#print(listEntites)
#=======

# Initiation du fichier SVG
svg_document = svgwrite.Drawing(filename = 'test.svg',
                                debug = True)

entityCoordsList = []
for entite in lesEntites:
    listAttributs = []
    for key in lesEntites[entite]['attributs']:
        listAttributs.append(key)
print(listAttributs)
#=======
entityCoordsList = []
for i in range(len(listEntites)):
    listAttributs = ['P1','P2']
    listAssocs = []

    # Recuperation des noms des attributs que l'on enregistre dans la variable "listAttributs"
    nbAttributs = len(lesEntites[listEntites[i]]['attributs'])
    if (i % 2 == 0):
        # Creation du rectangle contenant les infos de l'entite
        svg_document.add(svg_document.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "130px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))
        entityCoords = {
            "nomEntite": listEntites[i],
            "coordX": 10,
            "coordY": i*150 + 10
        }
        entityCoordsList.append(entityCoords)  

        entityCoordsList.append(entityCoords)          

        svg_document.add(svg_document.rect(insert = (10, i*150 + 10),
                                           size = ("150px", "26px"),
                                           stroke_width = "1",
                                           stroke = "black",
                                           fill = "rgb(209, 250, 46)"))
          

        # Affichage du nom de l'entite
        svg_document.add(svg_document.text(listEntites[i],
            insert=(20, i*150 + 30),
            stroke='none',
            fill="rgb(42, 42, 42)",
            font_size='15px',
            font_weight="bold")
        )

        # Affichage de la liste des attributs
        for k in range(len(listAttributs)):
            svg_document.add(svg_document.text(listAttributs[k],
                insert=(20, i*150 + 40 + (k+1)*20),
                stroke='none',
                fill="rgb(15, 15, 15)",
                font_size='15px',
                font_weight="bold")
            )
    else:
        # Creation du rectangle contenant les infos de l'entite
        svg_document.add(svg_document.rect(insert = (400, (i - 1)*150 + 10),
                                           size = ("150px", "130px"),
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

