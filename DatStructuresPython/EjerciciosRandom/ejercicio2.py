def isPalindrome(x):
    result = []
    if x < 0:
        return False
    while x > 10:
        s = x % 10
        x = x // 10
        result.append(s)
        if x < 10:
            result.append(x)

    print(result)
    k = list(reversed(result))


isPalindrome(1001)
