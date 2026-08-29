"""
Check if a year is a leap year. Rule: divisible by 4, EXCEPT century years (divisible by 100) unless also divisible by
400.
Hint: This needs nested or combined conditions — think about what makes a year divisible by 4 “not a leap year”
(the century exception), and what makes it “a leap year again” (the 400 exception).

"""
x = int(input(" Year: "))
if x%4 == 0 :
    print("Leap year ")
else:
    print("Normal year ")