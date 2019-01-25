# 02_web project

> SSAFY Bootstrap 활용 과제

영화 추천 사이트를 위한 반응형 웹사이트 구현 과제 (HTML / CSS / Bootstrap)

## 1. basic layout

요구 명세서에 기초 레이아웃으로 `Navigation Bar`, `Header`, `Footer`를 요구하였습니다.

### HTML 기초

요구사항의 필수 요소는 다음과 같습니다.

1. DOCTYPE은 html입니다.
2. html 의 언어는 한국어(ko)입니다.
3. meta 태그에 인코딩 설정을 UTF-8로 설정해주세요.
4. meta 태그에 기본 viewport 설정을 해주세요. (width: device-width, initial-scale: 1.0)
5. title 태그는 영화추천사이트 라고 설정해주세요.

위 요구사항을 충족하기 위해 아래와 같이 html 문서를 설정했습니다.

```html
<!DOCTYPE html> <!-- 1. DOCTYPE 설정 -->
<html lang="ko"> <!-- 2. 언어 ko 설정 -->
<head>
    <!-- ... -->
    <meta charset="UTF-8"> <!-- 3. meta 태그에 UTF-8로 인코딩 설정  -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- 4. meta 태그에 기본 viewport 설정 -->
    <title>영화추천사이트</title> <!-- 5. 영화추천사이트로 제목 설정 -->
    <!-- ... -->
```

### Navigation Bar

Navigation Bar 요구사항은 다음과 같습니다.

1. 최상단에 위치해야합니다.
2. Item List(예시 - Home/친구평점보러가기/Login)는 우측 정렬입니다.
3. 반응형으로 구성되어 일정 수준 이하에서는 item이 숨김 처리 됩니다.
4. Sticky navigation bar로 구성됩니다.
5. Item List에서 Home을 제외한 것들은 아직 기능이 구현되어 있지 않으므로 클릭이 불가능(disable)합니다.

위 요구사항을 충족하기 위해 Navbar Bootstrap을 사용했습니다.

[Navbar Bootstrap 참고](https://getbootstrap.com/docs/4.2/components/navbar/#supported-content)

위 `Navbar Bootstrap`을 활용하여 다음과 같이 `Navigation Bar`를 구성했습니다.

```html
<nav class="navbar sticky-top navbar-expand-lg navbar-light bg-light"> <!-- 1, 4. sticky-top 클래스를 주어 navbar를 최상단에 고정했습니다. -->
    <a class="navbar-brand" href="#">영화추천시스템</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">
    <!-- 2, 3. 우측 정렬을 위해 justify-content-end로 우측정렬을 했습니다. 또한, 반응형으로 구성하기 위해 collapse bootstrap 클래스를 지정했습니다. -->
        <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
                <a class="nav-link disabled" href="#">친구 평점 보러가기</a>
            </li>
            <li class="nav-item">
                <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Log in</a>
            </li>
        </ul>
        <!-- 5. Item List에서 Home을 제외하고는 disabled로 지정해야하여 클릭 불가능하게 만들었습니다.-->
    </div>
</nav>
```

### Header

Header 요구사항은 다음과 같습니다.

1. Navigation Bar 바로 아래에 위치합니다.
2. 높이는 350px , 너비는 브라우저 전체 영역입니다.
3. 이미지는 선택적으로 활용 가능하되 반드시 배경 이미지가 있어야 합니다.
4. Header 영역의 수직/수평 가운데 정렬 위치에 h2 태그를 사용하여 작성 해주세요.

`Header`는 bootstrap을 사용하지 않고 html과 css로 구현하였습니다.

```html
<header id="header" class="intro">
    <h2 class="intro-title">당신에게 어울리는 영화를 추천해드립니다.</h2>
</header>
```

Header 부분은 의미를 명확히 하기 위해 `header` 태그로 html을 작성했습니다.

`영화추천시스템`이라는 사이트를 처음 소개하는 부분이므로 `intro`로 class 이름을 지정하였습니다.

위와 같이 마크업 한 후 아래와 같이 css를 적용하였습니다.

```css
/* 
 1. 바로 아래에 위치 하여야하므로 앞서 navbar에 sticky-top으로 주었습니다.
*/
.intro {
    height: 350px; 
    /* 2. 높이는 350px로 맞추었습니다. 너비는 전체이므로 따로 설정하지 않았습니다.  */
    display: flex;
    justify-content: center;
    align-items: center;
    /* 4. h2 태그 (.intro-title)를 Header 영역에 수직, 수평에 두기 위해 flex 설정을 했습니다. */
    background-image: url("01_layout_main.jpeg");
    background-repeat: no-repeat;
    background-size: cover;
    /* 3. 배경이미지를 설정하였습니다. */
}

.intro-title {
    width: 350px;
    color: #fff;
}
/* ... */
```

### Footer

`Footer`에 대한 필수 요구 사항입니다.

1. 브라우저 최하단에 위치합니다. 옵션 중 선택 - 1) Sticky 2) 내용 최하단
2. 높이는 50px 이상, 너비는 브라우저 전체 영역입니다.
3. 왼쪽에는 본인의 이름 혹은 닉네임, 오른쪽에는 헤더로 올라가는 링크로 구성됩니다.
4. Footer는 padding이 좌우로 3rem

