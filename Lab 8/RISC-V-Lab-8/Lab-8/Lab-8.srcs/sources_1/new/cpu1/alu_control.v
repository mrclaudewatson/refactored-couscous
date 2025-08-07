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
module ALUControl(
    //Inputs
    input [1:0] ALUOp, // 2-bits ALUop lines from ControlUnit
    input [6:0] funct7, // bits 31 to 25 of the instruction
    input [2:0] funct3, // bits 14 to 12 of the instruction
    input       opcode5, // bit 5 of the instruction (or opcode)

    //Output
    output reg [3:0] operation //operation selection for ALU
);

    always begin
        case (ALUOp)
            // Save, Load, Jumps
            2'b00: operation <= `ADD;
            // Branch
            2'b01: begin
                case (funct3)
                    3'b000:  operation <= `EQ;
                    3'b001:  operation <= `NEQ;
                    3'b100:  operation <= `LT;
                    3'b101:  operation <= `GEQ;
                    default: operation <= 0;
                endcase
            end
            // R-types and I-types
            2'b01: begin
                case (funct3)
                    3'b001: operation <= `SLL;
                    3'b101: operation <= `SRL;
                    3'b011: operation <= `SRA;
                    3'b110: operation <= `OR;
                    3'b111: operation <= `AND;
                    3'b000: begin
                        if(opcode5) begin
                            case (funct7)
                                7'b0000000: operation <= `ADD;
                                7'b0100000: operation <= `SUB;
                                7'b0000001: operation <= `MUL;
                                default: operation <= 0;
                            endcase
                        end
                        else operation <= `ADD;
                    end
                    3'b100: begin
                        if(opcode5) begin
                            case (funct7)
                                7'b0000000: operation <= `XOR;
                                7'b0000001: operation <= `DIV;
                                default: operation <= 0;
                            endcase
                        end
                        else operation <= `XOR;
                    end

                    default: operation <= 0;
                endcase
            end
            default: begin
                operation <= 0;
            end
        endcase
    end
endmodule
