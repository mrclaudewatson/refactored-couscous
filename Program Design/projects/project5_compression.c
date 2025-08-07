/*
Name: Claude Watson
Description: To encode a message entered by the user 
*/

#include <stdio.h>

//declare the compress function for future use
void compress(char *input, char *output);

int main() {

    //initializing a varible for the user's input and the output assuming it is less than 1000 characters 
    char message[1001];
    char secret[1001];

    //prompting the user for a message and storing it 
    printf("Enter message: ");
    scanf("%s", message);

    //calling the compress function
    compress(message, secret);

    printf("Output: %s\n", secret);

    return 0;
}

void compress(char *input, char *output) {

    //initializing a char variable with the value of the first character of the string
    char current = *input;
    int count = 1;
    char *output_message = output;

    //looping through the string, if the current character matches the next, the count is incremented
    for (input++; *input != '\0'; input++) {
        if (*input == current) {
            count++;
        } else {

            //if the count is two or less, the character is written to the output
            if (count <= 2) {
                for (int i = 0; i < count; i++) {
                    *output_message++ = current;
                }
            } else {

                //if the count is greater than 2, the count will be written as a character. then the character is written to the output 
                if (count > 2) {
                    *output_message++ = count + '0';
                }
                *output_message++ = current;
            }

            //updates the current character and resets the count
            current = *input;
            count = 1;
        }
    }

    //handles the last consecutive characters. if the last group has two or more characters, write the count as a character
    if (count <= 2) {
        for (int i = 0; i < count; i++) {
            *output_message++ = current;
        }
    } else {

        //if the count is greater than 2, the count will be written as a character. then the character is written to the output
        if (count > 2) {
            *output_message++ = count + '0';
        }
        *output_message++ = current;
    }

    //terminate the string output˜
    *output_message = '\0';
}
