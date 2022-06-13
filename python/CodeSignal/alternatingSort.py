a = [1, 3, 5, 6, 4, 2]
b = []
length = len(a)
for i in range(length):
    if i%2==0  :
        b. b.append(a[length - (i // 2) - 1]) 
    else:
        b.append(a[i // 2])

print(b)    