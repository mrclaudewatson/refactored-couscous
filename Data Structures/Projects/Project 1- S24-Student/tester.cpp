#include <iostream>
#include <cassert>
#include "linked_calc.cpp" // Include the implementation file
using namespace std;
void runEvaluateExpressionTests() {
    // Test 1: Simple addition
    LinkedCalc<char> calc1;
    calc1.insert('1');
    calc1.insert('+');
    calc1.insert('2');
    assert(calc1.validateExpression());
    assert(calc1.evaluateExpression() == 3.0f);
    cout<<"Test 1 passed"<<endl;

    // Test 2: Simple subtraction
    LinkedCalc<char> calc2;
    calc2.insert('5');
    calc2.insert('-');
    calc2.insert('2');
    assert(calc2.validateExpression());
    assert(calc2.evaluateExpression() == 3.0f);
    cout<<"Test 2 passed"<<endl;

    // Test 3: Simple multiplication
    LinkedCalc<char> calc3;
    calc3.insert('3');
    calc3.insert('*');
    calc3.insert('4');
    assert(calc3.validateExpression());
    assert(calc3.evaluateExpression() == 12.0f);
    cout<<"Test 3 passed"<<endl;

    // Test 4: Simple division
    LinkedCalc<char> calc4;
    calc4.insert('8');
    calc4.insert('/');
    calc4.insert('2');
    assert(calc4.validateExpression());
    assert(calc4.evaluateExpression() == 4.0f);
    cout<<"Test 4 passed"<<endl;

    // // Test 5: Simple division 2
    LinkedCalc<char> calc5;
    calc5.insert('5');
    calc5.insert('/');
    calc5.insert('2');
    assert(calc5.validateExpression());
    assert(calc5.evaluateExpression() == 2.5f);
    cout<<"Test 5 passed"<<endl;


    // Test 6: Expression with decimal numbers
    LinkedCalc<char> calc6;
    calc6.insert('1');
    calc6.insert('.');
    calc6.insert('5');
    calc6.insert('+');
    calc6.insert('2');
    calc6.insert('.');
    calc6.insert('5');
    assert(calc6.validateExpression());
    assert(calc6.evaluateExpression() == 4.0f);
     cout<<"Test 6 passed"<<endl;

        // Test 7: Expression with decimal numbers
    LinkedCalc<char> calc7;
    calc7.insert('1');
    calc7.insert('.');
    calc7.insert('5');
    calc7.insert('+');
    calc7.insert('1');
    calc7.insert('.');
    calc7.insert('5');
    assert(calc7.validateExpression());
    assert(calc7.evaluateExpression() == 3.0f);
     cout<<"Test 7 passed"<<endl;



    // Test 8: Invalid expression (consecutive operators)
    LinkedCalc<char> calc8;
    calc8.insert('3');
    calc8.insert('+');
    calc8.insert('*');
    calc8.insert('2');
    assert(!calc8.validateExpression());
    

   
    // Test 9: Invalid expression (consecutive decimals)
    LinkedCalc<char> calc9;
    calc9.insert('3');
    calc9.insert('.');
    calc9.insert('.');
    calc9.insert('2');
    assert(!calc9.validateExpression());
    

    // Test 10: Expression ending with an operator
    LinkedCalc<char> calc10;
    calc10.insert('3');
    calc10.insert('+');
    calc10.insert('5');
    calc10.insert('*');
    assert(!calc10.validateExpression());
    

    // //Bonus Tests to test for edge cases and proper mathematical validation and evaluation
    // //Written to confirm robustness of code for unexpected results written by Sebastien Ghent U05939898

    // //Create Test 11 Linked List
    //Linked list test 1
    // LinkedCalc<char> calc11;
    // calc11.insert('6');
    // calc11.insert('+');
    // calc11.insert('2');
    // calc11.insert('*');
    // calc11.insert('3');
    // assert(calc11.evaluateExpression() == 12.0f);
    // std::cout<<"Test 11 passed"<<std::endl;
    
    //Hard order of operations test
    // LinkedCalc<char> calc12;
    // calc12.insert('6');
    // calc12.insert('*');
    // calc12.insert('4');
    // calc12.insert('+');
    // calc12.insert('2');
    // calc12.insert('/');
    // calc12.insert('2');
    // assert(calc12.evaluateExpression() == 25.0f);
    // std::cout<<"Test 12 passed"<<std::endl;


    //Decimal multiplcation
    // LinkedCalc<char> calc13;
    // calc13.insert('1');
    // calc13.insert('.');
    // calc13.insert('2');
    // calc13.insert('*');
    // calc13.insert('3');
    // calc13.insert('.');
    // calc13.insert('3');
    // assert(calc13.evaluateExpression() == 3.96f);
    // std::cout<<"Test 13 passed"<<std::endl;
    
    // //Last Bonus test to do before "submission"
    // LinkedCalc<char> calc14;
    // calc14.insert('1');
    // calc14.insert('.');
    // calc14.insert('2');
    // calc14.insert('.');
    // calc14.insert('3');
    // calc14.insert('.');
    // calc14.insert('4');
    // calc14.insert('.');
    // calc14.insert('4');
    // assert(!calc14.validateExpression());
    // //assert(calc14.evaluateExpression() == 7.6f);
    // std::cout<<"Test 14 passed"<<std::endl;

    // //Last Bonus test to do before "submission"
    // LinkedCalc<char> calc15;
    // calc15.insert('1');
    // calc15.insert('2');
    // calc15.insert('*');
    // calc15.insert('3');
    // calc15.insert('4');
    // assert(calc15.validateExpression());
    // assert(calc15.evaluateExpression() == 408.0f);
    // std::cout<<"Test 15 passed"<<std::endl;
    
    // //Who gonna carry the boats test
    // LinkedCalc<char> calc16;
    // calc16.insert('1');
    // calc16.insert('2');
    // calc16.insert('*');
    // calc16.insert('3');
    // calc16.insert('4');
    // calc16.insert('/');
    // calc16.insert('2');
    // calc16.insert('0');
    // calc16.insert('-');
    // calc16.insert('4');
    // assert(calc16.validateExpression());
    // assert(calc16.evaluateExpression() == 16.4f);
    // std::cout<<"Test 16 passed"<<std::endl;

}

int main() {
    // Run evaluateExpression tests
    runEvaluateExpressionTests();

    // If all assertions pass
    std::cout << "All evaluateExpression tests passed!" << std::endl;

    return 0;
}
