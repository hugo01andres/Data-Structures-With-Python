n = 5
i = 1
hola = 0

"""while i <= n:
    print(i)
    sum += i
    i += 1

print(sum)"""


def sum(n):
    if (n == 1):
        return 1
    return sum(n - 1) + n


print(sum(5))


def factorial(n):
    if n == 1:
        return 1
    return factorial(n -1)
