def lookup(index,keyword):
        if keyword in index:
            return index[keyword]
        else:
            return None

def Look_up_new(index,ranks,keyword):
	pages=lookup(index,keyword)
	for i in pages:
		print i+" --> "+str(ranks[i])
	QuickSort(pages,ranks)
	print "\nAfter Sorting the results by page rank\n"
	for i in pages:
		print i 

def QuickSort(pages,ranks):
	if len(pages)>1:
		piv=ranks[pages[0]]
		i=1
		j=1
		for j in range(1,len(pages)):
			if ranks[pages[j]]>piv:
				pages[i],pages[j]=pages[j],pages[i]
				i+=1
		pages[i-1],pages[0]=pages[0],pages[i-1]
		QuickSort(pages[1:i],ranks)
		QuickSort(pages[i+1:len(pages)],ranks)

def compute_ranks(graph):
	d=0.8
	numloops=10
	ranks={}
	npages=len(graph)
	print 'checkpoint 1'
	for page in graph:
		ranks[page]=1.0/npages
	for i in range(0,numloops):
		newranks={}
		for page in graph:
			newrank=(1-d)/npages
			for node in graph:
				if page in graph[node]:
					newrank=newrank+d*ranks[node]/len(graph[node])
			newranks[page]=newrank
		ranks=newranks
	return ranks


ranks=compute_ranks(graph)
Look_up_new(index,ranks,"is")

