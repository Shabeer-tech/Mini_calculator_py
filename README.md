# 🧮 Mini Calculator – Python Project

Welcome to my **Mini Calculator**, a simple Python-based arithmetic calculator that performs basic mathematical operations: addition, subtraction, multiplication, and division.

## 🚀 Features
- Simple and user-friendly command-line interface
- Handles division by zero errors
- Allows continuous usage until the user exits

## 🛠️ Technologies Used
- Python 3

## 📄 Code Overview

```python
print("|=====================|")
print("|   MINI CALCULATOR   |")
print("|=====================|\n")

while True:
    n1 = int(input("enter first number : "))
    n2 = int(input("enter second number : "))
    sign = input("enter the sign(+,-,*,/): ")

    if sign == '+':
        print("result is", (n1 + n2))
    elif sign == '-':
        print("result is", (n1 - n2))
    elif sign == '*':
        print("result is", (n1 * n2))
    elif sign == '/':
        if n2 == 0:
            print("error division by zero")
        else:
            print("result is", (n1 / n2))
    else:
        print("choose the correct sign")

    again = input("do you want to use it again (y/n): ")
    if again.lower() != 'y':
        print("thank you for using calculator 😇 & Good bye 🙋‍♂️")
        break
```

📷 Output Example

|=====================|
|   MINI CALCULATOR   |
|=====================|

enter first number : 10  
enter second number : 5  
enter the sign(+,-,*,/): +  
result is 15  
do you want to use again it (y/n): n  
thank you for using calculator 😇 & Good bye 🙋‍♂️
