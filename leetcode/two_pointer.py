arr1 = [50, 10, 70, 35, 20, 60]  
target = 70
left=0
right=len(arr1)-1

arr1.sort()
print(arr1)

while left<=right:
    mid=(left+right)//2
    if arr1[mid]== target:
        print("target found at index: ",mid)
        break
    elif arr1[mid]<target:
        left=mid+1
    else:
        rigth=mid-1
else:
    print("target not found in arr")
