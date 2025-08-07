`timescale 1ns / 1ps

`define R_TYPE 7'b0110011
`define I_LOAD 7'b0000011
`define I_JALR 7'b1100111
`define I_TYPE 7'b0010011
`define S_TYPE 7'b0100011
`define B_TYPE 7'b1100011
`define J_TYPE 7'b1101111

(* DONT_TOUCH = "yes" *)
module ImmGen #(
    DATA_WIDTH = 32
)(
    input [31:0] instruction,
    output reg [DATA_WIDTH-1:0] imm
);

        always begin
        case (instruction[6:0])
            `R_TYPE: imm <= 0;
            `I_LOAD: imm <= {{20{instruction[31]}}, instruction[31:20]};
            `I_JALR: imm <= {{20{instruction[31]}}, instruction[31:20]};
            `I_TYPE: imm <= {{20{instruction[31]}}, instruction[31:20]};
            `S_TYPE: imm <= {{20{instruction[31]}}, instruction[31:25], instruction[11:7]};
            `B_TYPE: imm <= {{19{instruction[31]}}, instruction[31:25], instruction[11:7], 0};
            `J_TYPE: imm <= {{11{instruction[31]}}, instruction[31:12], 0};
            default: imm <= 0;
        endcase
    end


endmodule
