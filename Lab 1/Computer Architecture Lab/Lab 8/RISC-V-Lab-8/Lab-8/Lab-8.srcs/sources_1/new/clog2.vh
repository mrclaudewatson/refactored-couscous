`ifndef _clog2_vh_
`define _clog2_vh_

    // Computer ceil(log2(value))
    // if ceil(log2(value))=0, then return 1 (useful when setting reg size) 
    function integer clog2(input integer value);
        begin
        if (value <= 1)
            clog2=1;
        else begin
            value = value-1;
            for (clog2=0; value>0; clog2=clog2+1)
                value = value>>1;
            end
        end
    endfunction

`endif //_clog2_vh_