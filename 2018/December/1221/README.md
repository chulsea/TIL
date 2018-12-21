# 2018 12.21 Friday

1. flask flash / response / Cookies / Sessions 

    - flash
    한 번만 사용하는 임시 메세지 

    보통 redirect와 url_for와 함께 사용한다.
    
    ```python
    flash(f"존재하지않는 소환사입니다.")
    return redirect(url_for('search_id'))
    ```

    > 단, application 객체에 secret_key attribute를 설정해줘야 오류없이 적용된다.

    - response

    view function의 return 값이 response 객체이다. Flask에서는 자동으로 return 값을 response 객체로 converting 해준다.

    > Flask가 response 객체로 converting하는 과정
    >
    > 1. view function이 return 값을 반환하자마자 올바른 타입(correct type)의 response 객체가 반환된다.
    >
    > 2. 만약 반환값이 string이라면 default parameter와 data를 생성한다.
    >
    > 3. 만약 튜플이라면 tuple 내부의 item들을 추가 정보(extra information)로 제공해준다. 
    >
    > 4. 위 Converting이 일어나지 않는다면 return value가 유효한 WSGI Application으로 인지하여 response 객체를 만들어 반환한다.

    - Cookies

    request의 **cookies attribute**를 통해 접근할 수 있다.

    ```python
    username = request.cookies.get('username')
    ```
    
    위와 같이 cookies의 username이라는 key를 가진 쿠키의 value을 username을 반환해준다.

    cookie를 response로 전달해주기 위해서는 response 객체에 set_cookie 메서드를 이용한다.

    > make_response(render_template(...))
    >
    > flask에서 response 객체를 만드는 방법
    
    ```python
    from flask import make_response

    @app.route('/')
    def index():
        resp = make_response(render_template(...))
        resp.set_cookie('username', 'the username')
        return resp
    ```
    위와 같이 response 객체인 resp에 set_cookie 메서드로 cookie를 추가할 수 있다.

    - Sessions

    flask는 session을 전역 객체로 지원해준다.

    사용은 다음과 같다.

    ```python
    from flask import Flask, session, redirect, url_for, escape, request

    app = Flask(__name__)

    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route('/')
    def index():
        if 'username' in session:
            return 'Logged in as %s' % escape(session['username'])
        return 'You are not logged in'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        return '''
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=Login>
            </form>
        '''

    @app.route('/logout')
    def logout():
        # remove the username from the session if it's there
        session.pop('username', None)
        return redirect(url_for('index'))

    # http://flask.pocoo.org/docs/1.0/quickstart/#sessions
    ```

    > escape는 template engine을 사용하지 않는다는 의미로 사용되었다.

    2. flask project layout

    ```
    /home/user/Projects/flask-tutorial
    ├── flaskr/
    │   ├── __init__.py
    │   ├── db.py
    │   ├── schema.sql
    │   ├── auth.py
    │   ├── blog.py
    │   ├── templates/
    │   │   ├── base.html
    │   │   ├── auth/
    │   │   │   ├── login.html
    │   │   │   └── register.html
    │   │   └── blog/
    │   │       ├── create.html
    │   │       ├── index.html
    │   │       └── update.html
    │   └── static/
    │       └── style.css
    ├── tests/
    │   ├── conftest.py
    │   ├── data.sql
    │   ├── test_factory.py
    │   ├── test_db.py
    │   ├── test_auth.py
    │   └── test_blog.py
    ├── venv/
    ├── setup.py
    └── MANIFEST.in
    ```
    > http://flask.pocoo.org/docs/1.0/tutorial/layout/
    
    위 폴더 구조는 flask 공식 홈페이지에서 제공하는 가이드 구조이다.

    - flaskr/ : application code와 files을 포함하는 python package
    - tests/ : test modules
    - venv/ : Flask와 그외 의존 라이브러리가 설치된 python 가상환경

    ```
    # 참고 .gitignore

    venv/

    *.pyc
    __pycache__/

    instance/

    .pytest_cache/
    .coverage
    htmlcov/

    dist/
    build/
    *.egg-info/
    ```

    3. flaskr/__init__.py

    flaskr의 `__init__.py`는 두 가지 역할을 한다.

    첫째는 application factory를 포함하는 역할, 두변째는 파이썬에게 flaskr 폴더가 파이썬 패키지임을 알려주는 역할이다.

    ```python
    import os

    from flask import Flask

    def create_app(test_config=None):
        # create and configure the app
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        )

        if test_config is None:
            # load the instance config, if it exists, when not testing
            app.config.from_pyfile('config.py', silent=True)
        else:
            # load the test config if passed in
            app.config.from_mapping(test_config)

        # ensure the instance folder exists
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        # a simple page that says hello
        @app.route('/hello')
        def hello():
            return 'Hello, World!'

        return app
    ```
    
    ### 1. app = Flask(__name__, instance_relative_config=True)
    
    위 부분은 Flask instance를 생성해준다.
    
    `__name__`은 현재 python module의 이름을 이미한다. (위 예시에서는 flaskr)

    instance_relative_config=True는 app 객체에 기본 설정이 아니라 상대경로에 있는 파일로 설정을 할 수 있도록 알려준다. 

    ```python
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('yourapplication.default_settings')
    app.config.from_pyfile('application.cfg', silent=True)
    ```
    위와 같이 설정을 상대 경로의 파일로 줄 수 있다.

    > ※ Flask.instance_path / Flask.open_instance_resource()
    >
    > Flask.instance_path : app 객체의 folder path를 알려준다.
    >
    > Flask.open_instance_resource() : 위 경로의 instance folder를 여는 메서드
    
    ```python
    filename = os.path.join(app.instance_path, 'application.cfg')
    with open(filename) as f:
        config = f.read()

    # or via open_instance_resource:
    with app.open_instance_resource('application.cfg') as f:
        config = f.read()
    ```

    ### 2. app.config.from_mapping()

    app에 기본설정을 할 수 있다.

    ```python
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    ```
    위 설정은 SECRET_KEY와 DATABASE 설정을 한 코드이다.

    SECRET_KEY는 random 값으로 지정하는 것이 좋다.

    DATABASE 지정시 사용한 **os.path.join**은 파라미터로 들어온 인자를 경로로 만들어주는 역할을 한다.

    ### 3. app.config.from_pyfile()

    만약 test_config가 없다면 flask가 기본으로 가지고 있는 config.py를 가지고 app의 설정을 진행한다. 다만 test_config가 있다면 해당 파일의 설정으로 덮어쓴다.

    위 구조로 만든 flask 앱을 실행하려면 `FLASK_APP=flaskr`과 `FLASK_ENV`=development를 환경변수로 설정한 후 flask run을 해주면 된다.