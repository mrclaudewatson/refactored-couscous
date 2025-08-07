//Name: Claude Watson
//Description: To Select the first letter of each word in a file to decrypt a code

#include <stdio.h>

void decode(char words[][101], int num_words, char *result) {
    int result_index = 0;

    //loop that extracts the first letter from each word
    for (int i = 0; i < num_words; i++) {
        if (words[i][0] != '\0') {
            result[result_index] = words[i][0];
            result_index++;
        }
    }
    result[result_index] = '\0';
}

int main() {

    //initalizing the variables
    char file_name[101];
    char words[1000][101];
    int num_words = 0;

    //prompting the user for the file name and storing the input
    printf("Enter the file name: ");
    fgets(file_name, 101, stdin);

    //removes the newline character from the input
    file_name[strcspn(file_name, "\n")] = '\0'; 

    //open the input file for reading.
    FILE *input_file = fopen(file_name, "r");

    //reads words from the file
    while (fscanf(input_file, "%100s", words[num_words]) == 1) {
        num_words++;
    }

    //closes the input file
    fclose(input_file);

    char result[1001];

    //calling the deocde function 
    decode(words, num_words, result);

    //create the output file with the "decoded_" prefix
    char output_name[101];
    snprintf(output_name, 101, "decoded_%s", file_name);

    //open the output file for writing.
    FILE *output_file = fopen(output_name, "w");

    //write the resulting message to the output file.
    fprintf(output_file, "%s", result);

    //close the output file.
    fclose(output_file);

    printf("Output file name: ", output_name);

    return 0;
}
