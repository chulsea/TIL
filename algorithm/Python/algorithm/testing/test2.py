import datetime

start = datetime.datetime.now()
test1 = [[0 for i in range(1000000)] for _ in range(100)]
# print(test1)
print(datetime.datetime.now() - start)
start = datetime.datetime.now()
t = [0]
test2 = [t*1000000 for _ in range(100)]
# print(test2)
print(datetime.datetime.now() - start)