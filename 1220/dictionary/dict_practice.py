# dictionary 활용 기초

# 평균 구하기

"""
scores = {
    "국어": 87,
    "영어": 92,
    "수학": 40,
}

values = scores.values()

# for 문으로 평균 구하기
hap = 0
for s in values:
    hap = hap + s
avg = hap / len(values)

# 내장함수 사용하기
avg = sum(values) / len(values)
print(avg)
"""

# 반 평균 구하기
"""
scores = {
    "철수": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "영희": {
        "수학": 70,
        "국어": 60,
        "음악": 50
    }
}

ban = 0
i = 0
for score in scores.values():
    for s in score.values():
        ban += s
    i += len(score)
print(f"반 전체의 평균은 {ban / i}입니다.")

hap = 0
for s in scores.values():
    hap += sum(s.values()) / len(s.values())
print(f"반 전체의 평균은 {hap / len(scores)}입니다.")
"""

# 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳
cities = {
    "서울": [-6, -10, -5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

cold = ("", float('inf'))
hot = ("", float('-inf'))
for city, tmp in cities.items():
    min_tmp = min(tmp)
    max_tmp = max(tmp)
    if cold[1] > min_tmp:
        cold = (city, min_tmp)
    if hot[1] < max_tmp:
        hot = (city, max_tmp)
print(f"가장 추운 곳: {cold}")
print(f"가장 더운 곳: {hot}")