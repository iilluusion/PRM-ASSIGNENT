n=int(input("enter no of elements"))
l=[str(x) for x in input("enter string for list ").split()][:n]
print("list before sorting with 2nd last element",l)
for i in range(0,len(l)):
    for j in range(0,len(l)-i-1):
        if (ord(l[j][-2])>ord(l[j+1][-2])):
            swap=l[j]
            l[j]=l[j+1]
            l[j+1]=swap
print("sorted list "  ,l)
