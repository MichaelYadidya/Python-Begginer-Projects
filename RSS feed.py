import feedparser

url = input('Enter the URL of the RSS feed page: ')

feeds = feedparser.parse(url)

for feed in feeds['entries']:
    print(feed['title'])

