def hashfun(value):
    hash_code = 0
    for char in value:
        hash_code += ord(char)
    return hash_code % 10   # hash bucket (0–9)

# input
arr = []
r = int(input("How many elements you want to insert: "))

for i in range(r):
    e = input("Enter element: ")
    arr.append(e)

print("Elements in arr:", arr)

# create hash table of size 10 with None
hash_table = [None] * 10

# insert according to hash index
for item in arr:
    h = hashfun(item)
    hash_table[h] = item   # store at exact index
    print(f"{item} hash code was: {h}")

print("Elements in hash table:", hash_table)
