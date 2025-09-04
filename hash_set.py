my_hash_set = [[] for _ in range(10)]

def hashfun(value):
    sum_m = 0 
    for char in value :
        sum_m += ord(char)
    return sum_m % 10

def add(value):
    index = hashfun(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)
    else:
        print("Element already Exist")

def retr(value):
    index = hashfun(value)
    bucket = my_hash_set[index]
    if value in bucket:
        return value in bucket
    else:
        print("No value !")

print(my_hash_set)

print("Operations: 1.Add  2.Retrive")
op = int(input("Your Choise:"))
if op==1:
    ad = input("Value:")
    add(ad)
elif op==2:
    rt = input("Value:")
    retr(rt)

print("Final Hast set:", my_hash_set)
    
