`timescale 1ns / 1ps

(* DONT_TOUCH = "yes" *)
module LeftShift #(
    parameter SHIFT = 1,
    parameter DATA_WIDTH = 32
)(
    input  [DATA_WIDTH-1:0] in,
    output [DATA_WIDTH-1:0] out
);

    assign sum = in << SHIFT;
endmodule
