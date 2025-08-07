`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    14:16:14 04/04/2025 
// Design Name: 
// Module Name:    controlpath 
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
module controlpath (
    input clk,
    input reset,
    input go_i,
    input neq, lt,
    output reg load_x, load_y,
    output reg sel_x, sel_y,
    output reg done
);

    localparam IDLE = 0, LOAD = 1, CHECK = 2, SUB_Y = 3, SUB_X = 4, DONE = 5;
    reg [2:0] state, next;

    always @(posedge clk or posedge reset) begin
        if (reset)
            state <= IDLE;
        else
            state <= next;
    end

    always @(*) begin
        case(state)
            IDLE:   next = (go_i) ? LOAD : IDLE;
            LOAD:   next = CHECK;
            CHECK:  next = (neq ? (lt ? SUB_Y : SUB_X) : DONE);
            SUB_Y:  next = CHECK;
            SUB_X:  next = CHECK;
            DONE:   next = DONE;
            default: next = IDLE;
        endcase
    end

    always @(*) begin
        load_x = 0; load_y = 0;
        sel_x = 0;  sel_y = 0;
        done = 0;
        case(state)
            LOAD: begin
                load_x = 1; sel_x = 1;
                load_y = 1; sel_y = 1;
            end
            SUB_Y: begin
                load_y = 1; sel_y = 0;
            end
            SUB_X: begin
                load_x = 1; sel_x = 0;
            end
            DONE: begin
                done = 1;
            end
        endcase
    end
endmodule

