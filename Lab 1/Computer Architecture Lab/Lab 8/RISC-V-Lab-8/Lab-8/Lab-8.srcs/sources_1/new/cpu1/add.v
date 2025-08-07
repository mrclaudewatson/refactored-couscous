`timescale 1ns / 1ps

(* DONT_TOUCH = "yes" *)
module add2 #(
    parameter DATA_WIDTH = 32
)(
    input  [DATA_WIDTH-1:0] a,
    input  [DATA_WIDTH-1:0] b,
    output [DATA_WIDTH-1:0] sum
);

    assign sum = a + b;
endmodule
