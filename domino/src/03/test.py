j = "123"
print(len(j), -len(j))
g = True
while g:
    try:
        i = int(input("Enter any number: "))
    except ValueError:
        print("Invalid input. Please try again.")
    else:
        if i <= len(j) and i >= -len(j):
            g = False
