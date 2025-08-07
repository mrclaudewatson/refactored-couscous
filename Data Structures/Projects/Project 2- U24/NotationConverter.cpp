#include "NotationConverter.hpp"
#include <iostream>
#include <string>
/*Sebastien Ghent U05939898 and Claude Watson U72087839 Project 2 Notation Convertion utilizing a Deque*/

//Brief Overview Description of Code:

/*Program utilizes a defined deque template build utilizng nodes from a doubly linked list to indicate the pointers to the node after and before.
The NotationConverter utilizes infix to prefix and postfix notation, prefix to infix and postfix notation, and finally postfix to infix and prefix notation.
Functions which were written first were infix to prefix , postfix to infix and prefix to postfix each of which utilize the deque as a stack to perform conversion calculations to obtain the needed prefix.
Functions such as infix to postfix , prefix to infix and postfix to prefix each utilize the functions written first to form intermediate expressions to then be converted into the needed notaiton.
Doing this allowed for 3 functions to be comprised of composite functions reducing complexitity and the need for difficult modification and maintainance of the code.*/

template <typename T> //Template for deque, utilized from class notes given by the professor in queue.cpp 
class Deque {
private:
    struct Node { //Node Struct to serve as elements in the deque
        T data; //Data held in the node
        Node* prev; //Previous Pointer for the node of the doubly linked list to be used
        Node* next; //The next pointer for the node for the doubly linked list
        Node(const T& value) : data(value), prev(NULL), next(NULL) {} //Node declaration
    }; 

    Node* head; //Node pointer for the head of the deque
    Node* tail; // Node pointer for the tail of the deque
    size_t size; //Size of the deque

public:
    Deque() : head(NULL), tail(NULL), size(0) {} //Deque constructor
 
    ~Deque() { //Deque Destructor
        clear();
    }

    bool empty() const { //Checks to see if the deque is empty
        return size == 0;
    }

    size_t getSize() const { //Returns the size of the deque
        return size;
    }

    void pushFront(const T& value) { //Pushes a node to the front of the Deqye
        Node* newNode = new Node(value); //Creates a new node 
        if (empty()) { //If the deque is empty 
            head = tail = newNode;// Set the new head and tail to be the newNode
        } else { //Otherwise 
            newNode->next = head; //Set the new node's next to point to the head of the node
            head->prev = newNode; //Set the head's previous value to be the new node
            head = newNode; //Set the head of the deque to the newNode
        }
        size++; //Incrament size of the deque
    }

    void pushBack(const T& value) { //Push a node to the back of the deque
        Node* newNode = new Node(value); //Make a new node pointer and set its value
        if (empty()) {
            head = tail = newNode; //If the deque is empty set the head to the newNode and as its tail
        } else { // Otherwise
            tail->next = newNode; // Set the tail's next to be the new node 
            newNode->prev = tail; //Set the new Node's previous value to the be the tail
            tail = newNode;//Set the tail of the deque as the newNode
        }
        size++; //Incrament deque size
    }

    void popFront() {
        if (empty()) { //If the list is empty
            std::cout << "Deque is empty. Cannot pop from front." << std::endl;
            return; //Throw error
        }
        Node* temp = head; //Otherwise make a temporary node pointer
        head = head->next;//Set the new head to be the next value
        if (head) //Once the deque is not empty then 
            head->prev = NULL; //Set the head's previous value to point to the nullpointer
        else//Else 
            tail = NULL; //set the tail to be empty
        delete temp; //Delete Temp
        size--; //Decrease size
    }

    void popBack() {
        if (empty()) { //If the deque is empty
            std::cout << "Deque is empty. Cannot pop from back." << std::endl;
            return;
        }
        Node* temp = tail; //Make temporary node pointer variable 
        tail = tail->prev; //Set the new tail to the previous node
        if (tail) //If tail is not null 
            tail->next = NULL; //Set the tails next to point to null
        else //Else
            head = NULL; //Set the head of the deque to null
        delete temp; //Delete temporary value
        size--; //Decrease size of Deque
    }

    T& front() const { //Return the front of the Deque's node data
        if (empty()) {
            std::cout << "Deque is empty. Cannot access front element." << std::endl;
            
        }
        return head->data;
    }

    T& back() const { //Return the back of the deque's node data
        if (empty()) { //Checks to see if the list is empty
            std::cout << "Deque is empty. Cannot access back element." << std::endl;
            
        }
        return tail->data; //Retrieves the tail node's data
    }

    void clear() { //Empty deque
        while (!empty()) { //While the deque is not empty
            popFront(); //Popfront
        }
    }
};

class NotationConverter : public NotationConverterInterface {
public:
    //helper function to determine if the input is an operator returns true if the character red is an operand
    bool isOperator(char c){
        return c == '+' || c == '-' || c == '*' || c == '/';
    }

    //helper function to determine the precedence and approach the input appropriately
    int precedence(char op){ //Higher precedence for multiplication and division
        if(op == '*' || op == '/')            
            return 2;
        if(op == '+' || op == '-')
            return 1;
        return 0;
    }

    //helper function to determine if the input is an operand
    bool isOperand(char c){ //Returns true if it is an operand
        return isalnum(c);
    }

