"""
# python 2.x
s2 = "%s %s" % ("hello", "world!")
print(s2)

# python 3.x
s = "{} {}".format("hello", "world!")
print(s)
"""

ko = "박경철"
en = "Park GyeongCheol"
myname = "한국 이름 : {}, 영어 이름 : {}".format(ko, en)
print(myname)

# f-string python 3.6
print(f"안녕하세요 {ko}입니다. My name is {en}")
