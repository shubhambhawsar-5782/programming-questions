#Iterative python program to reverse an array
def reverse(l,start,end):
    while start<end:
        l[start],l[end]=l[end],l[start]
        start+=1
        end-=1
l=list(map(int,input().split()))
reverse(l,0,len(l)-1)
print(l)
#Time Complexity : O(n)


# Recursive python program to reverse an array
"""def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
 
# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)"""
