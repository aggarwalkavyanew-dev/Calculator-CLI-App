
print("""========================\n
   CLI CALCULATOR v1.0\n
========================""")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
         print("Error! Division by zero.")
         return None
    return x / y

def remainder(x, y):
    if y == 0:
        print("Error! Division by zero.")
        return None
    return x % y

def power(x, y):
    return x ** y

def display_menu():

    print("1. Addition (+) => add or +")
    print("2. Subtraction (-) => sub or -")
    print("3. Multiplication (*) => multi or *")
    print("4. Division (/) => div or /")
    print("5. Remainder (%) => remain or remainder")
    print("6. Exponentiation (**) => exp or power or ^")
    print("7. Exit => q or exit")
    print()
    print()
poss_choices=['add','sub','multi','div','remain','quit'
              'power','exit','q','exp','^','remainder'
    ,'/','*','-','+']

def mains():
    display_menu()
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input, try again.")


    while True:
        while True:
            try:
                choice = input("Enter operation to perform: ")
                choice = choice.lower()
                break
            except ValueError:
                print("Invalid input, try again.")


        if choice in poss_choices:
            if choice == 'q'or choice == 'exit'or choice == 'quit':
                break
            if choice == 'add'or choice == '+':
                result = add(num1, num2)
                print(result)
                print()
            if choice == 'sub'or choice == '-':
                result = subtract(num1, num2)
                print(result)
                print()
            if choice == 'multi'or choice == '*':
                result = multiply(num1, num2)
                print(result)
                print()
            if choice == 'div'or choice == '/':
                result = divide(num1, num2)
                print(result)
                print()
                if result is None:
                    num2 = float(input("Enter second number again: "))
                    result = divide(num1, num2)

            if choice == 'remain'or choice == 'remainder':
                result = remainder(num1, num2)
                print(result)
                print()
                if result is None:
                    num2 = float(input("Enter second number again: "))
                    result = remainder(num1, num2)
            if choice == 'power'or choice == 'exp'or choice == '^':
                result = power(num1, num2)
                print(result)
                print()

            num1 = result
            num3 = input("Enter another number: ")
            if num3 == 'q' or num3 == 'exit'or num3 == 'quit':
                break
            else:
                while True:
                    try:
                        num2 = float(num3)
                        break
                    except ValueError:
                        print("Invalid input, try again.")
                        num3 = input("Enter again: ")

if __name__ == '__main__':
    mains()




