import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt


URL = "https://kaktus.media/"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='Dashboard--group')
    kaktus_list = []
    for item in items:
        kaktus_list.append(
            {
                'title_name': item.find('a', class_='Dashboard-Content-Card--name'),
                'title_url': URL + item.find('a').get('href'),
                "image": URL + item.find('a', class_='Dashboard-Content-Card--image').find('img').get('src'),


            }


        )
        return kaktus_list


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        kaktus_list2 = []
        for page in range(0, 1):
            html = get_html(f"https://kaktus.media/", params=page)
            kaktus_list2.extend(get_data(html.text))
        # print(kaktus_list2)
        return kaktus_list2
    else:
        raise Exception('Error in parser')


# parser()





