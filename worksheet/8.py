"""
Q8.	Pangram	Checker	(Medium/Hard	—	String	Manipulation)
Check	if	a	sentence	is	a	pangram	(contains	every	letter	of	the	alphabet	at	least	once),	ignoring	case.
Hint:	Track	which	letters	you’ve	seen	in	a	set	as	you	loop	through	the	(lowercased)	sentence.	At	the	end,	compare
the	size	of	your	set	of	seen	letters	to	26	—	or	check	if	all	26	letters	are	present.

"""
x = input().lower()

digit = 0 
for char in x :
    if 97 <=ord(char)<=122 :
        if char.isalpha(): # this gives a bool value 
            digit += 1
        else : 
            print("You Idiot its not a pangram ")
if digit >= 26 :
    print ( " Is a pangram")