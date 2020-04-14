num = int(input("Press Number: "))
print("This is your Pyramid!")
a = num - 1
blank = ""
text = ""
for x in range(num):
    text += "*"
    for y in range(num):
        blank = " " * a
    print(blank + text)
    text += "*"
    a -= 1