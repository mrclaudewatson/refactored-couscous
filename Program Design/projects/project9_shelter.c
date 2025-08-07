// Name: Claude Watson
// Description: To search a text file and return the matching values inputted by the user using quicksort for sorting animals by species and age.

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// structure definition for Animal
struct Animal {
    char name[100];
    char species[100];
    char gender[100];
    int age;
    double weight;
};

// somparison function for qsort
int compare_animals(const void *a, const void *b) {
    struct Animal *animalA = (struct Animal *)a;
    struct Animal *animalB = (struct Animal *)b;

    // first comparing by species
    int speciesComparison = strcmp(animalA->species, animalB->species);
    if (speciesComparison != 0) {
        return speciesComparison;
    }

    // if species are the same, compare by age
    return animalA->age - animalB->age;
}

int main() {
    // array to store animal data
    struct Animal animals[200];
    int numAnimals = 0;
    FILE *fileInput = fopen("animals.txt", "r");

    // reading animal data from the input file
    while (fscanf(fileInput, "%s %s %s %d %lf", animals[numAnimals].name, animals[numAnimals].species, animals[numAnimals].gender, &animals[numAnimals].age, &animals[numAnimals].weight) == 5) {
        numAnimals++;
    }
    fclose(fileInput);

    // prompting the user for species and gender
    char species[100];
    char gender[100];

    printf("Enter species: ");
    scanf("%s", species);
    printf("Enter gender: ");
    scanf("%s", gender);

    // creating the output file
    FILE *fileOutput = fopen("results.txt", "w");

    // sorting the animals array using qsort
    qsort(animals, numAnimals, sizeof(struct Animal), compare_animals);

    int counter = 1;

    // writing the matching results to the output file
    for (int i = 0; i < numAnimals; i++) {
        if (strcmp(animals[i].species, species) == 0 && strcmp(animals[i].gender, gender) == 0) {
            fprintf(fileOutput, "%d %s %d %.2lf\n", counter, animals[i].name, animals[i].age, animals[i].weight);
            counter++;
        }
    }
    fclose(fileOutput);

    printf("Output file name: results.txt");
    return 0;
}
