/*
Name: Claude Watson
Description: to split project 9 into two source files and one header file. 
*/

#ifndef GUEST_H
#define GUEST_H

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
void remove_guest(struct guest **list);

#endif