remainder = lambda num: num % 2

print(remainder(5))


product = lambda x, y: x * y

print(product(2, 3))


def testfunc(num):
    print(num)
    return lambda x: x * num


result10 = testfunc(10)
result100 = testfunc(100)

print(result10(9))
print(result100(9))


result10 = lambda x: x * 10
result100 = lambda x: x * 100
