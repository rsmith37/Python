def printMessage(name):
    print("Hello and good morning" + name)

def printCalc(num1, num2):
    print(num1 + num2)

def recurse(width):
    if (width == 1):
      return "[]"
    output = ""
    for x in range(width):
        output += "[]"
    return recurse(width - 1) + "\n" + output

printMessage("Richard")
printCalc(2,3)
print(recurse(3))
