/*
Name: Claude Watson
Description: Modify the function so that it tracks the guest list for a local restuarant.

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define NAME_LEN 30
#define PHONE_LEN 20

struct guest {
    char phone[PHONE_LEN + 1];
    char last[NAME_LEN + 1];
    char first[NAME_LEN + 1];
    int party_size;
    struct guest *next;
};

struct guest *add_guest(struct guest *list);
void print_list(struct guest *list);
void clear_list(struct guest *list);
int read_line(char str[], int n);

int main(void) {
    char code;
    struct guest *new_list = NULL;

    printf("Operation Code: a for adding to the list at the end, p for printing the list; q for quit.\n");

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
            case 'q':
                clear_list(new_list);
                return 0;
            default:
                printf("Illegal code\n");
        }
        printf("\n");
    }
}

struct guest *add_guest(struct guest *list) { // function to add a new guest o the linked list
    // variables to store user input
    char phone[PHONE_LEN + 1]; 
    char last[NAME_LEN + 1];
    char first[NAME_LEN + 1];
    int party_size;

    // allocating memory for the guest
    struct guest *new_guest = malloc(sizeof(struct guest));
    if (new_guest == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        exit(EXIT_FAILURE);
    }

    // prompting the user to enter the phone number
    printf("Enter phone number: ");
    read_line(phone, PHONE_LEN);

    // check if the guest already exists
    struct guest *current = list;
    while (current != NULL) {
        if (strcmp(current->phone, phone) == 0) {
            printf("guest already exists.");
            free(new_guest);
            return list;
        }
        current = current->next;
    }

    // copies the user input to the new guest 
    strcpy(new_guest->phone, phone);

    // prompting the user to enter the last name
    printf("Enter guest's last name: ");
    read_line(last, NAME_LEN);
    strcpy(new_guest->last, last);

    // prompting the user to enter the first name
    printf("Enter guest's first name: ");
    read_line(first, NAME_LEN);
    strcpy(new_guest->first, first);

    // prompting the user to enter the party size
    printf("Enter party size: ");
    scanf("%d", &party_size);
    new_guest->party_size = party_size;

    new_guest->next = NULL;

    // returns the new guest if the list is empty
    if (list == NULL) {
        return new_guest;
    }

    // adds the new guest to the end of the list if the list is not empty
    struct guest *current_guest = list;
    while (current_guest->next != NULL) {
        current_guest = current_guest->next;
    }
    current_guest->next = new_guest;

    return list;
}

void print_list(struct guest *list) {
    struct guest *current = list;
    // loop to iterate through the list and print the guest's information
    while (current != NULL) {
        printf("%-15s%-20s%-20s%5d\n", current->phone, current->last, current->first, current->party_size);
        current = current->next;
    }
}

void clear_list(struct guest *list) { // deallocates the memory for the list
    struct guest *current = list;
    // loop that iterates through the list to free memory for each guest
    while (current != NULL) {
        struct guest *temp = current;
        current = current->next;
        free(temp);
    }
}
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