#ifndef LINKED_CALC_HPP
#define LINKED_CALC_HPP

#include <iostream>

// Node structure
template <typename T> //Template to be copied by other nodes
struct Node { //Struct for node
    T data; //Template for data of various data types to be stored
    Node* next;//Value which comes after the node

    Node(const T& data) : data(data), next(nullptr) {}
};

// LinkedCalc class
template <typename T>
class LinkedCalc {
public:
    LinkedCalc();//Constructor
    ~LinkedCalc();//Destructor
    void insert(const T& value);//Insert a new node
    bool validateExpression();//Validate the linked list expression; true if valid false if not
    float evaluateExpression();//Evaluate linked list expression return floating point number

private:
    Node<T>* head;
    bool isDigit(const T& c);//Professor and TA completed helper function
    float convertToFloat(Node<T>*& current);//Project members completed function
    void applyOp(float &result,float cur_num,char op);//Additional helper function that was not included in project zip
};



#endif // LINKED_CALC_HPP
