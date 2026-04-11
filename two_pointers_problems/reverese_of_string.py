arr = ["ranjith", "kumar"]
result=[]
z=list(arr[0])
left=0

right=len(z)-1
while left < right:
    print(z[left],z[right])
    z[left],z[right]= z[right],z[left]
    print(f"left is {z[left]}.right is{z[right]}")
    print(z)
    left+=1
    right-=1
arr[0]="".join(z)
print(arr)
