"""
f = open("new.txt", "w")
f.write("Hello World!")
f.close()
"""
"""
with open("new.txt", "w") as f:
    f.write("Hello World!\n")
# Java의 try-with-resource와 유사함
"""
"""
f = open("new.txt", "r")
data = f.read()
print(data)
f.close()
"""

# with open("new.txt", "r") as f:
#     data = f.read()
#     print(data)

"""
with open("new.txt", "w", encoding="utf-8") as f:
    for i in range(1,6):
        data = f"{i}번째 줄입니다.\n"
        f.write(data)
"""

menu = ["돈까스", "치즈돈까스", "고구마크림돈까스", "치킨까스", "생선까스"]
menus = list(map(lambda x: x + "\n", menu))
# writeline
with open("menu.txt", "w", encoding="utf-8") as f:
    f.writelines(menus)
