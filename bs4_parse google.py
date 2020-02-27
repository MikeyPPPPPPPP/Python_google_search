import time
import bs4 as bs
import urllib.request

search = input('search: ')
url = 'https://www.google.com/search?q='+search


urls_on = []
page_in_url = []
text_for_page = []


headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
re = resp.read()

soup = bs.BeautifulSoup(re,'lxml')


def start():
    li = []
    for data in soup.find_all('div', class_='r'):
        for a in data.find_all('a'):
            if 'https://webcache.googleusercontent.com/' in a.get('href') or '/search' in a.get('href') or '#' in a.get('href'):
                pass
            else:
                text_for_page.append(a.text)
                page_in_url.append(a.get('href'))
                print('https://www.google.com'+a.get('href'))
                print(a.text) 
                
                
    for data1 in soup.find_all('tr', attrs={'valign':'top'}):
        for data2 in data1.find_all('td'):#, attrs={'class':'b navend'}):
            for a in data2.find_all('a', attrs={'class':'fl'}):
                urls_on.append('https://www.google.com/'+a.get('href'))
                li.append(a.text)
    print(li)
                
def pages(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    red = resp.read()
    soup = bs.BeautifulSoup(red,'lxml')
    curent = None
    rest = []
    urls = []
    stoper = []
    
    for data1 in soup.find_all('tr', attrs={'valign':'top'}):
        for data11 in data1.find_all('td', attrs={'class':'cur'}):
            curent = data11.text
    
    for data1 in soup.find_all('tr', attrs={'valign':'top'}):
        for data2 in data1.find_all('td'):#, attrs={'class':'b navend'}):
            for a in data2.find_all('a', attrs={'class':'fl'}):
                rest.append(a.text)
                urls.append('https://www.google.com/'+a.get('href'))
                stoper.append('https://www.google.com/'+a.get('href'))
                
    print('current ',curent)
    print('rest ',rest)
    
    urls_on.remove(urls_on[0])
    urls_on.append(stoper[-1])
    for data in soup.find_all('div', class_='r'):
        for a in data.find_all('a'):
            if 'https://webcache.googleusercontent.com/' in a.get('href') or '/search' in a.get('href') or '#' in a.get('href'):
                pass
            else:
                text_for_page.append(a.text)
                page_in_url.append(a.get('href'))
                print('https://www.google.com'+a.get('href'))
                print(a.text,'\n')
        


start()
time.sleep(2)
try:
    for x in range(1,20):
        url = urls_on[0]
        pages(url)
except:
    print('Error')

print('\n\n\n\nAll Results:\n\n')
for f, b in zip(page_in_url, text_for_page):
    print(f+'\n'+b+'\n')
                
