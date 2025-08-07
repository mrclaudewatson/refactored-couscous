// RISC-V CPU
`timescale 1ns / 1ps

(* DONT_TOUCH = "yes" *)
module riscv #(
    parameter DATA_WIDTH = 32,
    parameter INST_ADDR_WIDTH = 32, // number of memory instructions = 2^(INST_ADDR_WIDTH-2)
    parameter DATA_ADDR_WIDTH = 32, // number of memory data cells   = 2^(DATA_ADDR_WIDTH-2)
    parameter REG_ADDR_WIDTH  = 5   // number of registers           = 2^(REG_ADDR_WIDTH-2)
)(
    input clk, // clk
    input rst // reset
);
    
    wire [31:0] instruction;
    wire [DATA_WIDTH-1:0] imm_left_shift, imm;
    wire [DATA_WIDTH-1:0] rd_data, rs1_data, rs2_data, ALU_a, ALU_b;
    wire [DATA_WIDTH-1:0] mem_data, wb_data;
    wire [DATA_WIDTH-1:0] pc, pc_next, pc4_or_branchtarget, pc4;
    wire [DATA_WIDTH-1:0] jalr_target, branch_target;
    wire [DATA_WIDTH-1:0] ALUResult;
    wire take_branch_jump, take_branch;
    wire ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, Jump, Jalr;
    wire [1:0] ALUOp;
    wire [3:0] operation;
        
    /////////////////////////
    //// Program Counter ////
    /////////////////////////
    dff #(DATA_WIDTH) PC_REG(
        .clk(clk),
        .rst(rst),
        .d(pc_next),
        .q(pc)
    );
    
    /////////////////////////
    //// Next PC control ////
    /////////////////////////
    /* PC + 4 */
    add2 #(DATA_WIDTH) ADD_PC4(
        .a(pc),
        .b('b100),
        .sum(pc4)
    );
    
    /* PC + imm */
    LeftShift #(1,DATA_WIDTH) LS_IMM(
        .in(imm),
        .out(imm_left_shift)
    );
    add2 #(DATA_WIDTH) ADD_BRANCH_TARGET(
        .a(pc),
        .b(imm_left_shift),
        .sum(branch_target)
    );
    
    /* take branch/jump? */
    and2 AND_BRANCH(
        .a(Branch),
        .b(ALUResult[0]),
        .out(take_branch)
    );
    or2 OR_BRANCH_JUMP(
        .a(take_branch),
        .b(Jump),
        .out(take_branch_jump)
    );
    
    /* PC+4 or PC+imm */
    mux2 #(DATA_WIDTH) MUX_BRANCH(
        .din0(pc4),
        .din1(branch_target),
        .select(take_branch_jump),
        .dout(pc4_or_branchtarget)
    );
    
    /* [PC+4 or PC+imm] or rs1+imm */
    mux2 #(DATA_WIDTH) MUX_JALR(
        .din0(pc4_or_branchtarget),
        .din1(wb_data),
        .select(Jalr),
        .dout(pc_next)
    );
    
    ///////////////////////////
    //// Intruction Memory ////
    ///////////////////////////
    InstMem #(DATA_WIDTH, INST_ADDR_WIDTH, 20) INST_MEM(
        .addr(pc),
        .data(instruction)
    );
    
    //////////////////////////////////////
    //// Register Write Source Select ////
    //////////////////////////////////////
    /* wd_data or imm */
    mux2 #(DATA_WIDTH) MUX_REG(
        .din0(wb_data),
        .din1(pc4),
        .select(Jump),
        .dout(rd_data)
    );
    
    ///////////////////////
    //// Register File ////
    ///////////////////////
    RegFile #(DATA_WIDTH, REG_ADDR_WIDTH) REG_FILE(
        .clk(clk),
        .rst(rst),
        .RegWrite(RegWrite),
        .rd_addr(instruction[11:7]),
        .rs1_addr(instruction[19:15]),
        .rs2_addr(instruction[24:20]),
        .rd_data(rd_data),
        .rs1_data(rs1_data),
        .rs2_data(rs2_data)
    );
    
    /////////////////////////////
    //// Immediate Generator ////
    /////////////////////////////
    ImmGen #(DATA_WIDTH) IMM_GEN(
        .instruction(instruction),
        .imm(imm)
    );
    
    //////////////////////
    //// Control Unit ////
    //////////////////////
    ControlUnit CU(
        .opcode(instruction[6:0]),
        .ALUSrc(ALUSrc),
        .MemtoReg(MemtoReg),
        .RegWrite(RegWrite),
        .MemRead(MemRead), 
        .MemWrite(MemWrite), 
        .Branch(Branch),
        .Jump(Jump),
        .Jalr(Jalr), 
        .ALUOp(ALUOp)
    );
    
    /////////////////////
    //// ALU Control ////
    /////////////////////
    ALUControl ALU_CTRL(
        .ALUOp(ALUOp),
        .funct7(instruction[31:25]),
        .funct3(instruction[14:12]),
        .opcode5(instruction[5]),
        .operation(operation)
    );
    
    ///////////////////////////
    //// ALU Source Select ////
    ///////////////////////////
    assign ALU_a = rs1_data;
    
    /* rs2_data or imm */
    mux2 #(DATA_WIDTH) MUX_ALU(
        .din0(rs2_data),
        .din1(imm),
        .select(ALUSrc),
        .dout(ALU_b)
    );
    
    /////////////////////
    //// ALU Control ////
    /////////////////////
    alu #(DATA_WIDTH) ALU(
        .operation(operation),
        .A(ALU_a),
        .B(ALU_b),
        .ALUResult(ALUResult)
    );
    
    /////////////////////
    //// Data Memory ////
    /////////////////////
    DataMem #(DATA_WIDTH, DATA_ADDR_WIDTH, 20) DATA_MEM(
        .clk(clk),
        .rst(rst),
        .addr(ALUResult),
        .MemRead(MemRead),
        .MemWrite(MemWrite),
        .write_data(rs2_data),
        .read_data(mem_data)
    );
    
    //////////////////////////////////
    //// Write-Back Source Select ////
    //////////////////////////////////
    /* wd_data or imm */
    mux2 #(DATA_WIDTH) MUX_WB(
        .din0(ALUResult),
        .din1(mem_data),
        .select(MemtoReg),
        .dout(wb_data)
    );
endmodule
