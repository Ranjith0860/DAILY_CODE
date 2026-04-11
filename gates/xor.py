# binary digits
# /0000=8421

arr1=list(map(int,input("enter array spacee").split(" ")))
n=len(arr1)+1
arr_full=0
arr_sum=0
for i in range(1,n+1): 
    arr_full^=i
print("xor of full array 1 to n", arr_full)
for j in arr1:
    arr_sum^=j
print("xor of full array given array", arr_sum)
z=arr_full^arr_sum
print("missing number is ", z)