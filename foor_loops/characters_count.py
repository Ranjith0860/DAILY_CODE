
# Count characters
# Count number of characters in a string
# Reverse string
# Print a string in reverse using loop


s="ranjith kumar     hanuman r"
count=0
for str in s:
    if str==" ":
        continue
    else:
        count+=1
print(count)


re="ranjitH KumaR"
rev=""
for i in re:
    rev=i+rev
print(rev)

re = "ranjitH KumaR"

words = re.split()
rev_words = []

for i in range(len(words)-1, -1, -1):
    rev_words.append(words[i].lower())

print(",".join(rev_words))