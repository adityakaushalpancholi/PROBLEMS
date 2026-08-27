
"""
Q6.	Reverse	a	String	Without	Slicing	(Medium	—	String	Manipulation)
Reverse	a	string	manually,	without	using	
[::-1]	or	
reversed() .
Hint:	Build	a	new	empty	string,	and	either	loop	through	the	original	string	backwards	using	indices,	or	loop
forwards	and	prepend	each	character	to	the	result	instead	of	appending
"""

"""
x = int(input( " Enter a string : "))

string = []
while x!=0:
    v = x%10
    x = x//10
    string += v 
print(string)
so here my approach is right but logic fails 
""" 





"""
string = input()
reversed_string = ""
for i in range(1, len(string) + 1):
    reversed_string += string[-i]
print(reversed_string)

"""

x = int(input("Enter a number: "))

reversed_num = 0
while x != 0:
    digit = x % 10
    reversed_num = reversed_num * 10 + digit
    x = x // 10

print(reversed_num) # here the fall back is we cannot take other input like alphabates 
