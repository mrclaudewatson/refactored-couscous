`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:15:19 04/04/2025 
// Design Name: 
// Module Name:    datapath 
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
module datapath (
    input clk,
    input reset,
    input [3:0] x_i, y_i,
    input load_x, load_y,
    input sel_x, sel_y,
    output [3:0] d_o,
    output neq, lt
);
    wire [3:0] x_out, y_out;
    wire [3:0] x_sub_y, y_sub_x;
    wire [3:0] x_mux_out, y_mux_out;

    subtractor sub1 (.A(x_out), .B(y_out), .Y(x_sub_y));
    subtractor sub2 (.A(y_out), .B(x_out), .Y(y_sub_x));

    mux2 mux_x (.A(x_sub_y), .B(x_i), .sel(sel_x), .Y(x_mux_out));
    mux2 mux_y (.A(y_sub_x), .B(y_i), .sel(sel_y), .Y(y_mux_out));

    register reg_x (.clk(clk), .reset(reset), .enable(load_x), .D(x_mux_out), .Q(x_out));
    register reg_y (.clk(clk), .reset(reset), .enable(load_y), .D(y_mux_out), .Q(y_out));

    neq neq_cmp (.X(x_out), .Y(y_out), .x_neq_y(neq));
    less_than lt_cmp (.X(x_out), .Y(y_out), .x_lt_y(lt));

    assign d_o = x_out;
endmodule

