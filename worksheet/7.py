""" 
Q7.	Vowel,	Consonant,	Space	&	Digit	Counter	(Medium	—	String	Manipulation)
Given	a	string,	count	vowels,	consonants,	spaces,	and	digits	separately	in	a	single	pass.
Hint:	Loop	once	through	the	string,	and	inside	the	loop	use	
if-elif-else	branches:	check	
then	whether	the	lowercased	character	is	a	vowel,	else	treat	it	as	a	consonant.
isspace() ,	
isdigit() 

x = input("Enter a string: ")
vowel = 0 
consonant = 0 
space = 0
digits = 0
for char in x :
    if x.isalpha():
        if char in "aeiou":
            vowel +=1
        else : 
            consonant += 1
for char in  x:
    if x.isspace():
        if True:
            space+= 1
for char in  x:
    if x.isdigit():
        if True:
            digits += 1
print(f" Vowels{vowel} , Consonat{ consonant} , space{ space} , Digits{digits}") 

if i using for loop for char then i have to aplly isalpha and isspace in character 

"""
x = input("Enter a string: ")
vowel = 0
consonant = 0
space = 0
digits = 0

for char in x:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowel += 1
        else:
            consonant += 1
    elif char.isspace():
        space += 1
    elif char.isdigit():
        digits += 1

print(f"Vowels {vowel}, Consonant {consonant}, Space {space}, Digits {digits}")