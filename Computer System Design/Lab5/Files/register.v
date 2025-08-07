`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:10:58 04/04/2025 
// Design Name: 
// Module Name:    register 
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
module register (
    input clk,
    input reset,
    input enable,
    input [3:0] D,
    output reg [3:0] Q
);
    always @(posedge clk or posedge reset) begin
        if (reset)
            Q <= 0;
        else if (enable)
            Q <= D;
    end
endmodule
