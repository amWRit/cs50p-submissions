expression = input("Enter expression: ")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

# print(f"Leave ${tip:.2f}")

if y == '+':
    print(f"{x+z:.1f}")
elif y == '-':
    print(f"{x-z:.1f}")
elif y == '*':
    print(f"{x*z:.1f}")
else:
    print(f"{x/z:.1f}")