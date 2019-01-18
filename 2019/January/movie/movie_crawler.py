import requests as req, os, datetime, json, csv

kobis_key = os.environ['KOBIS_API_KEY']
naver_id = os.environ['NAVER_API_ID']
naver_secret = os.environ['NAVER_API_SECRET']
def kobis_make_csv():
    url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={kobis_key}&weekGb=0&targetDt="
    td = datetime.timedelta(7)
    dt = datetime.date(2019, 1, 20)
    movie = []
    check = set()
    for _ in range(10):
        dt -= td
        current = dt.strftime('%Y%m%d')
        movie_data = req.get(url + current).json()
        for data in movie_data['boxOfficeResult']['weeklyBoxOfficeList']:
            if data['movieCd'] not in check:
                movie.append({'movie_code': data['movieCd'], 'title': data['movieNm'], 'audience': data['audiAcc'], 'date': current})
                check.add(data['movieCd'])
    fieldnames = ('movie_code', 'title', 'audience', 'date')
    __write_movie_file('boxoffice.csv', fieldnames, movie)
    
def movie_details():
    url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={kobis_key}&movieCd="
    movie = []
    movie_code_list = __get_file_column_datas('boxoffice.csv', 'movie_code') 
    for code in movie_code_list:
        movie_data = req.get(url + code).json()
        movie_info = movie_data['movieInfoResult']['movieInfo']
        save_data = {
            'movie_code': movie_info['movieCd'],
            'movie_name_ko': movie_info['movieNm'],
            'movie_name_en': movie_info['movieNmEn'],
            'movie_name_og': movie_info['movieNmOg'],
            'prdt_year': movie_info['openDt'],
            'genres': movie_info['genres'][0]['genreNm'],
            'directors': movie_info['directors'][0]['peopleNm'],
            'watch_grade_nm': movie_info['audits'][0]['watchGradeNm'],
        }
        for i in range(len(movie_info['actors'])):
            if i > 2:
                break
            save_data['actor' + str(i + 1)] = movie_info['actors'][i]['peopleNm']
        movie.append(save_data)
    fieldnames = tuple(save_data.keys()) + ('actor1', 'actor2', 'actor3')
    __write_movie_file('movie.csv', fieldnames, movie)

def naver_movie_details():
    url = f"https://openapi.naver.com/v1/search/movie.json?query="
    headers = {
        'X-Naver-Client-Id': naver_id,
        'X-Naver-Client-Secret': naver_secret
    }
    movie = []
    movies = __get_file_column_datas('movie.csv', 'movie_name_ko')
    codes = __get_file_column_datas('movie.csv', 'movie_code')
    datas = list(zip(movies, codes))
    for data in datas:
        movie_data = req.get(url + data[0], headers=headers).json()
        save_data = {
            'movie_code': data[1],
            'thumb_url': movie_data['items'][0]['image'],
            'link_url': movie_data['items'][0]['link'],
            'user_rating': movie_data['items'][0]['userRating']
        }
        movie.append(save_data)
    __write_movie_file('movie_naver.csv', save_data.keys(), movie)

def save_images():
    thumbnails = __get_file_column_datas('movie_naver.csv', 'thumb_url')
    codes = __get_file_column_datas('movie.csv', 'movie_code')
    datas = list(zip(thumbnails, codes))
    os.mkdir('images')
    for data in datas:
        res = req.get(data[0], stream=True)
        if res.status_code == 200:
            with open(f'images/{data[1]}.jpg', 'wb') as f:
                for chunk in res.iter_content(1024):
                    f.write(chunk)

def __get_file_column_datas(filename, column_name):
    movie_code_list = []
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie_code_list.append(row[column_name])
    return movie_code_list

def __write_movie_file(filename, fieldnames, datas):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for data in datas:
            writer.writerow(data)

def main():
    kobis_make_csv()
    movie_details()
    naver_movie_details()
    save_images()

if __name__ == "__main__":
    main()