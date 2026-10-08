x = input()
if len(x)%2==0:
    mid = len(x)//2
    a = x[:mid]
    b = x[mid:]
    empty = ""
    for char in a:
        if char == "(" : 
            empty = empty + ")"

    if b == empty:
        print("balanced")
    else:
        print("unbalanced")
        
    

    
else:
    print("unbalanced")
    