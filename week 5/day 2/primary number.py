num = input("Enter a Number: ")
num = int(num)

if num == 1 or num == 2 or num == 3 or num == 5 or num == 7 or num == 9:
    print("Yours is PRIMARY")
elif num % 2 == 0 or num % 3 == 0 or num % 4 == 0 or num % 5 == 0 or num % 6 == 0 or num % 7 == 0 or num % 8 == 0 or num % 9 == 0:
    print("Yours is not a PRIMARY")
else:
    print("Yours is PRIMARY")

