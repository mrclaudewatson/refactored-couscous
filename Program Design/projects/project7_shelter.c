//Name: Claude Watson
//Description: To search a text file and return the mathcing values inputted by the user

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//declaring the structure and its members
    struct Animal{
        char name[100];
        char species[100];
        char gender[100];
        int age;
        double weight;
    }; 

int main(){

    //creates an array of size 200 that will store the animal data
    struct Animal animals[200];

    //setting the number of animals to 0, in order to keep count later in the program
    int numAnimals = 0;

    //opening the input file for reading
    FILE *fileInput = fopen("animals.txt", "r");

    //reads the animal data from the input file
    while(fscanf(fileInput, "%s %s %s %d %lf", animals[numAnimals].name, animals[numAnimals].species, animals[numAnimals].gender, &animals[numAnimals].age, &animals[numAnimals].weight)==5){
        numAnimals++;
    }

    //closing the input file
    fclose(fileInput);

    //initlaizing species and gender arrays to store the user input. Then prompting the user to enter these values
    char species[100];
    char gender[100];

    printf("Enter species: ");
    scanf("%s", species);
    printf("Enter gender: ");
    scanf("%s", gender);

    //creates the file that will contain the results
    FILE *fileOutput = fopen("results.txt", "w");

    //loop that iterates through the input file and compares it with the input of the user. if there is a match, the result is added to the new file
    for(int i=0;i<numAnimals;i++){
        if(strcmp(animals[i].species, species)==0 && strcmp(animals[i].gender, gender)==0){
         fprintf(fileOutput, "%s %d %.2lf\n", animals[i].name, animals[i].age, animals[i].weight);
        }
    }

    //closes the file
    fclose(fileOutput);

    printf("Output file name: results.txt");



    return 0;
}
