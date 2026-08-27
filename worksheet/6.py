
"""
Q6.	Reverse	a	String	Without	Slicing	(Medium	—	String	Manipulation)
Reverse	a	string	manually,	without	using	
[::-1]	or	
reversed() .
Hint:	Build	a	new	empty	string,	and	either	loop	through	the	original	string	backwards	using	indices,	or	loop
forwards	and	prepend	each	character	to	the	result	instead	of	appending
"""
x = input( " Enter a string : ")

string = []
while x!=0:
    v = x%10
    x = x//10
    v = int(v)
    string += v 

print(string)