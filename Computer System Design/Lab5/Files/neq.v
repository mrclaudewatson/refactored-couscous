`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:12:40 04/04/2025 
// Design Name: 
// Module Name:    neq 
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
module neq (
    input [3:0] X, Y,
    output x_neq_y
);
    assign x_neq_y = (X != Y);
endmodule

