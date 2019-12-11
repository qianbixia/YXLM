from filecmp import cmp

import requests
#
# name = 'fff-K/DA /\?*:"<>|伊芙琳.jpg'
# for char in ['/','\\','?','*',':','<','>','|']:
#     if char in name:
#         newName = name.replace(char,'')
#         name = newName
#         print(name)
# dict = {"name1": "痛苦之拥-K/DA 伊芙琳28006.jpg";"name3":"提莫"约德尔人的一大步""}
# name2 = dict["name"]
# print(name2)
# for char in ['/','\\','?','*',':','<','>','|','"']:
#     if char in name2:
#         newName = name2.replace(char,'')
#         name2 = newName
#         print(name2)

# name2dic={"id":"17003"}
# print(dic["id"])
# if cmp(dic["id"],str(17003)):
#     print('22')
pf = {"skinId": "32004","name": "殇之木乃伊-阿木木“主人不要我了”32004.jpg"}
if pf['skinId'] == "32004":

    print('11')
    print('32004原来：', pf['name'])
    pf['name'] = pf['name'].replace('“', '')
    pf['name'] = pf['name'].replace('”', '')
    print('32004处理：', pf['name'])
# pf_full_name = "提莫:\"约德尔人的一大步\""
# for char in ['/', '\\', '?', '*', ':', '<', '>', '|', '"']:
#     # 有的名称有非法字符,没法保存，需要处理一下
#     if char in pf_full_name:
#         # tep_name = pf['name'].replace(char,'')
#         # pf['name'] = tep_name
#         temp = pf_full_name.replace(char, '')
#         pf_full_name = temp
#         print('去掉非法字符后的路径 + 图片名称：', pf_full_name)

