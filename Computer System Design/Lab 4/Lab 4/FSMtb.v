`timescale 1ns / 1ps

module FSMtb;
    // Inputs
    reg clk;
    reg reset;
    reg quarter;
    reg dime;
    reg nickel;
    reg soda;
    reg diet;

    // Outputs
    wire GiveSoda;
    wire GiveDiet;

    // Instantiate the Unit Under Test (UUT)
    VendingMealy uut (
        .clk(clk),
        .reset(reset), 
        .quarter(quarter), 
        .dime(dime), 
        .nickel(nickel), 
        .soda(soda), 
        .diet(diet), 
        .GiveSoda(GiveSoda), 
        .GiveDiet(GiveDiet)
    );
    
    always #5 clk = ~clk;

    initial begin
        // initialize inputs
        clk = 0;
        reset = 1;
        quarter = 0;
        dime = 0;
        nickel = 0;
        soda = 0;
        diet = 0;

        #10 reset = 0;

        // Test 1: insert money normally then select soda normally
        #10 nickel = 1; 
		  #10 nickel = 0;
        #10 dime = 1;
		  #10 dime = 0;
        #10 quarter = 1;
		  #10 quarter = 0;
        #10 nickel = 1; 
		  #10 nickel = 0; // 45 cents
        #10 soda = 1;
		  #10 soda = 0; // Select soda

        #20 reset = 1;
		  #10 reset = 0;
		  #10;

        // Test 2: Diet is selected before enough money is input
        #10 diet = 1; 
		  #10 diet = 0;
        #10 dime = 1; 
		  #10 dime = 0;
        #10 quarter = 1; 
		  #10 quarter = 0; //45 cents
        #10 dime = 1; 
		  #10 dime = 0;// Should automatically dispense Diet

		  #20 reset = 1;
		  #10 reset = 0;
		  #10;
		  
		  // Test 3: 
        #10 quarter = 1; 
		  #10 quarter = 0;
        #10 quarter = 1; 
		  #10 quarter = 0; //50 cents
		  #10 soda = 1; 
		  #10 soda = 0;
		  
        #20 reset = 1;
		  #10 reset = 0;
		  #10;
		  
		  // Test 4
		  #10 quarter = 1; 
		  #10 quarter = 0;
        #10 nickel = 1; 
		  #10 nickel = 0;
		  #10 soda = 1;
		  #10 soda = 0;
		  #10 dime = 1;
		  #10 dime = 0;
		  #10 quarter = 1;
		  #10 quarter = 0; // should automatically dispense
		  
		  #20;
        $finish;
    end
endmodule