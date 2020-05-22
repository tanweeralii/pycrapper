import dryscrape
from bs4 import BeautifulSoup
session = dryscrape.Session()
session.visit("https://twitter.com/explore/tabs/trending")
response = session.body()
soup = BeautifulSoup(response,features="lxml")
print(soup)


#for i in soup.body:
#    print(i)
#    j = i.split('\\n')
#print("Top Trendings in twitter are : \n")
#for i in j:
#    if 'data-trend-name=' in i:
#        split1 = i.split('\"')
#        split2 = split1[1].split('\\')
#        print(split2[0])
