`timescale 1ns / 1ps

(* DONT_TOUCH = "yes" *)
module and2(
    input  a,
    input  b,
    output out
);

    assign out = a && b;
endmodule
