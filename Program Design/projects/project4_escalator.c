/*
Name: Claude Watson
Description: To calculate the total time that an elevator is active. 
*/

#include <stdio.h>

int active_seconds(int *arrival, int n);

int main(){
    
    int people;

    //prompting the user for the amount of people and storing the input.
    printf("Enter number of people: ");
    scanf("%d", &people);

    //initializing an array with the size of the number of people.
    int arrival[people];
    
    //prompting the user to input the arrival times and storing the input in the array.
    printf("Enter arrival times: ");
    for(int i=0;i<people;i++){
        scanf("%d", &arrival[i]);
    }

    //initializng a varible that calls the function that determines the amount of active seconds.
    int time = active_seconds(arrival,people);

    printf("Active seconds: %d\n", time);

    return 0;
}

//function that calculates the active time.
int active_seconds(int *arrival, int n){

    //initializing the total seconds to 10 since one trip will take 10 seconds.
    int seconds = 10;
    
    // initalizing a pointer to the first value of the array
    int *current = arrival;

    //for loop to iterate between each value in the array.
    for(int i=0;i<n-1;i++){

        /*
        comparing the values in the array. if the difference between the two values are greater than 10, 
        10 seconds are added to the seconds. however if the differnce is less than 10, the difference is 
        added to the seconds.
        */
        int difference = *(current + 1) - *current;

        if(difference > 10){
            seconds += 10;
        }
        else{
            seconds += difference;
        }

        // increments current to the next value of the array
        current++;

    }
    return seconds;
}