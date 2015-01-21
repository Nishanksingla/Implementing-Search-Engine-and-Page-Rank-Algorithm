import HTMLParser
import cStringIO
from bs4 import BeautifulSoup
import urllib2

class HTML2Text(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.output = cStringIO.StringIO()
        self.var=0
    def get_text(self):
        return self.output.getvalue()
    
    def handle_starttag(self, tag, attrs):
        if tag == 'br':
            self.output.write('\n')
        if tag == 'meta':
            for name, value in attrs:
                if name=='content':
                    self.output.write(value)
        if tag == 'script':
            self.var=1
            
    def handle_data(self, data):
        if self.var == 0:
            self.output.write(data)
            
    def handle_endtag(self, tag):
        if tag == 'p':
            self.output.write('\n')
        if tag == 'script':
            self.var=0

def get_page_text(page):
        html=get_page(page)
        p = HTML2Text()
        p.feed(html)
        text = p.get_text()
        raw_list = text.splitlines()
        new_list = []
        for line in raw_list:
                line = line.strip()
                if line != '':
                        line = line + '\n'
                        new_list.append(line)
        clean_text = "".join(new_list)
        
        file_name=page[7:].replace('/','-')
        
        f=open(file_name+'.txt',"w")
        f.write(clean_text)
        f.close()

        
def get_next_target(page):
        start_link=page.find('<a href=')
        if start_link==-1:
                return None,0
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url,end_quote

def print_all_links(page):
        while True:
                url, endpos=get_next_target(page)
                if url:
                        print url
                        page=page[endpos:]
                else:
                        break

def get_page(url):
        try:                                
                return urllib2.urlopen(url).read()
        except:
                print url
                print "ERROR GETTING THE PAGE"
                return 

def get_all_links(page):
        links=[]        
        for link in soup.find_all('a'):
            link=unicode(link.get('href'))
            if link.find("http://www.")== -1 or link.find("http://") == -1:
                link=page+'/'+link
            links.append(link)
        return links

def union(p,q):
        for e in q:
                if e not in p:
                        p.append(e)
                        

def crawl_web(seed):
        tocrawl=[seed]
        crawled=[]
        #index={}
        graph={}
        while tocrawl: #and len(crawled)<12:
            f_crawled=open("crawled.txt","a+")
            page=tocrawl[0]
            
            tocrawl=tocrawl[1:]
            if page not in crawled:
                outlinks=get_all_links(page)                
                union(tocrawl,outlinks)
                graph[page]=outlinks
                get_page_text(page)
                crawled.append(page)
                f_crawled.write(page+"\n")
                f_crawled.close()
                #print "tocrawl"
                #print tocrawl
        return graph
page="http://www.innovaccer.com/"
content=get_page(page)
soup=BeautifulSoup(content)
graph=crawl_web(page)

