.globl __main

.data

.text

__main:

    li s0, 0x10010000

    # white pixel
    li t0, 0x00FFFFFF
    sw t0, 0(s0)
    
    # red pixel
    li t0, 0x00FF0000
    sw t0, 4(s0)
    
    # green pixel
    li t0, 0x000FF000
    sw t0, 8(s0)
    
    # blue pixel
    li t0, 0x00000FF0
    sw t0, 12(s0)
    
    

    li a7, 10
    ecall
    
    