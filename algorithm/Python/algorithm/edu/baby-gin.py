
def solution(cards):
    answer = 6
    count = [0 for _ in range(12)]
    for card in cards:
        count[card] += 1
    i = 0
    while i < 10:
        if answer == 0:
            break
        if count[i] >= 3:
            count[i] -= 3
            answer -= 3
            continue
        if count[i] >= 1 and count[i + 1] >= 1 and count[i + 2] >= 1:
            count[i] -= 1
            count[i + 1] -= 1
            count[i + 2] -= 1
            answer -= 3
            continue
        i += 1
    return True if answer == 0 else False

def main():
    cards = list(map(int, input().split()))
    print(solution(cards))

if __name__ == "__main__":
    main()