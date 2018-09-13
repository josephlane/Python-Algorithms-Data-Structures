from bs4 import BeautifulSoup
import sys
import time
import urllib2

class WebCrawler(object):
    
    __slots__ = ["index", "graph", "ranks"]

    def __init__(self):
        self.index = {}
        self.graph = {}
        self.ranks = {}

    def add_to_index(self, keyword, url):
        if keyword in self.index:
            self.index[keyword].append(url)
            return
        self.index[keyword] = [url]
    
    def add_page_to_index(self, url, content):
        words = content.split()
        for word in words:
            self.add_to_index(word, url)
    
    def lookup(self, keyword):
        if keyword in self.index:
            return self.index[keyword]
        return []
    
    def get_next_url(self, html):
        start_tag = html.find("<a href=")
        if start_tag == -1:
            return None, 0
        start_quote = html.find('"', start_tag)
        end_quote = html.find('"', start_quote+1)
        url = html[start_quote+1: end_quote]
        return url, end_quote
    
    def get_page_html(self, url):
        try:
            return urllib2.urlopen(url).read()
        except:
            return ""
            
    def crawl(self, start_url, page_html):
        html = page_html
        links = []
    
        while len(html) > 0:
           # print "Length of html: {0}".format(len(html))
            url,pos = self.get_next_url(html) 
            if pos:
                if url.find("http") != -1:
                    links.append(url)
                   # print url
                html = html[pos:].strip()
                time.sleep(1)
            else:
                break
            
        return links
    
    def compute_ranks(self):
        DAMPING_FACTOR = 0.8
        NUMBER_OF_LOOPS = 10
        
        npages = len(self.graph)
        for page in self.graph:
            self.ranks[page] = 1.0 / npages
        for i in range(0, NUMBER_OF_LOOPS):
            new_ranks = {}
            for node in self.graph:
                new_rank = (1 - DAMPING_FACTOR) / npages
                if page in self.graph[node]:
                    new_rank = new_rank + DAMPING_FACTOR * (self.graph[node] /
                            len(self.graph))
                new_ranks[node] = new_rank
            self.ranks = new_ranks
    def initialize_crawl(self, url):
        to_crawl = [url]
        crawled = []
        for link in to_crawl:
            if link not in crawled:
                page_html = self.get_page_html(link)
                page_text = BeautifulSoup(page_html, 'html.parser')
                para_text = page_text.find_all('p')
                para_text = [m.contents[0] for m in para_text]
                para_text = " ".join(para_text)
                self.add_page_to_index(link, para_text)
                print "Now Crawling: {0}".format(link)
                new_links = self.crawl(url, page_html)
                self.graph[link] = new_links
                to_crawl += set(new_links) - set(to_crawl)
                crawled.append(link)
                print "Number of Links Crawled: {0}".format(len(crawled))
                print "Number of Links To Be Crawled: {0}".format(len(to_crawl))
            break
        print "Crawl Complete" 
    
if __name__ == "__main__":
    url = sys.argv[1]
    w = WebCrawler()
    w.initialize_crawl(url)