`Footer`도 의미를 명확히 하기 위해 `footer` 태그를 사용하였습니다.

```html
<footer class="fixed-bottom">
    <span class="madeby">&#169; made by pkch</span>
    <a href="#header"><i class="fas fa-arrow-circle-up fa-lg"></i></a>
</footer>
```

위와 같이 마크업을 작성하였습니다. 최하단에 위치하기 위한 옵션으로 `fixed-bottom`을 주어 **1번 필수 요구 사항**을 충족하였습니다.

또한 **3번 필수 요구 사항**을 충족하기위해 class 이름으로 `madeby`를 사용해 제 닉네임이 들어나도록 했고 헤더로 올라가는 링크를 구성하기 위해 `a` 태그를 사용했습니다. `header`의 id가 `header`이므로 `href` 속성에 `#header`로 설정하여 헤더로 올라가는 링크를 구성했습니다.

```css
footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 50px;
    padding: 0 3rem;
    background: #a9a9a9;
}
/*
2. 높이 50px 이상이 요구사항이므로 height를 50px, 너비는 전체 영역이므로 따로 설정하지 않았습니다.

4. footer 영역의 padding을 좌우 3em 주어야하므로 padding: 0(상하) 3rem(좌우); 로 충족했습니다.
*/

footer > a {
    color: #fff;
}

footer > a:hover {
    color: #000;
}
```

### Font 설정

서로 다른 폰트를 2개 이상 활용해야 합니다.

```css
@import url('https://fonts.googleapis.com/css?family=Noto+Sans+KR&subset=korean');
@import url('https://fonts.googleapis.com/css?family=Nanum+Gothic&subset=korean');

* {
    font-family: 'Noto Sans KR', sans-serif;
}

/* ... */

footer > .madeby {
    font-family: 'Nanum Gothic', sans-serif;
}
```

구글 폰트 중 `Noto Sans`와 `Nanum Gothic`을 활용하였습니다.

전체적으로 `Noto Sans`를 사용했고 제 닉네임 표현에 `Nanum Gothic`을 사용했습니다.

