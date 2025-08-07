#include "linked_calc.hpp"

/*COP 4530 Data Structures*/
/*Professor: Doctor Taseef Rahman */
/*Teaching Assistants: Mohammad Ratul Mahjabin and Animesh Nighojkar */

/*COP 4530 Data Structures Project 1 Linked List Calculation done by Sebastien Ghent U05939898, Claude Watson U72087839*/

/*The linked_list_calc.cpp file features a template class for constructing and manipulating a 
linked list that represents and evaluates arithmetic expressions. The constructor initializes 
the list, while the destructor manages cleanup to prevent memory leaks. The insert() method 
adds nodes to the end of the list, handling both empty and non-empty lists efficiently.
The isDigit() function checks for numeric digits, which is essential for parsing numbers. 
convertToFloat() transforms sequences of nodes into floating-point numbers, critical for 
interpreting numeric calculations. The applyOp() method executes arithmetic operations in 
the correct order of precedence. validateExpression() ensures the list's structure complies 
with arithmetic rules, checking for errors like consecutive operators or misplaced decimals. 
evaluateExpression() parses numbers and applies operations, prioritizing multiplication and 
division before addition and subtraction, and ultimately returns the final calculated value 
as a floating-point number. This comprehensive implementation demonstrates the practical 
application of linked lists for complex data management and highlights C++'s capabilities in 
problem-solving and dynamic memory management.*/

// Default constructor definition
template <typename T>
LinkedCalc<T>::LinkedCalc() : head(NULL) {}

// Destructor to deallocate memory
template <typename T>
LinkedCalc<T>::~LinkedCalc() {
    Node<T>* current = head; //Set the current pointer to be the first node
    Node<T>* nextNode;//Create an instance of the next node
    while (current != NULL){ //While the current pointer is not nothing 
        nextNode = current->next; //Set the next node as the node infront of the current node
        delete current; //Delete the current node
        current = nextNode; //Set the current code to the next code
    }

}

// Function to insert a new node at the end of the linked list
template <typename T>
void LinkedCalc<T>::insert(const T& value) {
    Node<T>* newNode = new Node<T>(value); //Declare a new node
    if (head == NULL) { //If the list is empty make the new node the head of the list
        head = newNode;
    } else {
        Node<T>* current = head; // Otherwise if the list has elements make a current node pointer and have it point to the head
        while (current->next != NULL) { //While the next node in the list is not at the end
            current = current->next; //Move pointer
        }
        current->next = newNode; //Set pointer current next to new node
    }
}
// Helper function to determine if a character is a digit
template <typename T>
bool LinkedCalc<T>::isDigit(const T& c) { //Helper function to check whether or not a character is a digit
    return (c >= '0' && c <= '9') ;
}
//Helper function to convert number to floating point number
template <typename T>
float LinkedCalc<T>::convertToFloat(Node<T>*& current) {
    if (!current) return 0.0; // Handle empty input edge case

    Node<T>* next = current;  // Start processing from the current node, will indicate where to move the current pointer after storing the whole floating point number
    float num = 0.0;          // Stores the resultant number
    float decimal_factor = 1.0; // Factor for decimal digits
    bool Dec = false;   // Indicates if a decimal point has been encountered

    // Continue while there are digits or a decimal point
    while (next != NULL && (isdigit(next->data) || next->data == '.')) { //Iterate while next is not empty, and when the next node has a digit or a decimal point
        if (next->data == '.') { //If the next node contains a decimal point
            Dec = true; // Set flag for decimal numbers
            decimal_factor = 0.1; // Start multiplying by 0.1 for decimal places
        } else if (isdigit(next->data)) { //If the next node is a digit
            if (Dec) { //If the decimal flag has been marked
                num += (next->data - '0') * decimal_factor; // Append the decimal part by converting it from a character to an integer and multiplying by 0.1
                decimal_factor *= 0.1; // Move to the next decimal place to the next significant position for every time a digit is marked to have continuous decimal places
            } else { //Add number to left side of whole number through incramentations of 10, starts at 10*0
                num = num * 10 + (next->data - '0'); // Build the integer part by adding the current number multiplied by 10 and adding the decimal value of the character read
            }
        }
        next = next->next; // Move to the next node
    }

    current = next; // Update the 'current' pointer to point to the node following the last processed node (likely an operator or NULL)
    return num; // Return the parsed number
}
//Helper function to apply operations
template <typename T>
void LinkedCalc<T>::applyOp(float &result,float cur_num,char op){
    switch(op){
        case '+': result += cur_num; break; //Adds the result to the current number (float or integer but represented as a floating point number) through modification of the address where result is stored
        case '-': result -= cur_num; break;//Subtracts
        case '*': result *= cur_num; break;//Multiplies 
        case '/': result /= cur_num; break; //Divides 
    }
}

