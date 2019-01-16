from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import json

"""
******************************************************************************************
                            VALIDATION DU FICHIER XML
******************************************************************************************
                                                                                         
        Un texte est un document XML bien formé s'il adhère à                        
        toutes les règles de syntaxe de base pour les documents XML.                          
        En d'autres termes, il a une déclaration XML correcte et                              
        un élément racine unique, toutes les balises sont correctement                        
        imbriquées, les attributs de balise sont cités, et ainsi de suite.                    
                                                                                                  
        On utilise l'API SAX avec un ContentHandler qui ne fait rien.                         
        En général, lorsque nous analysons un document XML avec SAX,                          
        nous utilisons une instance ContentHandler pour traiter le contenu du document.       
        Mais dans ce cas, nous voulons seulement savoir si le document répond aux             
        contraintes de syntaxe les plus fondamentales de XML;                                 
        par conséquent, il n'y a pas de traitement que nous devons faire, et                  
        le gestionnaire de do-Nothing suffit.                                                
                                                                                                  
La fonction parsefile analyse le document en entier et lève une exception en cas d'erreur et
la fonction validateXML imprime a l'ecran l'exception                                                                                           
*********************************************************************************************   
"""
def parsefile(filename):
    parser = make_parser(  )
    parser.setContentHandler(ContentHandler(  ))
    parser.parse(filename)

def validateXML(filename) :
    try:
        parsefile(filename)
        return True
    except Exception as erreur:
        print ("%s n\'est pas valide' %s" % (filename, erreur))
        return False
      
      
      
""" 
****************************************************************************************************
                            VALIDATION DU FICHIER JSON
****************************************************************************************************
    De meme que le XML, On va juste verifier si le document JSON adhère à                        
    toutes les règles de syntaxe de base pour les documents JSON.
    
    la fonction validateJSON analyse le document JSON en entier
*****************************************************************************************************
"""
def validateJSON(filenameJSON):
    try:
        file = open(filenameJSON)
        data = file.read()
        json.loads(data)
        return True
    except ValueError as erreur:
        print ("%s n\'est pas valide %s"%(filenameJSON ,erreur))
        return False

#a = validateJSON(sys.argv[1])
#print(a)
