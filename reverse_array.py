#Iterative python program to reverse an array
def reverse(l,start,end):
    while start<end:
        l[start],l[end]=l[end],l[start]
        start+=1
        end-=1
l=list(map(int,input().split()))
reverse(l,0,len(l)-1)
print(l)