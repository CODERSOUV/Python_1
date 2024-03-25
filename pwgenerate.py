import random

l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

n=['0','1','2','3','4','5','6','7','8','9']
s=['!','@','#','$','%','^','&','*','(',')','-','_','+']
print("\nWellcome to Password Generator!")
while(1):
 print("\n\nPassword contaion atleast one character,number and symbol.\nTotal password length must be between 8 and 12 characters.\n")
 nl=int(input("How many letter you want in your Password?\n"))
 nn=int(input("How many numbers you want in your Password?\n"))
 ns=int(input("How many symbols you want in your Password?\n"))
 list=[]
 password=""
 total=nl+nn+ns
 
 if 8 <= total <= 12 and nl >= 1 and nn >= 1 and ns >= 1:
 
    for i in range(1,nl+1):
        char=random.choice(l)
        list+=char
        
    for i in range(1,nn+1):
        x=random.choice(n)
        list+=x
        
    for i in range(1,ns+1):
        y=random.choice(s)
        list+=y
    print(list)   
    random.shuffle(list)
    print(list)   
    
    print("Generated Password:")
    for i in list:
        password+=i
    print(password)
    break
  

 else:print("Invalid input. Password must meet the requirements.")