    std::string postfixToInfix(std::string inStr) override {
        Deque<std::string> Infix; //Declaration of a Deque to act like a stack as we sort the string only pushing variables or set terms to the back of the deque so that it would act as a stack
        for (char c : inStr){ // Stores the current character c of the iterator pointer , that points to each letter in the string 
            if (isOperand(c)) { // If the current value is an operand 
                Infix.pushFront(std::string(1, c)); // Push 1 instance of the character to the front of the stack
            } else if (isOperator(c)) { //Else if the character is an operator 
                std::string op2 = Infix.front(); Infix.popFront();// Stores the top of the "stack", or end of the deque in the op2 used as the right operand then pops that element, utilized for both individual variables or elements that have that have already underwent conversion to an infix notation and were pushed to the top of the stack
                std::string op1 = Infix.front(); Infix.popFront();//Store the next top of the "Stack" or end of the deque as the first operand and then pop the element
                Infix.pushFront("(" + op1 + " " + c + " " + op2 + ")"); //Since c is at this point assumed to be an operand , op1 is to the left of the operand c followed by op2 which is then pushed to the top of the stack
            } else continue; //If c is neither an operand or an operator then assume it to be a white space and iterate over
        }

        return Infix.back(); //Return the back of the stack which would be the only element/node remaining in the stack/deque
    }

    std::string postfixToPrefix(std::string inStr) override {
        std::string post_to_infix = postfixToInfix(inStr); // Convert postfix to infix
        std::string infix_to_prefix = infixToPrefix(post_to_infix); // Convert Infix to prefix
        return infix_to_prefix; // Return infix to prefix
    }

    std::string infixToPostfix(std::string inStr) override {
        std::string prefix = infixToPrefix(inStr);  // Convert infix to prefix first
        std::string postfix = prefixToPostfix(prefix);  // Now convert prefix to postfix
        return postfix; //Returns postfix notation 
    }

    std::string infixToPrefix(std::string inStr) override {
       Deque<char> operators;                           //creating two new deques, one to hold the operators and one to hold the output
       Deque<std::string> output;

       for(char &c : inStr){                            // loop that will check each character of the input
        if(isspace(c)){                                 // condition to check if the current input in a space. If so then the program continues
            continue;
        }
        else if(isOperand(c)){                          // condition that will check if the input is an operand, if it is then the operand is pushed to the output deque
            output.pushBack(std::string(1,c));          
        }
        else if(c == '('){                              // condition that will check if the input is an open parenthesis, if it is then it is pushed to the operators deque
            operators.pushBack(c);
        }
        else if (c == ')') {                            // condition that will check if the input is an open parenthesis
            while (!operators.empty() && operators.back() != '(') { // loop that pops operators from the output deque and stores into op, op1 and op2 until a ')' is encuontered
                std::string op; //Definition of Operator / Operators                                     
                op += operators.back(); //Add operator to at the top of the stack
                operators.popBack(); //Pop the operator
                std::string op2 = output.back(); // Get Right most operand
                output.popBack(); //Pop Operand
                std::string op1 = output.back(); // Get the left most operand
                output.popBack(); //Pop the top of the stack
                output.pushBack(op + " " + op1 + " " + op2); // combines the operators and the operands
            }
            operators.popBack(); // pops the '(' from the deque
        }
        else if (isOperator(c)) { // condition to check if the input is an operator
            while (!operators.empty() && precedence(operators.back()) >= precedence(c)) { // loop to pop the operators from the deque to the output deque based off of precedence
                std::string op; //Same steps as the first while loop
                op += operators.back(); //Store then Pop the operator
                operators.popBack(); 
                std::string op2 = output.back(); //Store the right most operand and pop
                output.popBack();
                std::string op1 = output.back(); //Store the left most operand and pop
                output.popBack(); 
                output.pushBack(op + " " + op1 + " " + op2); // combines the operators and operands
            }
            operators.pushBack(c);//Push the combined result to the top of the stack
        }
       }
       while(!operators.empty()){ // loop that pops the remaining operators from the deque into the output deque as long as the operator deque isnt empty
        std::string op; //Store the operator
        op += operators.back(); //Add and then pop the operator
        operators.popBack();
        std::string op2 = output.back(); //Add the right most operand 
        output.popBack(); //Pop the top of the stack
        std::string op1 = output.back(); //Add the left most operand 
        output.popBack(); // Pop the left most operand
        output.pushBack(op + " " + op1 + " " + op2); // combines the operators and operands in prefix notation
       }
       return output.back(); //Return resultant prefix
       }

    std::string prefixToInfix(std::string inStr) override {
        std::string postfix = prefixToPostfix(inStr); //convert from prefix to postfix 
        std::string infix = postfixToInfix(postfix); //Converts from postfix to infix
        return infix; //Returns infix
}

    std::string prefixToPostfix(std::string inStr) override {
        Deque<std::string> Postfix;  // Using Deque as a stack
        // Process from right to left
        for (auto it = inStr.rbegin(); it != inStr.rend(); ++it) { //Declares iterator to iterate through each character in string from start to finish
            char c = *it; //Stores value of iterator into c

            if (isOperand(c)) { //Checks if the character value is an operand 
                Postfix.pushFront(std::string(1, c));  // Push operand to the stack
            } else if (isOperator(c)) { //Else if the c is an operator,
                // Since it's prefix, we pop two items for each operator. The first item would be read from the top of the stack , serving as the left most operand and the second operand is utilized 
                std::string op1 = Postfix.front(); Postfix.popFront(); //Store the first operand variable in the stack and pop
                std::string op2 = Postfix.front(); Postfix.popFront(); // Store the second operand variable from the stack and pop
                Postfix.pushFront(op1 + " " + op2 + " " + c);// Create new expression in postfix order and push back to the stack
            } else{
                continue; //else if the character is neither continue
            }
        }

        // The final item in the stack is the complete postfix expression
        
        return Postfix.back(); //Return back of the stack
    }


};
