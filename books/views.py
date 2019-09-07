from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
from django.conf import settings

# Create your views here.


def index(request):
    return HttpResponse("Books Space")


def booksearch(request):
    if request.method == 'GET':
        client_id = settings.NAVERBOOK_CLIENT_ID
        client_secret = settings.NAVERBOOK_CLIENT_SECRET

        q = request.GET.get('q')  # html에 변수 붙이는거 쉽게 하기 위해
        encText = urllib.parse.quote("{}".format(q))  # 검색어 형식은 str로
        url = "https://openapi.naver.com/v1/search/book?query=" + encText  # json 결과
        # request라는 변수 이름이 같지만 다르게 쓰여서 변경

        book_api_request = urllib.request.Request(url)
        book_api_request.add_header("X-NAVER-Client-Id", client_id)
        book_api_request.add_header("X-NAVER-Client-Secret", client_secret)
        response = urllib.request.urlopen(book_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            # result 변수 만들어서 jsson 파일 읽고
            # 그 결과를 items 변수에 집어 넣고 그걸 템플릿에 띄울 수 있게
            items = result.get('items')
            # print(result)
            # request를 받아서 json 형식으로 출력해서 vs code에서 보여줌

            context = {
                'items': items
            }
            return render(request, 'books/booksearch.html', context=context)

        else:
            print("Error Code:" + rescode)
