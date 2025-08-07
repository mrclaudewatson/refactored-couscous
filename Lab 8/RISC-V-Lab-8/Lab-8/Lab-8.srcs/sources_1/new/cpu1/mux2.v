`timescale 1ns / 1ps

(* DONT_TOUCH = "yes" *)
module mux2 #(
    parameter DATA_WIDTH = 32
)(
    input  [DATA_WIDTH-1:0] din0,
    input  [DATA_WIDTH-1:0] din1,
    input  select,
    output [DATA_WIDTH-1:0] dout
);

    assign dout = select ? din1 : din0;
endmodule
