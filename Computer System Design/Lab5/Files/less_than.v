`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:14:58 04/04/2025 
// Design Name: 
// Module Name:    less_than 
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
module less_than (
    input [3:0] X, Y,
    output x_lt_y
);
    assign x_lt_y = (X < Y);
endmodule
