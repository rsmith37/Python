number = int(input("what is your number: "))
OddOrEven = number % 2
if(number == 0):
    print("0 is neither odd nor even and it neither positive nor negative")
elif(OddOrEven == 1):
    print("Your number is odd")
else:
    print("Your number is even")
