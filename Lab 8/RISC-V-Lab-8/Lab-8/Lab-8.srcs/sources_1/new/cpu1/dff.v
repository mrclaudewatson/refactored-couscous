`timescale 1ns / 1ps

(* DONT_TOUCH = "yes" *)
module dff #(
    parameter DATA_WIDTH = 32
)(
    input clk,
    input rst,
    input [DATA_WIDTH-1:0] d,
    output reg [DATA_WIDTH-1:0] q
);

    always @(posedge clk) begin
        if (rst)
            q <= 0;
        else
            q <= d;
    end
endmodule
