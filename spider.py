import urllib.request
import requests
import os

path = ""

def get_hero_list(url):
    response = requests.get(url)
    if response.status_code == 200:
        print('请求hero列表成功')
        # print(response.json())
        jsonlist = response.json()
        # print(type(jsonlist))
        hero_list = jsonlist['hero']
        return hero_list


def get_one_hero(id):
    hero_url = 'https://game.gtimg.cn/images/lol/act/img/js/hero/' +id + '.js'
    reponse = requests.get(hero_url)
    if reponse.status_code == 200:
        print('请求单个hero成功，hero_id:' + id)
        jsonlist = reponse.json()
        pf_list = jsonlist['skins']
        return pf_list
def download_image(img_url,full_name):
    isFile = os.path.exists(full_name)
    if not isFile:
        print(full_name + ' 开始下载。。。')
        html = requests.get(img_url)
        f = open(full_name,'wb')
        f.write(html.content)
        print(full_name,' 保存成功')
        f.close()
        return True
    else:
        print(full_name + ' 图片已经存在')
        return False


def mkdir(file_name):
    global path #使用全局变量
    pwd = os.getcwd()
    print('当前路径：' + pwd)
    path = pwd + '\\' + file_name
    print("保存图片的路径： " + path)
    isExists = os.path.exists(path)
    if not isExists:
        os.mkdir(path)
        print(path  + ' 目录创建成功')

        return True
    else:
        print(path + ' 目录已存在')
        return False


def run(url):
    for hero in get_hero_list(url):
        id = hero['heroId']
        print("hero_id: " + id)
        for pf in get_one_hero(id):
            # print(pf)
            pf_full_name = path + '\\' + pf['heroName'] + pf['skinId'] +'.jpg'
            pf_url = pf['mainImg']
            # print("皮肤的name： " + pf_full_name)
            # print("皮肤的下载url： "+ pf_url)
            if pf_url :
                mkdir('pf')
                download_image(pf_url,pf_full_name)


if __name__ == '__main__':
    url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
    run(url)