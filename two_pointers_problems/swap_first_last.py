

arr = ["a", "b", "c"]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)


arr=["hi","hello","sun"]
# → ["ih","hello","nus"]
arr = ["hi", "hello", "sun"]

def reverse_word(word):
    s = list(word)
    left = 0
    right = len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return "".join(s)

# reverse first and last
arr[0] = reverse_word(arr[0])
arr[-1] = reverse_word(arr[-1])

print(arr)