# 1부터 n까지 한줄씩 숫자 출력
"""
item = int(input("번호를 입력해주세요! "))
for i in range(item):
    print(i+1)
"""

# list in 사용
"""
warn_investment_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
print(f"경고 종목 리스트 : {warn_investment_list}")
item = input("투자종목이 무엇입니까? ")
if item.lower() in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
"""

# list 요소 지우기
"""
colors = ["Apple", "Banana", "Coconut", "Deli", "Ele", "Grape"]
del colors[0] 
del colors[-2:]
print(colors)
"""

# dictionary indexing
"""
ssafy = {
    "location" : [ "서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}

print(ssafy["duration"]["semester1"], ssafy["location"][1], ssafy["classes"]["daejeon"]["manager"])
"""
