`timescale 1ns / 1ps

`define AND 4'b0000 // logic and
`define OR  4'b0001 // logic or
`define ADD 4'b0011 // signed addition
`define XOR 4'b0100 // logic xor
`define SLL 4'b0101 // logic left shift
`define SUB 4'b0110 // signed subtration
`define MUL 4'b0111 // signed multiplication
`define EQ  4'b1000 // signed equal to
`define NEQ 4'b1001 // signed not equal to
`define LT  4'b1011 // signed less than to
`define GEQ 4'b1100 // signed greater or equal to
`define SRL 4'b1101 // logic right shift
`define SRA 4'b1110 // signed arithmetic right shift
`define DIV 4'b1111 // signed integer division

(* DONT_TOUCH = "yes" *)
module alu #(
    parameter DATA_WIDTH = 32
)(
    // Inputs
    input [3:0] operation,
    input [DATA_WIDTH-1:0] A,
    input [DATA_WIDTH-1:0] B,

    // Output
    output reg [DATA_WIDTH-1:0] ALUResult
);
    always @(A or B or operation) begin
        case(operation)
            `AND: ALUResult <= A & B;
            `OR : ALUResult <= A | B;
            `ADD: ALUResult <= $signed(A) +  $signed(B);
            `XOR: ALUResult <= A ^ B;
            `SLL: ALUResult <= A << B;
            `SUB: ALUResult <= $signed(A) -  $signed(B);
            `MUL: ALUResult <= $signed(A) *  $signed(B);
            `EQ : ALUResult <= $signed(A) == $signed(B);
            `NEQ: ALUResult <= $signed(A) != $signed(B);
            `LT : ALUResult <= $signed(A) <  $signed(B);
            `GEQ: ALUResult <= $signed(A) >= $signed(B);
            `SRL: ALUResult <= A >> B;
            `SRA: ALUResult <= $signed(A) >>> B;
            `DIV: ALUResult <= $signed(A) /  $signed(B);
            default: ALUResult <= 0;
        endcase
    end
endmodule

