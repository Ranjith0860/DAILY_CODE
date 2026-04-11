arr = [22, 11, 33, 44, 55, 11, 22, 33, 44, 11, 22, 33, 11]

# Step 1: Frequency count
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

# Step 2: Find max frequency manually
max_freq = -1
for v in freq.values():
    if v > max_freq:
        max_freq = v

# Step 3: Find largest element among most repeated
largest_most_repeated = -1
for k in freq:
    if freq[k] == max_freq:
        if k > largest_most_repeated:
            largest_most_repeated = k

# Step 4: Find least element that is not repeated (freq = 1)
least_not_repeated = None
for k in freq:
    if freq[k] == 1:
        if least_not_repeated is None or k < least_not_repeated:
            least_not_repeated = k

print("Largest among most repeated:", largest_most_repeated)
print("Least not repeated:", least_not_repeated)