nums = [1,3,5,6]
target = 3

def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

print(searchInsert(nums, target))


# binary search 

def binarySearh(nums,target):
    result=len(nums)
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            result=mid
            right=mid-1
        else:
            left=mid+1
    return result
print(binarySearh(nums,target))
