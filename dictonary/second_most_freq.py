# second most frequency


nums = [11,22,33,11,22,33,44,55,66,11]

freq={}
for i in nums:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
higest=-1
for value in freq.values():
    if value>higest:
        higest=value
print(higest)

second=-1
for i in freq.values():
    if i>second and i<higest:
        second=i
print(second)