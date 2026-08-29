"""
Q4.	Prime	Number	Checker	(Medium	—	Loops)
Write	a	function	that	checks	if	a	number	is	prime,	using	a	loop	(no	built-in	libraries).
Hint:	A	number	is	prime	if	no	number	from	2	up	to	its	square	root	divides	it	evenly.
You	don	need	to	check	all
the	way	up	to	
n-1	—	that	a	common	inefficiency	worth	avoiding.

"""
x = int(input(" enter a no "))
sum  = 0 

for i in range(2, (x-1)):
    v = x%i 
if sum == 0:
    print("prime")
else:
    print("not a prime")