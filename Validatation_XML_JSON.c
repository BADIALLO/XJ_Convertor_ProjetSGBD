#include <libxml/parser.h>
#include "JSON_checker.h"


int validateJSON (FILE *filename) {
    char ch;
    JSON_checker jc = new_JSON_checker(20);
    while(1) {
        ch = fgetc(filename);
        
        if (feof(filename)) {
            break;
        }
        if (!JSON_checker_char(jc, ch)) {
            fprintf(stderr, "JSON_checker_char: syntax error\n");
            exit(1);
        }
    }
    if (!JSON_checker_done(jc)) {
        fprintf(stderr, "JSON_checker_end: syntax error\n");
        exit(1);
    }
}


/* *******************************************************
 *              VALIDATION DU FICHIER XML
 *********************************************************
 */

int validateXML(char *filename) {

    xmlDocPtr doc;    // definir le contexte
    xmlNodePtr racine;
    char *filexml = filename;
    // Ouverture du fichier XML
    doc = xmlParseFile(filexml);
    /*On essaie de parser le fichier XML */
    if (doc == NULL) {
        fprintf(stderr, "Document XML invalide\n");
        return EXIT_FAILURE;
    }

    racine = xmlDocGetRootElement(doc);

    if (racine == NULL) {
        fprintf(stderr, "Document XML vierge\n");
        xmlFreeDoc(doc);
        return EXIT_FAILURE;
    }

    // Libération de la mémoire
    xmlFreeDoc(doc);

    return EXIT_SUCCESS;
}
