# A very contrived buffer overflow example
# A static buffer is the target for a read string operation.
# RARS ecall for read string requires a length, so you must intentionally
# exceed this length to overwrite the 16 byte buffer and replicate this in the
# password variable stored sequentially in memory. 
 
.data

	password_in: 	.space 16			# input buffer
	password:		.ascii "cda4205L"	# password

.align 3
	txtEntPass:	.asciz "\nEnter Password: "
	txtSuccess:	.asciz "\nSuccess!\n"
	txtFailure:	.asciz "\nWrong Password!\n"

.text

	la a0, txtEntPass
	li a7, 4
	ecall

	la a0, password_in
	li a1, 50			# number of characters to read from input dialog
	li a7, 8			# ReadString
	ecall
	
	jal remove_nl		# ReadString adds a \n (new line) character, this routine removes it

	
	la s0, password_in
	la s1, password
	addi s4, s0, 8	
strcmp:
	lb s2, 0(s0)
	lb s3, 0(s1)
	bne s2, s3, exit_failure
	addi s0, s0, 1
	addi s1, s1, 1
	lb s2, 0(s0)
	beq s2, zero, exit_success 	# we have reached a null terminator
	beq s0, s4, exit_success	# we have reached the max bytes for the password and so far all have been equal to what was entered.
	j strcmp
	
exit_failure:
	
	li a7, 4
	la a0, txtFailure
	ecall
	j done

exit_success:
	
	li a7, 4
	la a0, txtSuccess
	ecall

done:
	li a7, 10
	ecall

remove_nl:
	
	li t0, '\n' 			# new line character
	mv t1, a0				# assuming a0 contains buffer address
rnl_loop:
	lb t2, 0(a0)
	beq t2, zero, rnl_done	# we have reached a null terminator before hitting the newline
	beq t2, t0, rnl_fnl		# branch to handle if we found a new line
	addi a0, a0, 1
	j rnl_loop
rnl_fnl:
	sb zero, 0(a0)
rnl_done:
	jalr ra
