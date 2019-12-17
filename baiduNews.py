import re

str = "'civilnews', 'InternationalNews',  'EnterNews', 'SportNews', 'FinanceNews', 'TechNews', 'MilitaryNews','InternetNews',   'DiscoveryNews',  'LadyNews', 'HealthNews',   'PicWall'"

ls = str.split(",")
print(ls)
for i in ls:
    i = i.strip()
    print(i.replace("'",''))