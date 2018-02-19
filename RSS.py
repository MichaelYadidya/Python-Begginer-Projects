import feedparser

url = input('Enter the RSS feed url: ')

feeds = feedparser.parse(url)

for feed in feeds['entries']:
    print('title')