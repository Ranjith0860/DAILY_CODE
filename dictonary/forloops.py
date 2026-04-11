nums=[11,22,33,11,22,33,44,55,66,11]
dic={}
for num in nums:
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
print(dic)

for key in dic.keys():
    print(key)
for value in dic.values():
    print(value)
for k,v in dic.items():
    print(k,v)

# sime conversion
ar=[11,22,33,44,55,11,22,33,44,55]
freq={}
for i in ar:
    freq[i] = freq.get(i, 0) + 1
print(freq)