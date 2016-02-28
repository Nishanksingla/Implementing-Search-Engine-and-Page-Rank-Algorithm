## Implementing Search Engine and Page Rank Algorithm Using Python
This is my undergrad final year project. 
A prototype of search eninge to understand the components of search eninge and how it works.

Search Engine has 3 parts:

1. Indexer
2. Crawler
3. Query Processor

######Crawler

A crawler crawls the web page, fetch the contens and links in the page and stores them. 
The developer of a website can define a file called Robot.txt that defines how frequently a crawler is allowed to crawl and 
which web pages it is allowed to crawl.

######Indexer

Indexes the content of web page fetched by crawler. It also filters important words to be indexed out of the content.

######Query Processor

This program basically processes the query entered by the user, fetches the indexes of the query, calculate the page rank, sort them and 
then displays the result. This is just simple explanantion of query processor but it includes a lot more than this like making sense of 
the query and give suggestions by using Machine Learning algorrithms.

All these 3 programs are almost same in each search engine whether it is Microsoft Bing or yahoo or google search engine. They all differ
in their implementation of Ranking algorithm. 
Page Rank algorithm is google's patented algorithm.


