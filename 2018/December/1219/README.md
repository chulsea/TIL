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

> jinja
>
> flask는 jinja 문법을 사용한다.
>
> {{ var }} 와 같이 변수를 랜더링할 수 있다.

## 4. Variable Rules

URL 값을 변수로 받아올 수 있다.

url에 <>를 통해서 값을 변수로 받을 수 있다.

```python
@app.route("/user/<id>")
def my_id(id):
    return f"{id}고객님 안녕하세요"
```

위와 같이 url로 들어온 id를 my_id의 파라미터로 받아 사용할 수 있다.

```python
@app.route("/html_name/<name>")
def html_name(name):
    return render_template("hello.html", your_name=name)
```

여담으로 받은 변수를 render하는 html 파일에서 사용하기 위해서 변수를 지정할 수 있다. your_name이 바로 그 부분이며 html 내부에서 jinja 문법을 사용하여 render 할 수 있다.

위 url 값은 기본적으로 string으로 converting 된다. 이 값을 다르게 변환할 수 있다.

> ## - converter types
>
> - string : (default) accepts any text without a slash
>
> - int : accepts positive integers
>
> - float : accepts positive floating point values
>
> - path : like string but also accepts slashes
>
> - uuid : accepts UUID strings

다르게 변환하는 방법은 url 변수 지정시 `<type:var>` 형식으로 converting을 적용할 수 있다.
