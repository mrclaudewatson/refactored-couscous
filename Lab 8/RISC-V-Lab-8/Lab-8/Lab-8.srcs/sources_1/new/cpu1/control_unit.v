`timescale 1ns / 1ps

`define R_TYPE 7'b0110011
`define I_LOAD 7'b0000011
`define I_JALR 7'b1100111
`define I_TYPE 7'b0010011
`define S_TYPE 7'b0100011
`define B_TYPE 7'b1100011
`define J_TYPE 7'b1101111


(* DONT_TOUCH = "yes" *)
module ControlUnit(
    //Input
    input [6:0] opcode, // 7-bit opcode field from the instruction register (IR)

    //Outputs
    output reg ALUSrc, // The second ALU operand comes from: (0) Reg2 or (1) the sign-extended immediate
    output reg MemtoReg, // The value fed to the register Write data input comes from (0) ALU result or (1) data memory.
    output reg RegWrite, // The register on the Write register input is written with the value on the Write data input 
    output reg MemRead, // Data memory contents designated by the address input are put on the Read data output
    output reg MemWrite, // Data memory contents designated by the address input are replaced by the value on the Write data input.
    output reg Branch, // If the branch condition is met, then PC=PC+Imm
    output reg Jump, // If this is jal or jalr, then write register input PC+4.
    output reg Jalr, // If this is jalr, thus sets PC=Reg1+Imm
    output reg [1:0] ALUOp
);

    always begin
        case (opcode)
            `R_TYPE: begin
                ALUSrc   <= 1'b0;
                MemtoReg <= 1'b0;
                RegWrite <= 1'b1;
                MemRead  <= 1'b0;
                MemWrite <= 1'b0;
                Branch   <= 1'b0;
                Jump     <= 1'b0;
                Jalr     <= 1'b0;
                ALUOp    <= 2'b10; // 1010
            end
            `I_LOAD:  begin
                ALUSrc   <= 1'b1;
                MemtoReg <= 1'b1;
                RegWrite <= 1'b1;
                MemRead  <= 1'b1;
                MemWrite <= 1'b0;
                Branch   <= 1'b0;
                Jump     <= 1'b0;
                Jalr     <= 1'b0;
                ALUOp    <= 2'b00;
            end
            `I_JALR:  begin
                ALUSrc   <= 1'b1;
                MemtoReg <= 1'b0;
                RegWrite <= 1'b1;
                MemRead  <= 1'b0;
                MemWrite <= 1'b0;
                Branch   <= 1'b0;
                Jump     <= 1'b1;
                Jalr     <= 1'b1;
                ALUOp    <= 2'b10;
            end
            `I_TYPE:  begin
                ALUSrc   <= 1'b1;
                MemtoReg <= 1'b0;
                RegWrite <= 1'b1;
                MemRead  <= 1'b0;
                MemWrite <= 1'b0;
                Branch   <= 1'b0;
                Jump     <= 1'b0;
                Jalr     <= 1'b0;
                ALUOp    <= 2'b10;
            end
            `S_TYPE:  begin
                ALUSrc   <= 1'b1;
                MemtoReg <= 1'b0;
                RegWrite <= 1'b0;
                MemRead  <= 1'b0;
                MemWrite <= 1'b1;
                Branch   <= 1'b0;
                Jump     <= 1'b0;
                Jalr     <= 1'b0;
                ALUOp    <= 2'b00;
            end
            `B_TYPE:  begin
                ALUSrc   <= 1'b0;
                MemtoReg <= 1'b0;
                RegWrite <= 1'b0;
                MemRead  <= 1'b0;
                MemWrite <= 1'b0;
                Branch   <= 1'b1;
                Jump     <= 1'b0;
                Jalr     <= 1'b0;
                ALUOp    <= 2'b01;
            end
            `J_TYPE:  begin
                ALUSrc   <= 1'b0;
                MemtoReg <= 1'b0;
                RegWrite <= 1'b0;
                MemRead  <= 1'b0;
                MemWrite <= 1'b0;
                Branch   <= 1'b1;
                Jump     <= 1'b1;
                Jalr     <= 1'b0;
                ALUOp    <= 2'b00;
            end
            default: begin
                ALUSrc   <= 1'b0;
                MemtoReg <= 1'b0;
                RegWrite <= 1'b0;
                MemRead  <= 1'b0;
                MemWrite <= 1'b0;
                Branch   <= 1'b0;
                Jump     <= 1'b0;
                Jalr     <= 1'b0;
                ALUOp    <= 2'b00;
            end
        endcase
    end
endmodule