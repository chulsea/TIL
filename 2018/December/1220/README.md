# 2018 12.20 Thursday

## 1. Flask의 request

Flask에서 client(브라우저)가 보내는 데이터를 받는 방법은 request라는 Flask **전역 객체**를 사용하는 것이다.

> Context Locals
>
> Flask가 threadsafe하게 메세지를 관리하는 방법
> 
> local의 특정 context(상태)에 있는 객체로 감싸져있는 전역객체를 사용하여 관리할 수 있다.
>
> request가 client로부터 요청이 생길때마다 생성되는데 이때 웹 서버는 새로운 thread를 생성한다.
>
> 이 때, 내부 요청을 처리하는 과정에서 현재 thread가 활성화됐는지, 현재의 application을 bind하는지, 해당 context가 WSGI environments 인지를 확인한다. 이는 서버를 끊지않고 한 application에서 다른 application을 부르는 방법이다.

get 방식으로 querystring을 가져오려면 **request.args**를 post 방식으로 form 데이터를 가져오려면 **request.form**을 참조하면 된다.

## 2. Redirects and Errors

flask에서 바로 redirect를 하는 방법은 redirect(url) 메서드를 사용한다.

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

다음과 같이 redirect 메서드를 이용하면 해당 url로 리다이렉트한다.

error는 **abort(status_code)**를 이용하여 http error를 발생할 수 있다. 위 코드는 401 error를 제공하여 request를 중단하는 예시이다.

그 외에 error를 커스텀해서 제어하는 방법은 errorhandler(status_code)를 이용하는 방법이다.

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```
다음과 같이 @app.errorhandler(status_code) 데코레이션으로 에러를 직접 커스텀할 수 있다.
