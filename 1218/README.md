# 2018 12.18 Tuesday

1. pyformat

python 2.x 버전에서는 `"%s %s" % (args1, args2)`와 같은 형식으로 포멧팅을 했다.

python 3.x 버전에서는 `"{} {}".format(args1, args2)`와 같은 형식으로 포멧팅을 했다.

최근의 python 3.6에서는 **f-string**을 지원해준다.

```python
print(f"내이름은 {arg}")
```
위와 같이 {}안에 변수명을 넣어서 쓸 수 있다.

[코드보러가기](pyformat.py)

[로또 예제 format으로 출력하기](lotto.py)

