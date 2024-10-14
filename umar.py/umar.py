# a = int(input("1st number: "))
# b = int(input("2nd number: "))


# def mod(x, y):
#     z = x%y
#     return z

# print(mod(a, b))
# def factorial():
#     i = int(input("input a number: "))
#     for z in range(i):
#         print(z)
# factorial()

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(12))