/*
Name: Claude Watson
Description: to split project 9 into two source files and one header file. 
*/

#include <stdio.h>
#include <ctype.h>
#include "read_line.h"

int read_line(char str[], int n) {
    int ch, i = 0;

    while (isspace(ch = getchar()))
        ;

    str[i++] = ch;
    while ((ch = getchar()) != '\n') {
        if (i < n)
            str[i++] = ch;
    }

    str[i] = '\0';

    return i;
}