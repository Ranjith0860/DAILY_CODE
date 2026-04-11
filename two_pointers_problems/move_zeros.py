arr = [0, 0, 1, 11, 0, 12]

j = 0  # place for non-zero

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1

print(arr)