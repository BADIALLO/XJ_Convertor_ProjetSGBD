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