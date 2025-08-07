/*
Name: Claude Watson
Description: to split project 9 into two source files and one header file. 
*/

#include <stdio.h>
#include <stdlib.h>
#include "guest.h"
#include "read_line.h"

int main(void) {
    char code;
    struct guest *new_list = NULL;

    printf("Operation Code: a for adding to the list at the end, r for removing from the list, p for printing the list; q for quit.\n");

    for (;;) {
        printf("Enter operation code: ");
        scanf(" %c", &code);
        while (getchar() != '\n') /* skips to the end of the line */;
        switch (code) {
            case 'a':
                new_list = add_guest(new_list);
                break;
            case 'p':
                print_list(new_list);
                break;
            case 'r':
                remove_guest(&new_list);
                break;
            case 'q':
                clear_list(new_list);
                return 0;
            default:
                printf("Illegal code\n");
        }
        printf("\n");
    }
}