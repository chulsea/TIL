numbers = [2, 3, 6, 11, 8]

s = ""
for i in numbers:
    s = s + str(i) + " "
print(s)

# 모범 답안
for i in numbers:
    print(i, end=" ")