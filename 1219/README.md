# 2018 12.19 Wendesday

## 1. Flask

flask는 micro web framework!

일반 웹 프레임워크보다 기능이 축소됐지만 가벼운 웹 프레임워크

```
pip install Flask
```

위와 같이 flask를 다운받을 수 있다.

```python
from flask import Flask

app = Flask("__name__")

@app.route("/")
def home():
    return "hello world!"
```

위와 같이 Flask로 웹 서버를 app 변수에 받을 수 있다.

`@app.route` 데코레이션으로 라우팅을 지정할 수 있다.

## 2. render_template

template 파일을 render 하는 방법, 다만 render_template도 외장 함수이기 때문에 import해서 사용해야한다.

```python
from flask import render_template 
```

이렇게 import한 **render_template**를 사용해서 html문서를 render할 수 있다. 하지만, 한가지 작업을 더해줘야 한다.

**templates**라는 폴더를 프로젝트 폴더 안에 생성한 후 render_template을 해야한다. render_template 함수가 파라미터로 들어온 파일을 탐색할 때 templates 폴더를 기준으로 탐색하기 때문이다.

## 3. static

css, js, img, layout 등 정적 파일을 Flask에서 제공하기 위해서는 **static** 폴더를 사용해야한다.

```
{{ url_for('static',filename='assets/css/main.css') }}
```

위 같은 형식으로 정적 파일을 import 받아 사용할 수 있다.
