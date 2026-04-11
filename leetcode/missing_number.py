arr = [1, 2, 3, 4, 6]

# find the missing number
n=len(arr)+1
total=n*(n+1)//2
sum_of_arr=0
for i in arr:
    sum_of_arr+=i
print(sum_of_arr)
print(total)
missing=total-sum_of_arr
print("missing number through normal" ,missing)



# x or
full_arr=0
given_rr=0
for i in range(n+1):
    full_arr^=i
for i in arr:
    given_rr^=i
missin_num=full_arr^given_rr
print("missing number through xor",missin_num)
