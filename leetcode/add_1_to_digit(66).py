# leetcode 66 add plus 1 to number ex=.123=123+1=1234,99=>99+1=100
# if we add +1 to any number it gives 10 ex 9+1 =10 we keep last digit is 0 else we add last digit +1
nums = list(map(int,input("enter with ,: ").split(",")))

for i in range(len(nums)-1, -1, -1):
    if nums[i] < 9:
        nums[i] += 1
        break
    else:
        nums[i] = 0

# If first element became 0 → add 1 at front
if nums[0] == 0:
    nums = [1] + nums

print(nums)