/*
Name: Claude Watson
Description: To compare two arrays and print the unique elements
*/

#include <stdio.h>

void exclusive_or(int *a, int n1,  int *b, int n2, int *c, int *size);

int main(){

    // initialize the variables
    int n1, n2;

    //prompting the user the enter the size of the array and storing it in the previously assigned variables
    printf("Enter the of array #1: ");
    scanf("%d", &n1);

    //initialize an array with the size prompted by the user
    int array1[n1];

    //prompting the user to enter the elements of the array
    printf("Enter array elements: ");
    for(int i=0;i<n1;i++){
        scanf("%d", &array1[i]);
    }

    printf("Enter the of array #2: ");
    scanf("%d", &n2);

    int array2[n2];

    printf("Enter array elements: ");
    for(int i=0;i<n1;i++){
        scanf("%d", &array2[i]);
    }

    //initializing a third array to store the variables of the uncommon elements
    int array3[n1+n2];
    int size = 0;

    exclusive_or(array1, n1, array2, n2, array3, &size);

    //printing the contents of the third array (the uncommon elements)
    printf("Output: ");
    for(int i=0;i<size;i++){
        printf("%d", array3[i]);
    }

    return 0;
}

void exclusive_or(int *a, int n1,  int *b, int n2, int *c, int *size){

    //loop to compare the values of array a to array b
    for (int i=0;i<n1;i++) {

        //setting a variable (match) to 0 (false)
        int match = 0;

        for (int j = 0; j < n2; j++) {

            //if there are common elements in a and b, the match conidtion is changed to true and the loop is broken
            if (*(a + i) == *(b + j)) {
                match = 1;
                break;
            }
        }

        //if there are no matches, array c will be updated with that uncommon element
        if (match != 0) {
            *(c + *size) = *(a + i);
            (*size)++;
        }
    }

    for (int i = 0; i < n2; i++) {
        for (int j = 0; j < n1; j++) {

            //if a common element is found, the function will end
            if (*(b + i) == *(a + j)) {
                return;
            }
        }

        //adds the element to the c array if no common elements are found in the inner loop.
        *(c + *size) = *(a + i);
        (*size)++;
    }

}