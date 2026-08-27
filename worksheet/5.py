"""
Q5.	Digital	Root	(Repeated	Digit	Sum)	(Medium	—	Loops)
Given	a	number,	repeatedly	sum	its	digits	until	only	a	single	digit	remains	(e.g.,	
1+1=2 ).
Hint:	You will	need	a	loop	inside	a	loop	—	an	outer	
9875	→	
9+8+7+5=29	→	
2+9=11	→	
while	that	keeps	repeating	“as	long	as	the	number	has	more
than	one	digit,”	and	an	inner	loop	or	logic	to	sum	the	digits	of	the	current	number.
"""
x = int(input("enter a number "))
sum = 0
while x != 0:
    v = x % 10
    x = x // 10
    sum += v
    while sum > 9:
        z = sum%10
        sum = sum//10
        sum += z
