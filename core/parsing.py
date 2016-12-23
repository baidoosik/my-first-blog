from bs4 import BeautifulSoup as bs
import requests as req

def _search_naver(key_word):
    req1= req.get('https://search.naver.com/search.naver?where=webkr&sm=tab_jum&ie=utf8&query={}'.format(key_word))
    html =req1.text
    soup= bs(html, 'html.parser')

    search_results = soup.select(
        'dl > dt > a'
    )
    result ={}

    for i in search_results:
       # print('제목' + result.text)
       # print('링크' + result['href'])
       result[i.text] = i['href']

    return result

if __name__=='__main__':
    print(_search_naver('some_thing'))
