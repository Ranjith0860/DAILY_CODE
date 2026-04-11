# merge sorted array and after smergingarray should asscending to des
# nums1 total values is m+n
# we loop from last of nums1,nums2 using two pinters

nums1,nums2=[1,2,7,0,0,0],[2,3,6]
m,n=3,3
midx=m-1
nidx=n-1
right=m+n-1

while nidx>=0:
    if midx >=0 and nums1[midx]> nums2[nidx]:
        nums1[right]=nums1[midx]
        midx-=1
    else:
        nums1[right]=nums2[nidx]
        nidx-=1
    right-=1
print(nums1)

#  explanation 
# nums1,nums2=[1,2,7,0,0,0],[2,3,6]
# m,n=3,3
# first=>midx=3-1=>2,nidx=3-1=>2
# nid>0,midx>0 and nums1[2] > nums2[2] so nums[right]=nums1[midx] 7>6  and right=0 right=>7
# midx-=1
# midx=1=>2<6 so right=6
# nidx-=1
# loop continues





