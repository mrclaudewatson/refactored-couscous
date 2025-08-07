`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:17:01 04/04/2025 
// Design Name: 
// Module Name:    GCD_top 
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
module GCD_top (
    input clk, reset, go_i,
    input [3:0] x_i, y_i,
    output [3:0] d_o,
    output done
);
    wire load_x, load_y, sel_x, sel_y, neq, lt;

    controlpath ctrl (
        .clk(clk), .reset(reset), .go_i(go_i),
        .neq(neq), .lt(lt),
        .load_x(load_x), .load_y(load_y),
        .sel_x(sel_x), .sel_y(sel_y),
        .done(done)
    );

    datapath dp (
        .clk(clk), .reset(reset),
        .x_i(x_i), .y_i(y_i),
        .load_x(load_x), .load_y(load_y),
        .sel_x(sel_x), .sel_y(sel_y),
        .d_o(d_o), .neq(neq), .lt(lt)
    );
endmodule

