import bs4 as bs
import urllib.request

#url = 'https://www.google.com/search?q=python'



url = 'https://www.google.com/search?q=python&oq=python&aqs=chrome..69i57j69i60l3j69i61j69i60.2614j0j4&sourceid=chrome&ie=UTF-8'
    
#^ page 1
page_in_url = []


got_o = False



headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
red = resp.read()

#source = urllib.request.urlopen('https://www.google.com/search?q=python').read()

soup = bs.BeautifulSoup(red,'lxml')




#source = urllib.request.urlopen('https://www.google.com/search?q=python').read()
def get_pages_at_bottom():
    return page_in_url

    
def get_urls():
    for data in soup.find_all('td'):
        for a in data.find_all('a', attrs={'class':'fl'}):
            
            #print('page', a.get('href')) #for getting link
            page_in_url.append('https://www.google.com'+a.get('href'))
            #print(a.text)
        #get url of page under colerd O


    for x in page_in_url:
        print(x)

# gets all page nums on page
def get_page_nums():
    for data1 in soup.find_all('tr', attrs={'valign':'top'}):
        for data2 in data1.find_all('td'):#, attrs={'class':'b navend'}):
            for a in data2.find_all('a', attrs={'class':'fl'}):
                print(a.text)

def get_page_n_on():
    #gets page num you are on

    for data1 in soup.find_all('tr', attrs={'valign':'top'}):
        for data2 in data1.find_all('td', attrs={'class':'cur'}):
            
            print(data2.text)
            


def get_searches():
    #gets searches
    print('\nSearches on page\n')
    for data in soup.find_all('div', class_='r'):
        for a in data.find_all('a'):
            if 'https://webcache.googleusercontent.com/' in a.get('href') or '/search' in a.get('href') or '#' in a.get('href'):
                pass
            else:
                print(a.get('href')) #for getting link
                
                
                #print(a.text)
