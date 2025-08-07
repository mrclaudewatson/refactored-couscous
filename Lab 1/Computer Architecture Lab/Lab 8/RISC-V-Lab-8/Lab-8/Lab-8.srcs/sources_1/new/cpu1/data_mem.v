`timescale 1ns / 1ps

`define MEM_FILENAME "data.mem"

(* DONT_TOUCH = "yes" *)
module DataMem #(
    parameter DATA_WIDTH    = 32,  // number of bits in each memory cell
    parameter ADDRESS_WIDTH = 32, // number of memory cells <= 2^(ADDRESS_WIDTH-2)
    parameter NUM_MEM_CELLS = 64
)(
    input clk, // clk
    input rst, // reset
    input  [ADDRESS_WIDTH-1:0] addr, // Read/write address
    input MemRead, // read enable signal from control unit
    input MemWrite, // write enable signal from control unit
    input  [DATA_WIDTH-1:0] write_data, // Write Data
    output [DATA_WIDTH-1:0] read_data // Read Data
);


    reg [DATA_WIDTH-1:0] data_mem [0:NUM_MEM_CELLS-1];

    // init
    initial begin
        // $readmemb(`MEM_FILENAME, data_mem); /* if data is in binary */
        $readmemh(`MEM_FILENAME, data_mem); /* if data is in hex */
    end
    
    // synchronous write
    always @(negedge clk) begin
        if (rst) begin
            // $readmemb(`MEM_FILENAME, data_mem); /* if data is in binary */
            $readmemh(`MEM_FILENAME, data_mem); /* if data is in hex */
        end
        else if(MemWrite) // write
            data_mem[addr] <= write_data;
    end

    // asynchronous read
    assign read_data = (MemRead)? data_mem[addr] : 0;

endmodule
