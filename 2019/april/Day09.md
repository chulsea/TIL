# 19.04.09 Tuesday

## Django Auth

1. sign up

- 회원가입은 CRUD에서 User를 생성하는 것과 같은 로직

- class User Model은 django에서 미리 만들어놨다.

  >  django.contrib.auth.models의 User 모델

- 또한, 이 User 모델은 ModelForm인 UserCreationForm으로 연동되어있다.

마찬가지로 UserCreationForm을 커스텀할 때는 UserCreationForm을 상속하여 커스텀한다.

```python
from django.contrib.auth.forms import UserCreationForm

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('boards:index')
	else:
		form = UserCreationForm()
	ctx = {
        'form': form,
	}
	return render(request, 'accounts/signup.html', ctx)
```

2. login

- 로그인의 경우 로그인 세션을 만들어주어야한다. django auth는 관련하여 세션 생성 및 유지 등을 관리해준다.

- 로그인 관련 폼은 AuthenticationForm과 연동되어있다.
- 또한, django의 세션과 연동하기 위해서는 `django.contrib.auth`에서 `login` 메서드를 import해주어야한다.
- 로그인이 되면 request의 user 변수에 접근하여 현재 로그인한 유저의 정보를 가져올 수 있다.

```python
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def login(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, request.POST)
		if form.is_valid():
			auth_login(request, form.get_user())
			return redirect('boards:index)
	else:
		form = AuthenticationForm()
	ctx = {
        'form': form,
	}
	return render(request, 'accounts/login.html', ctx)
		
```

3. logout

- 로그아웃은 CRUD에서 세션을 삭제하는 로직이다.

```python
from django.contrib.auth import logout as auth_logout

def logout(request):
	auth_logout(request)
	return redirect('boards:index')
```

※ user.is_authenticated

유저의 로그인 상황을 확인할 수 있는 방법으로 is_authenticated가 있다.

위 변수를 통해 현재 유저가 로그인 되었는지 안되었는지를 판단하여 다른 서비스를 제공할 수 있다.

> 예를 들면, 로그인하지 않은 유저는 글을 쓸 수 없다는 식의 서비스



