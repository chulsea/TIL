import random

lotto_numbers = list(range(1,46))
jackpot = random.sample(lotto_numbers, 6)
print(f"오늘의 행운 번호는 {sorted(jackpot)}") # f-string
print("오늘의 행운 번호는 {}".format(jackpot)) # py format
print("오늘의 행운 번호는 " + str(jackpot))