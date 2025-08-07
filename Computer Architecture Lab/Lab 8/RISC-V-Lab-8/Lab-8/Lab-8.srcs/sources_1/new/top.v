`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 01/13/2023 11:23:58 PM
// Design Name: 
// Module Name: top
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module top(
    input         CLK100MHZ,
    input         CPU_RESETN,
    output [15:0] LED,
    output [7:0]  SEG,
    output [7:0]  AN
);
    wire   clk;
    wire   rst;
    assign clk     = CLK100MHZ;
    assign rst     = ~CPU_RESETN;
    assign LED16_R = rst;

    riscv CPU(
        .clk(clk),
        .rst(rst)
    );

    
endmodule
