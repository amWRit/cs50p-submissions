text = input("Input: ")
output = ''
for c in text:
    if c.lower() in ['a', 'e', 'i', 'o', 'u']:
        c = ''
    output += c

print("Output:", output)