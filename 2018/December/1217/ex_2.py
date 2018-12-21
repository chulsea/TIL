numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd = [i for i in numbers if i % 2 != 0]
even = [i for i in numbers if i % 2 == 0]
"""
odd = []
even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
"""
print("홀수 :", odd)
print("짝수 :", even)