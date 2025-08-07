`timescale 1ns / 1ps

(* DONT_TOUCH = "yes" *)
module RegFile#(
    // Parameters
    parameter DATA_WIDTH   = 32, // number of bits in each register
    parameter ADDRESS_WIDTH = 5, // number of registers = 2^ADDRESS_WIDTH
    parameter NUM_REGS = 2**ADDRESS_WIDTH
)(
    // Inputs 
    input  clk, // clock
    input  rst, // synchronous reset; if it is asserted (rst=1), all registers are reseted to 0
    input  RegWrite,  // write enable signal from control unit
    input  [ADDRESS_WIDTH-1:0] rd_addr,  // address of the destination register
    input  [ADDRESS_WIDTH-1:0] rs1_addr, // first address to be read from
    input  [ADDRESS_WIDTH-1:0] rs2_addr, // second address to be read from
    input  [DATA_WIDTH-1:0] rd_data,     // data that supposed to be written into the register file

    // Outputs
    output [DATA_WIDTH-1:0] rs1_data, //content of reg_file[rs1_addr] is loaded into
    output [DATA_WIDTH-1:0] rs2_data  //content of reg_file[rs2_addr] is loaded into
);

    integer i;
    reg [DATA_WIDTH-1:0] reg_file [0:NUM_REGS-1];

    // init
    initial begin
        for (i = 0; i < NUM_REGS; i = i + 1)
            reg_file[i] <= 0; /* all reg will be set to 0 in parallel (at the same time) */
    end

    // synchronous write and reset
    always @(negedge clk) begin
        if(rst) begin // reset
            for (i = 0; i < NUM_REGS; i = i + 1)
                reg_file[i] <= 0; /* all reg will be set to 0 in parallel (at the same time) */
        end
        else if(RegWrite) // write
            reg_file[rd_addr] <= rd_data;

    end

    // asynchronous read
    assign rs1_data = reg_file[rs1_addr];
    assign rs2_data = reg_file[rs2_addr];


endmodule
