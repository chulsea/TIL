# 2018 12.18 Tuesday

### 1. pyformat

python 2.x 버전에서는 `"%s %s" % (args1, args2)`와 같은 형식으로 포멧팅을 했다.

python 3.x 버전에서는 `"{} {}".format(args1, args2)`와 같은 형식으로 포멧팅을 했다.

최근의 python 3.6에서는 **f-string**을 지원해준다.

```python
print(f"내이름은 {arg}")
```
위와 같이 {}안에 변수명을 넣어서 쓸 수 있다.

[코드보러가기](pyformat.py)

[로또 예제 format으로 출력하기](lotto.py)

### 2. os

- os.chdir(r'파일경로')

현재 작업 폴더를 바꾸는 메서드

```python
os.chdir(r'C:\Users\student\Desktop\TIL\1218\dummy')
```

- os.listdir('경로')

해당 경로에 있는 파일들의 파일명을 list 형태로 가져오는 메서드

```python
os.listdir('.')
```

- os.rename('현재 파일명', '바꿀 파일명')

현재 작업경로에 있는 파일명을 바꿀 파일명으로 바꾸는 메서드

- os.getcwd()

현재 작업경로를 가져오는 메서드

[코드보러가기](ch_name.py)

### 3. 파일 다루기

- open

파일을 여는 메서드, python 내장 함수이므로 그냥 사용할 수 있다.
open(filename, mode)를 기본으로 사용할 수 있다.
mode는 'r'(읽기 모드), 'w'(쓰기 모드) 등을 많이 쓴다.

- close

파일 작업이 끝난 후 저장/닫기를 위한 메서드

- write / writelines

해당 파일에 data를 쓰는 메서드, writelines는 list를 파일에 쓰는 메서드

[코드보러가기](make_txt.py)
