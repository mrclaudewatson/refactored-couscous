# �Hello World� program in RISC-V assembly
# Information on ecalls: https://github.com/TheThirdOne/rars/wiki/Environment-Calls

.globl __main						# global definition of main entry point
 	
.data								# start of the data segment 
	msg: .string "\n\n\nHello, Claude!"		# .string is an alias for .asciz, a null-terminated (\0) ASCII string
	msg2: .string "\nThis is CDA4205L Lab "
	
.text 							# start of the text segment
	__main: 			
		li 	a7, 4					# load value 4 into argument register a7, defines the "print string" ecall
		la 	a0, msg				# load address of label "msg" into argument register a0
		ecall						# perform the environment call (print string stored at address "msg" to the console)	
		
		li a7, 4
		la a0, msg2
		ecall	
		
		li a7, 5
		ecall
		
		li 	a7, 10 				# load value 10 into argument register a7, defines the "exit with code 0" ecall
		ecall						# perform the environment call
