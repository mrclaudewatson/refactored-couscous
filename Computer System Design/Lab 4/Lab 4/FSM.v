`timescale 1ns / 1ps

module VendingMealy(
    input clk, reset, quarter, dime, nickel, soda, diet,
    output reg GiveSoda, GiveDiet
);

    parameter S0 = 4'b0000, S5 = 4'b0001, S10 = 4'b0010, S15 = 4'b0011,
              S20 = 4'b0100, S25 = 4'b0101, S30 = 4'b0110, S35 = 4'b0111, 
              S40 = 4'b1000, S45 = 4'b1001;
              
    (*FSM_ENCODING = "SEQUENTIAL", SAFE_IMPLEMENTATION = "NO" *) 
    reg [3:0] state;
    reg queued_soda, queued_diet;

    always @(posedge clk or posedge reset) begin
        if (reset) begin
            state <= S0;
            queued_soda <= 0;
            queued_diet <= 0;
            GiveSoda <= 0;
            GiveDiet <= 0;
        end 
        else begin
            GiveSoda <= 0;
            GiveDiet <= 0;

            case (state)
                S0: if (nickel) state <= S5;
                    else if (dime) state <= S10;
                    else if (quarter) state <= S25;

                S5: if (nickel) state <= S10;
                    else if (dime) state <= S15;
                    else if (quarter) state <= S30;

                S10: if (nickel) state <= S15;
                     else if (dime) state <= S20;
                     else if (quarter) state <= S35;

                S15: if (nickel) state <= S20;
                     else if (dime) state <= S25;
                     else if (quarter) state <= S40;

                S20: if (nickel) state <= S25;
                     else if (dime) state <= S30;
                     else if (quarter) state <= S45;

                S25: if (nickel) state <= S30;
                     else if (dime) state <= S35;
                     else if (quarter) state <= S45;

                S30: if (nickel) state <= S35;
                     else if (dime) state <= S40;
                     else if (quarter) state <= S45;

                S35: if (nickel) state <= S40;
                     else if (dime) state <= S45;
                     else if (quarter) state <= S45;

                S40: if (nickel) state <= S45;
                     else if (dime) state <= S45;
                     else if (quarter) state <= S45;

                S45: begin
                    if (queued_soda || soda) begin
                        GiveSoda <= 1;
                        state <= S0;
                        queued_soda <= 0; 
                    end
                    else if (queued_diet || diet) begin
                        GiveDiet <= 1;
                        state <= S0;
                        queued_diet <= 0;
                    end
                end 
            endcase

            // if soda or diet is selected before enough money, queue the selection
            if (state != S45) begin
                if (soda) queued_soda <= 1;
                if (diet) queued_diet <= 1;
            end
        end
    end
endmodule