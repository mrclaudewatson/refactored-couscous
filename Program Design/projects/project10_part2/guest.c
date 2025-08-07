/*
Name: Claude Watson
Description: to split project 9 into two source files and one header file. 
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "guest.h"

#define NAME_LEN 30
#define PHONE_LEN 20

struct guest *add_guest(struct guest *list) { // function to add a new guest to the linked list
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

void remove_guest(struct guest **list) {
    char phone[PHONE_LEN + 1];
    char last[NAME_LEN + 1];
    char first[NAME_LEN + 1];

    // prompts the user for the phone number
    printf("Enter phone number: ");
    read_line(phone, PHONE_LEN);

    // prompts the user for the last name
    printf("Enter guest's last name: ");
    read_line(last, NAME_LEN);

    // prompts the user for the first name
    printf("Enter guest's first name: ");
    read_line(first, NAME_LEN);

    // adds the new guest to the end of the list if the list is not empty
    struct guest *current = *list;
    struct guest *prev = NULL;

    // Loop through the list to find the guest to be removed
    while (current != NULL) {
        if (strcmp(current->phone, phone) == 0 &&
            strcmp(current->last, last) == 0 &&
            strcmp(current->first, first) == 0) {
            if (prev == NULL) {
                // if the guest is the first node, update the list pointer
                *list = current->next;
            } else {
                // bypass the current node in the list
                prev->next = current->next;
            }
            //free memory for the removed guest
            free(current);
            return;
        }
        // move prev to the current node
        prev = current;
        // move current to the next node
        current = current->next;
    }

    printf("Guest does not exist.\n");
}
