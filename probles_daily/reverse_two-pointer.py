arr = ["ranjith", "kumar"]

result=[]

for i in arr:
    s=list(i)
    left = 0
    right = len(s) - 1

    while left < right:
        s[left],s[right] = s[right],s[left]
        left+=1
        right-=1

    rev = ""
    for j in s:
        rev+=j

    result.append(rev)
print(result)