//Validate Expression function used to confirm that linked list follows the rules of arithmetic 
//Checks for special cases of invalid input, looks to ensure that consecuative operands/decimals are not present and that the end list does not end with either an operand or just a decimal place
template <typename T> //Declaration that this function will be part of the template to validate the method of the linked list when creating an instance of the object
bool LinkedCalc<T>::validateExpression() {
    if (!head) return false;  // Return false if list is empty

    Node<T>* cur = head;//Set the current pointer to point to the head of the list
    bool prevOp = false; // Previous character was an operator
    bool prevDec = false; // Previous character was a decimal

    while(cur) { // Traverse through the linked list
        char value = cur->data; //value is equal to the value of the node that cur points to 

        // Check for digits
        if(isDigit(value)) {//If a digit is read
            // Check for illegal consecutive decimals proceding one place after a number followed a decimal
            if (prevDec && cur->next && cur->next->data == '.') {//If a decimal point came before the digit and the data read in the next node is another decimal that is invalid arithmetic
                return false;
            }
            prevDec = false; //If the edge case condition does not occur and an operator or another number follows instead then reset flag to false
            prevOp = false; //Resets previous operator flag to false
        } else if (value == '.') { //If the value read is a decimal point
            // Check to see if a decimal follows an operator or another decimal.
            if (prevOp || prevDec) { //If the decimal point follows the operator or decimal 
                return false;
            }
            prevDec = true; //Otherwise mark that a previous decimal was spotted
        } else if (value == '+' || value == '*' || value == '/' || value == '-') { //Else is an operator is read
            // check to see whether the operator immediately following another operator or a decimal 
            if (prevOp || prevDec) { //If the operator follows another operator or decimal then it is false
                return false;
            }
            prevOp = true; //Otherwise mark that an operator was seen
        }

        cur = cur->next; // Move to the next node in the list
    }

    // Last character checks for trailing operators or decimals
    if (prevOp || prevDec) { //The current node pointer would be positioned at the last node in the linked list, therefore if an operator or decimal was seen in the last node then the mathematical expression is invalid
        return false;
    }

    return true; // If we pass all checks, expression is valid
}

//Evaluate Function Iterates through the linked list with a current pointer, the current pointer determines whether the current value is a digit,decimal or operator.
//If the current value is a digit, a helper function gets called to iterate through the rest of the linked list and stop when the pointer next reaches an operator.
//The current pointer is then updated to the position that the pointer next is in to retrieve full floating point number regardless of how big the number or precise leaving current at the next operation afterward
//Performs Multiplication then Division first
//Finishes with order of addition then Subtraction
//Assumes only that 0 is never to be assumed to be part of the divisor

template <typename T> //To be used as a public method for each linked list as part of the template
float LinkedCalc<T>::evaluateExpression() {
    Node<T>* current = head; //Declare a node pointer and set it equal to the start of the linked list
    float result = 0.0; //Result starts at 0 used to store the result of the linked list
    float cur_num = 0.0; //Cur num, used to track the number we are currently reading in set to 0 at first
    char lastOp = '+'; //Last operator read , default operation stored is addition

    while (current != NULL) { //While current pointer is not at the end of the list
        if (isdigit(current->data)) { //If the current node's data is a digit
            cur_num = convertToFloat(current);  // Converts the current sequence of digits/decimal to float
        }

        // We need to check if current is still valid after convertToFloat and if we've reached an operator or the end of the list
        if (current == NULL || current->data == '+' || current->data == '-' || current->data == '*' || current->data == '/') { //If the current pointer is at the end of the list or encounters an operator
            if (current != NULL && (current->data == '*' || current->data == '/')) {//Given that current is not at the end of the list and that the current data is either multiplication or division for order presecendce
                // Special handling for immediate operations (* and /)
                if (current->next != NULL && (isdigit(current->next->data))) { //If the next node is not equal to the end of the list and that the next node's data is a digit
                    float next_num = convertToFloat(current->next);  // Directly get the next number from the current position by calling convertToFloat to store the number
                    applyOp(cur_num, next_num, current->data);  // Apply * or / immediately to the current number using the current operation and next number
                }
            } else {
                // For + or -, we apply it to the result
                applyOp(result, cur_num, lastOp); //Using the helper function applyOp modify result 
                lastOp = current ? current->data : lastOp;  // Update lastOp to the current operator
                cur_num = 0.0;  // Reset cur_num for the next number
            }
        }

        // Only move to the next node if we are not at the end
        if (current != NULL) {// Once current is not equal to the end of the list
            current = current->next; //Iterate the current pointer
        }
    }

    // Apply the final operation 
    applyOp(result, cur_num, lastOp);
    return result; // Return floating point result
}




