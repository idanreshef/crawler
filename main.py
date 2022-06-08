from collections import deque
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.request import urlopen

start_url = "https://www.geeksforgeeks.org/recursion/"

queue = deque([])

# Maintains list of visited pages
visited_list = []


# Crawl the page and populate the queue with newly found URLs
def crawl(url):
    visited_list.append(url)
    if len(queue) > 99:
        return

    urlf = urlopen(url)
    soup = BeautifulSoup(urlf.read())
    urls = soup.findAll("a", href=True)

    for i in urls:
        flag = 0
        # Complete relative URLs and strip trailing slash
        complete_url = urljoin(url, i["href"]).rstrip('/')

        # Check if the URL already exists in the queue
        for j in queue:
            if j == complete_url:
                flag = 1
                break

        # If not found in queue
        if flag == 0:
            if len(queue) > 99:
                return
            if (visited_list.count(complete_url)) == 0:
                queue.append(complete_url)

    # Pop one URL from the queue from the left side so that it can be crawled
    current = queue.popleft()
    # Recursive call to crawl until the queue is populated with 100 URLs
    crawl(current)


crawl(start_url)

# Print queue
for u in queue:
    print(u)

# Print list of visited pages
for v in visited_list:
    print(v)
