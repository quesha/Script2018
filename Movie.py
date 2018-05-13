import urllib.request
from xml.etree.ElementTree import parse
from urllib.parse import quote

def py_xml_proc(data):
    for item in data.iterfind('channel/item'):
        Movie_title = item.findtext('title')
        Movie_pubDate = item.findtext('date')
        Movie_director = item.findtext('director')
        Movie_actor = item.findtext('actor')
        Movie_userRating = item.findtext("integer")
        movie_info = "제목 : {0} / 제작연도 : {1} / 감독 : {2} / 주 배우 : {3} / 네티즌 평점 : {4} ".format(Movie_title, Movie_pubDate, Movie_director, Movie_actor, Movie_userRating)
        print(movie_info)

def naver_search_xml(search_word):
    client_id = "aEPpWJgwVkbzvn7kqBaZ"  # 애플리케이션 등록시 발급 받은 값 입력
    client_secret = "H1htgE5oup"  # 애플리케이션 등록시 발급 받은 값 입력
    url = "https://openapi.naver.com/v1/search/movie.xml?display=100&query=" + quote(search_word) # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        xml_data = parse(response)
        py_xml_proc(xml_data)
    else:
        print("Error Code:" + rescode)

prompt = """
... 1. Movie Search
... 2. Blog Serach
... 3. News Search
... 4. Theater Search
... 5. Reamaining Seat Search
... 6. Quit
...
... Enter number: """
number = 0
while number != 6:
    print(prompt)
    number = int(input())
    if number == 1:
        movie_name = input("Enter Movie Name : ")
        naver_search_xml(movie_name)