# init --------------
li t1, 2024
nop
nop
# start -------------
load_use1:
lw s4, 12(t1)
add t5, s4, s0
sub s1, t6, s0
or s2, t6, s0
load_use2:				
lw s4, 12(t1)			
add t5, s4, s0			
sub s4, t6, s0			
or s2, t6, s0			
no_dep:					
lw s4, 12(t1)			
add t5, t6, s0			
sub t2, t0, s1			
or s5, s6, t6			
alu_then_branch:		
sub t3, t4, t5			
sub s3, s3, t0			
add t0, s4, t2			
beq t0, t5, load_then_branch		
load_then_branch:		
add t4, t6, s0			
sub t2, t3, s1			
lw s4, 0(t1)					
beq t0, t5, fix_no_steal		
fix_no_steal:			
lw s4, 12(t1)			
add t5, t0, s0			
sub t2, t4, t6			
or s5, t0, t6			
add s3, s5, s6			
handshake:			
lw s4, 12(t1)			
add t5, t0, s0			
sub s5, t4, t6			
or s5, s0, t6			
add s3, s5, s6	