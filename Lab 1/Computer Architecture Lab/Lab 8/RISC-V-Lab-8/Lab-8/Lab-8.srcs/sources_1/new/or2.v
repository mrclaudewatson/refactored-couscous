`timescale 1ns / 1ps

(* DONT_TOUCH = "yes" *)
module or2(
    input  a,
    input  b,
    output out
);

    assign out = a || b;
endmodule