[Google font](https://fonts.google.com/)

## 2. 영화 추천 사이트를 위한 영화 리스트 구성

`레이아웃`, `subtitle`, `Card view`가 해당 section의 주요 요구사항 입니다.

### 레이아웃

영화 리스트 구성시 영화 리스트는 container에 속하는 것이 필수 요구사항입니다.

```html
<!-- main container -->
<div class="container">
<!-- ... -->
```
따라서 위와 같이 카드리스트가 있을 부분을 `container`를 설정했습니다.

### subtitle

`subtitle`의 필수 요구 사항은 다음과 같습니다.

1. subtitle 영역은 위 아래 margin이 3rem입니다.
2. 글씨 부분은 h3 태그입니다.
3. 밑줄은 너비가 70px이고, 색상은 자유롭게 해주세요.


```html
<div class="subtitle">
    <h3>영화 목록</h3> 
    <!-- 2. 글씨를 h3 태그로 주었습니다. -->
</div>
```
```css
.subtitle {
    text-align: center !important;
    margin: 3rem 0;
} 
/* 
1. 영역의 위 아래 margin이 3rem이므로 위와 같이 margin을 주었습니다. */
.subtitle > h3::after {
    content: '';
    display: block;
    margin: 0 auto;
    width: 70px;
    padding-bottom: 1em;
    border-bottom: 3px solid orange;
}
/*
3. after 가상 선택자로 subtitle의 밑줄을 주었습니다. 너비가 70px이므로 width를 70px로 주었습니다.
*/
```

### card view

card의 필수 요구 사항은 다음과 같습니다.

1. 카드 총 6개 이상이며, 반응형으로 배치해야 합니다. 한 줄에 보이는 카드의 갯수는 다음과 같이 구성됩니다.
    576px 미만 : 1개
    576px 이상 768px 미만 : 2개
    768px 이상 992px 미만 : 3개
    992px 이상 : 4개
2. 카드는 각각 위 아래 margin이 1rem입니다.
3. 이미지는 반드시 alt 속성에 값이 있어야 합니다.
    img의 alt 속성은 alternate의 약자로, 이미지의 대안을 나타냅니다. 이미지가 서버 혹은 경로 오류로 인해 읽어 오지 못할 경우 해당 속성값이 대체하여 나타납니다.
4. 이미지 밑에는 h4 태그를 활용하여 영화 제목을 작성 해주세요.
5. 영화 제목 옆에는 네이버 영화 평점을 작성 해주세요. 영화 평점은 9점 이상인 경우 청색 계열의 색으로, 9점 미만인 경우는 어두운 계열
의 색으로 꾸며 주세요.
6. 제목 및 평점과 내용에는 구분선이 있습니다.
7. 구분선 아래에는 영화 장르와 개봉일을 작성 해주세요.
8. 가장 아래에는 네이버 영화 상세 정보 링크를 만들어 주세요. 링크는 반드시 새 창에서 열려야 합니다.

```html
<div class="col-12 col-sm-6 col-md-4 col-lg-3 my-3 p-0">
    <!--
         1. 반응형으로 배치하기 위해 col을 크기에 맞춰 bootstrap class를 구성하였습니다.
         2. 아래위 margindmf 1rem으로 주기 위해 my-3 클래스를 주었습니다.
    -->
    <div class="card">
        <img data-target="#modal--mal-mo-e" data-toggle="modal" src="assets/20184105.jpg" class="card-img-top"
            alt="영화 말모이">
        <!-- 3. alt로 해당 영화의 이름을 주었습니다. -->
        <div class="card-body">
            <h4 class="card-title border-bottom pb-3">
                말모이
                <span class="badge badge-info">9.04</span>
                <!-- 5. 네이버 평점을 bootstrap bedge로 주었습니다. 9점 이상은 청색으로 주기위해 bedge-info로 주었습니다. 9점 미만은 bedge-dark로 주었습니다. -->
            </h4>
            <!-- 4. 영화 제목은 h4 태그로 주었습니다. -->
            <p class="card-text">
                드라마
                <br>
                개봉일:2019.01.09.
            </p>
            <!-- 6, 7. 구분선은 card-title에 border-bottom을 주어 만들었습니다. 구분선 아래에 장르와 개봉을 작성했습니다. -->
            <a href="https://movie.naver.com/movie/bi/mi/basic.nhn?code=167699" target="_blank" class="btn btn-success">영화정보
                보러가기</a>
            <!-- 8. 새창에서 네이버 영화 상세 정보를 열기 위해 href에 네이버 영화 링크와 target 속성을 _blank로 주었습니다. -->
        </div>
    </div>
</div>
```

[bootstrap bedge 참고](https://getbootstrap.com/docs/4.2/components/badge/?)

[bootstrap card 참고](https://getbootstrap.com/docs/4.2/components/card/#example)

## 3. 영화 상세 보기

영화 상세 보기는 Modal로 구현하는 것이 목표입니다.

따라서 `bootstrap modal`을 사용했습니다.

[bootstrap modal 참고](https://getbootstrap.com/docs/4.2/components/modal/#modal-components)

```html
<div id="modal--mal-mo-e" class="modal fade" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">말모이, MAL-MO-E:The Secret Mission</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <div class="modal__movie modal__movie--info border-bottom">
                    <div id="mal-mo-e-carouselExampleControls" class="carousel slide" data-ride="carousel">
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img src="assets/20184105-1.jpg" class="d-block w-100" alt="영화 말모이 극중 이미지">
                            </div>
                            <div class="carousel-item">
                                <img src="assets/20184105-2.jpg" class="d-block w-100" alt="영화 말모이 극중 이미지">
                            </div>
                            <div class="carousel-item">
                                <img src="assets/20184105-3.jpg" class="d-block w-100" alt="영화 말모이 극중 이미지">
                            </div>
                        </div>
                        <a class="carousel-control-prev" href="#mal-mo-e-carouselExampleControls" role="button"
                            data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                            <span class="sr-only">Previous</span>
                        </a>
                        <a class="carousel-control-next" href="#mal-mo-e-carouselExampleControls" role="button"
                            data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                        </a>
                    </div>
                    <h5 class="mt-2">12세이상관람가</h5>
                    <p>누적 관객수:2,224,930</p>
                </div>
                <div class="modal__movie modal__movie--details p-2">
                    <p>
                        까막눈 판수, 우리말에 눈뜨다! vs 조선어학회 대표 정환, ‘우리’의 소중함에 눈뜨다!<br>
                        1940년대 우리말이 점점 사라져가고 있는 경성.<br>
                        극장에서 해고된 후 아들 학비 때문에 가방을 훔치다 실패한 판수.<br>
                        하필 면접 보러 간 조선어학회 대표가 가방 주인 정환이다.<br>
                        사전 만드는데 전과자에다 까막눈이라니!<br>
                        그러나 판수를 반기는 회원들에 밀려 정환은 읽고 쓰기를 떼는 조건으로 그를 받아들인다.<br>
                        돈도 아닌 말을 대체 왜 모으나 싶었던 판수는 난생처음 글을 읽으며 우리말의 소중함에 눈뜨고,<br>
                        정환 또한 전국의 말을 모으는 ‘말모이’에 힘을 보태는 판수를 통해 ‘우리’의 소중함에 눈뜬다.<br>
                        얼마 남지 않은 시간, 바짝 조여오는 일제의 감시를 피해 ‘말모이’를 끝내야 하는데…<br>
                        <br>
                        우리말이 금지된 시대, 말과 마음이 모여 사전이 되다
                    </p>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal" aria-label="Close">Close</button>
            </div>
        </div>
    </div>
</div>
```