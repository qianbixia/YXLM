import requests
from bs4 import BeautifulSoup
import re
'''练习抓取百度新闻首页'''

def get_first_page(url,headers):
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text

def parse_one_page(html):
    soup = BeautifulSoup(html,'lxml')
    raw_lst = soup.select('li a[target="_blank"]')
    for lst in raw_lst:
        # print(lst)
        href = lst.attrs['href']
        title = lst.text
        # print(href,title)
        yield {
            "href":href,
            'title':title
        }
def write_to_file(content):
    with open('baidu_news.txt','a',encoding='utf8') as f:
        f.write(content)
        f.close()
def get_moduleName(url,headers):
    '''获取'''
    # url = 'http://news.baidu.com/'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    response = requests.get(url,headers=headers)
    try:
        response.status_code == 200
        html = response.text
        print('响应成功')
    except Exception as e:
        print(e)

    soup = BeautifulSoup(html,'lxml')
    total = len(soup.select('script'))
    print('Total: %d'% total)
    piece_html = soup.select('script')[-1].text
    patern = 'widgetList = \[(.*?)\];'
    result = re.findall(patern,piece_html)[0]
    # print(result)

    raw_widgetList = result.split(',')
    my_widgetList = []

    for li in raw_widgetList:
        li = li.strip()
        my_widgetList.append(li.replace("'",''))
    print(my_widgetList)
    return my_widgetList

def get_module_html(modulName):
    moduleUrl = 'http://news.baidu.com/widget?id=' + modulName
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    response = requests.get(moduleUrl, headers=headers)
    print("moduleUrl :%s"% response.url)
    if response.status_code == 200:
        # print(response.text)
        return response.text

def run():
    url = 'http://news.baidu.com/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    html = get_first_page(url,headers)
    for each in parse_one_page(html):
        # print(each)
        write_to_file(str(each)+'\n')
    for module in get_moduleName(url,headers):
        module_html = get_module_html(module)
        for each in parse_one_page(module_html):
            write_to_file(str(each) + '\n')

if __name__ == '__main__':
    run()