/*
Name: Claude Watson
Description: To determine if the input is in order (alphabetically) or not
*/

#include <stdio.h>
#include <ctype.h>

//declare a function which will determine if the input is in order or not
int inOrder(char *input);

// intializing the main function with two parameters to access command line arguments
int main(int argc, char *argv[]) {

    //if argument ount is not equal to 2, the main function will print invalid input and terminate
    if (argc != 2) {
        printf("invalid input\n");
        return 0;
    }

    //calling the in order function and storing the value in result
    int result = inOrder(argv[1]);

    //depending on the result from the function, the program will print in order, not in order or invalid input
    if (result == 1) {
        printf("in order\n");
    } else if (result == 0) {
        printf("not in order\n");
    } else if (result == -1) {
        printf("invalid input\n");
    }

    return 0;
}

int inOrder(char *input) {

    //setting the second letter to lowercase
    char ch2 = tolower(*input);

    // loop that will iterate through each element
    while (*input) {

        //converts the first letter to lowercase and determines if it is an alphabetical character. if it is not, it returns -1
        char ch = tolower(*input);
        if (ch < 'a' || ch > 'z') {
            return -1;
        }

        //compares the value of the current variable to the previous variable. if it is not in order, it will return 0
        if (ch < ch2) {
            return 0;
        }

        //sets ch2 as the current character for later comparision
        ch2 = ch;
        input++;
    }

    //returns 1 if it is in order
    return 1; 
}
