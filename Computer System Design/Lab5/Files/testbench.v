`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:19:29 04/04/2025 
// Design Name: 
// Module Name:    testbench 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
`timescale 1ns / 1ps

module testbench;
    reg clk = 0, reset = 1, go_i = 0;
    reg [3:0] x_i, y_i;
    wire [3:0] d_o;
    wire done;

    // Instantiate top-level GCD module
    GCD_top uut (
        .clk(clk),
        .reset(reset),
        .go_i(go_i),
        .x_i(x_i),
        .y_i(y_i),
        .d_o(d_o),
        .done(done)
    );

    // Generate 5ns clock
    always #5 clk = ~clk;

    initial begin
	 
        // Initial reset
        #10 reset = 0;

        // test 1: GCD(12, 8) = 4
        x_i = 4'd12;
        y_i = 4'd8;
        go_i = 1; #10; go_i = 0;
        wait(done); #20;

        reset = 1; #10; reset = 0; // Reset for next case

        // Test Case 2: GCD(9, 6) = 3
        x_i = 4'd9;
        y_i = 4'd6;
        go_i = 1; #10; go_i = 0;
        wait(done); #20;

        reset = 1; #10; reset = 0;

        // Test Case 3: GCD(15, 15) = 15
        x_i = 4'd15;
        y_i = 4'd15;
        go_i = 1; #10; go_i = 0;
        wait(done); #20;

        reset = 1; #10; reset = 0;

        // Test Case 4: GCD(7, 3) = 1
        x_i = 4'd7;
        y_i = 4'd3;
        go_i = 1; #10; go_i = 0;
        wait(done); #20;

        $finish;
    end
endmodule


