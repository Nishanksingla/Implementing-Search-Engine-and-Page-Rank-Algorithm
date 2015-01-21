def make_index():
        index={}
        f_crawled=open("crawled.txt","r")
        #print f_crawled.readlines()
        for line in f_crawled.readlines():
                line=line.replace('\n','')
                url=line
                line=line[7:]
                line=line.replace('/','-')
                line=line+'.txt'
                f_file=open(line,"r")
                content=f_file.read()
                
                words=content.split()
                for word in words:
                        add_to_index(index,word,url)

        return index


def add_to_index(index,keyword,url):
        if keyword in index:
                if url not in index[keyword]:
                        index[keyword].append(url)
        else:
                index[keyword]=[url]   

def lookup(index,keyword):
        if keyword in index:
                return index[keyword]
        else:
                return None


index=make_index()
print index

