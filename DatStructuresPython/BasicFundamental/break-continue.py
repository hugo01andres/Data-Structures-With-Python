l = [10, 54, 2, 61, 15]

n = int(input('Enter Search Key: '))

for i in l:
    print(i, n)
    if i == n:
        print('Found')
        break

print('\n\n')
for i in l:
    if i % 2 != 0:
        continue
    print(i)