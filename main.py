import requests
from bs4 import BeautifulSoup

res = requests.get('https://twitter.com/explore/tabs/tab_1')
soup = BeautifulSoup(res.text, 'html5lib')
for i in soup.body:
    print(i)
    j = i.split('\\n')
print("Top Trendings in twitter are : \n")
for i in j:
    if 'data-trend-name=' in i:
        split1 = i.split('\"')
        split2 = split1[1].split('\\')
        print(split2[0])
