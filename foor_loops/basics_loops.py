# sinngle loop print 1 to 100 num

# even odd number sum of num  print
n=int(input("enter a number find even or odd"))
even_count=0
odd_count=0
sum=0

for i in range(1,n+1):
    sum+=i
    if i & 1==0:
        print("even",i)
        even_count+=1
    else:
        print("odd" , i)
        odd_count+=1
print("total even count is ",even_count)
print("total odd count is ",odd_count)
print("sum of numbers is : ", sum)
        


# loops in strings
s="ranjith"
for i in s:
    for j in s:
        print(i+j,end=" ")
        
for i in range(0,len(s)):
    print(f"\n{s[i]}", end=" " )