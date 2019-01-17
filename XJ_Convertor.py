import sys,os,getopt
import validation

def usage() :
    print("""\nUTILISATION : XJ_Convertor [-i xml/json] [-t ][-h url_FluxHTTP] [-f FichierInput] -o nomFichier.svg\n
    \t[-i xml/json] : permet de dire si l’input est en xml ou en json\n
    \t[-t] : permet de dire si on veut les traces (affichage sur écran de la liste des entités et des relations)\n
    \t[-h url_FluxHTTP] : permet de désigner un input en flux http\n
    \t[-f FichierInput] : permet de désigner un input de type fichier\n
    \t-o nomFichier.svg : permet de designer le fichier de sortie\n
    Exemple d’utilisation : XJ_Convertor -i xml -f monfichier.xml -o monfichier.svg\n""")

def exemple () : 
    print("Exemple d’utilisation : XJ_Convertor -i xml -f monfichier.xml -o monfichier.svg\n")

#if len(sys.argv) < 2 : 
#    usage()
#    sys.exit(2)

fichierInput  = ''      #variable pour stocker le nom du fichier en entree
fichierOutput = ''      #variable pour stocker le nom fichier en sortie
formatFich    = ''      #le format du fichier
""" Pour prendre en compte le format saisi l'utilisateur """
xml           = 0     
json          = 0

""" Variables pour compter le nombre de parametres renseignes par l'utilisateur """
iflag         = 0 
tflag         = 0 
hflag         = 0 
oflag         = 0
fflag         = 0

try:
    opts, args = getopt.getopt(sys.argv[1:], 'tf:h:i:o:')
except getopt.GetoptError:
    print("Verifier la syntaxe de la commande ! \n")
    exemple()
    sys.exit(2)

for opt, arg in opts:
    if opt == '-i':
        iflag = 1
        formatFich = arg
    elif opt =='-t':
        tflag = 1
    elif opt == '-h':
        hflag = 1
        params = arg
    elif opt == '-f' :
        fflag = 1
        fichierInput = arg
    elif opt == '-o' :
        oflag = 1
        fichierOutput = arg
    else:
        usage()
        sys.exit(2)

if (iflag == 1) :
    if (formatFich == 'xml' or formatFich == 'json') :
        if (formatFich == 'xml') :
            xml  = 1
            json = 0
        elif (formatFich == 'json') :
            json = 1
            xml  = 0
        if(fflag == 1 or hflag == 1) :
            if not(os.path.exists(fichierInput)):
                print("Verifier le nom du fichier ...!")
                sys.exit(2)
            else :
                if(oflag == 1) :
                    if(xml == 1) :
                        if(validation.validateXML(fichierInput)) :
                            import generate_svg_xml
                            if(tflag == 1) :
                                print("")
                                #print(extractionXML.getEntites(fichierInput))
                                
                    elif(json == 1) :
                        if (validation.validateJSON(fichierInput)) :
                            import generate_svg_json
                            if(tflag == 1) :
                                #print("La listes des entites et associations : \n")
                                f=1

                else :
                    print("Veuillez specifier l'option -o pour la generation du fichier de sortie svg\n")
                    exemple()
                    sys.exit(2)
        else :
            print("Veuillez specifier l'option -f pour un <fichier> ou l'option -h pour un <flux http> \n")
            exemple()
    else :
        print("L'option -i a pour argument <xml> ou <json> \n")
        exemple()

else :
    usage()
