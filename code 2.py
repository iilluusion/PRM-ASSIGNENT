def validtriangle(a,b,c):
    if(a+b>c) or (a+c>b) or (b+c>a):
        return("Valid triangle")
    else:
        return("invalid triangle")
def validrectangle(l1,b1,l2,b2):
    if (l1==l2 and b1==b2):
        return"valid rectangle"
    else:
        return"invalid rectangle"
    
    
a,b,c=int(input("enter length of triangle")),int(input("enter height of triangle")),int(input("enter base of triangle"))
l1,b1=int(input("Enter the first length of rectangle ")), int(input("Enter the first width of rectangle "))
l2,b2=int(input("Enter the second length of rectangle ")),int(input("Enter the second width of rectangle "))
a=validtriangle(a,b,c)
b=validrectangle(l1,b1,l2,b2)
print(a)
print(b)
