s="namn"
l=0
r=len(s)-1
flag=True
for x in range(len(s)//2):
    if s[l]!=s[r]:
        flag=False
        break
    else:
        l+=1
        r-=1
if flag:
    print("Palindrome string")
else:
    print("Not Palindrome")
