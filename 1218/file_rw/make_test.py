# not with
f = open("test.txt", "w", encoding="utf-8")
for i in range(1,6):
    data = f"{i}번쨰 줄입니다.\t"
    f.write(data)
f.close()

# with
with open("test.txt", "w", encoding="utf-8") as f:
    for i in range(1,6):
        data = f"{i}번쨰 줄입니다.\t"
        f.write(data)
