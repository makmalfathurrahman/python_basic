i = 1
while i <= 5:
    print(i)
    i += 1

print("----------")


# Break
i = 1
while i <= 5:
    if i == 4:
        break
    print(i)
    i += 1

print("----------")


# Continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

print("----------")


# Else
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Finish!")

print("----------")
