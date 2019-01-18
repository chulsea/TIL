# 2019 01.18 Friday

> SSAFY Python Project

## 1. boxoffice.csv
   
   boxoffice.csv는 영화진흥위원회(`kobis`)의 API를 이용하여 `2019년 1월 13일`을 기준하여 10주간의 주간 박스오피스 TOP 10데이터를 가공한 파일입니다.

   10주간의 데이터(월~일)를 조회하였으며 `다양성/상업 영화`, `한국/외국 영화`, `모든 상영지역` 범주에 있는 박스오피스 데이터입니다.

   - Request URL
    
        ```
        "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={kobis_key}&weekGb=0&targetDt="
        ```

      - key: API를 가져오기 위한 인증키
      - weekGb: 주간 데이터를 받기 위해 설정 (기본 값은 1로 금~일의 주말 데이터 가져옴)
      - targetDt: 해당 일이 포함된 주를 조회 
    
      이때 targetDt를 프로그래밍적으로 해결하기 위해 `datetime` 모듈을 사용하였습니다. `datetime.date(2019, 1, 13)`으로 `2019년 1월 13일` 기준 날짜를 설정하고 `datetime.timedelta(7)`로 일주일 간격을 조절하였습니다.

   - response
    
      boxoffice.csv를 만들기 위해 영진위 api에서 필요한 데이터는 `영화 대표코드(movieCd)`, `영화명(movieNm)`, `해당일 누적관객일(audiAcc)`입니다.

      위 데이터를 이용하여 `영화 대표코드`는 `movie_code`, `영화명`은 `title`, `해당일 누적 관객일`은 `audience`, 해당일은 `recorded_at`으로 컬럼을 설정하였습니다. 이를 통해 boxoffice.csv를 만들었습니다.

      이 때 중복되는 영화가 있을 수 있는데 최근 주간을 기준으로 데이터를 받으므로 뒤에 만약에 중복되는 영화가 있다면 데이터에 넣지 않고 다음 for문으로 넘어갔습니다.

## 2. movie.csv

`movie.csv`는 앞서 구한 `boxoffice.csv`의 `movie_code`를 참고하여 해당 영화의 상세 정보를 담은 csv파일입니다.

- request
    
    ```
     http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={kobis_key}&movieCd=
    ```

    위 url을 사용하여 movie code에 맞는 영화의 세부정보를 가져올 수 있습니다.

- response

     `movie.csv`를 만드는데 필요한 정보는 `영화 대표코드`, `영화명(국문)`, `영화명(영문)`, `영화명(원문)`, `개봉연도`, `상영시간`, `장르`, `감독명`, `관람등급`, `배우1`, `배우2`, `배우3` 입니다.

     이 정보를 api 문서를 참고하여 `dict`형태로 저장하였습니다.

     그후 DictWriter를 활용하여 csv 파일로 만들었습니다.

## 3. movie_naver.csv

- request

     ```
     https://openapi.naver.com/v1/search/movie.json?query=
     ```

     위 url로 naver 검색 api를 사용할 수 있습니다.

     `query` 요청 변수에 검색하고자 하는 영화명을 설정하면 해당 영화의 정보를 뽑아 올 수 있습니다.

- response

     위 request로 `썸네일 이미지 url(image)`, `하이퍼텍스트 link(link)`, `유저평점(userRating)`을 가져올 수 있습니다.

     위 정보로 `movie_naver.csv`를 만들었습니다.

## 4. images

위 `movie_naver.csv`에서 썸네일 이미지 경로를 받아 requests로 이미지(바이너리 데이터)를 가져올 수 있습니다.

```python
res = req.get(data[0], stream=True)
```

위와 같이 `stream` 속성을 `True`로 설정하면 바이너리 파일로 해당 url의 정보를 가져올 수 있습니다. 즉, 해당 url의 이미지를 가져올 수 있습니다.

이렇게 보낸 요청이 제대로 받아왔다면 (`status_code == 200`) res의 `iter_content`를 가져와 images에 저장하였습니다.

```python
os.mkdir('images')
for data in datas:
    res = req.get(data[0], stream=True)
    if res.status_code == 200:
        with open(f'images/{data[1]}.jpg', 'wb') as f:
            for chunk in res.iter_content(1024):
                f.write(chunk)
```
참고로 images 폴더가 없다면 `open`에서 오류가 나므로 `os.mkdir`로 `images` 폴더를 만들었습니다.