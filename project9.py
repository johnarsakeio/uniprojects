a=int(input ('give a nubmer'))  
while True:
    result=0
    a=(a*3)+1
    while a>0:
        temp=a%10
        result=result+temp
        a=int(a/10)
    a=result
    if a<10:
        break
print (a)

    
