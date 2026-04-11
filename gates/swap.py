a = 5
b = 3
# Output → a=3, b=5

a=a^b
b=a^b
a=a^b
print(a,b)

if a^0==0:
    print(a)
else:
    print(b)
    
arr = [1, 2, 3, 4]
# Find XOR of all elements
z=0
for i in arr:
   z=z^i
print(z) 