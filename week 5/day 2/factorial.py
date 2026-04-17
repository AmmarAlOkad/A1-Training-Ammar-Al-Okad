num = int(input("Enter a Number: "))

def fact(n):
    result = 1
    if n > 0:
        result = n * fact(n - 1)
    return result

print( fact(num) )