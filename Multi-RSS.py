import feedparser

RSS_URLS = [ 'http://feeds.feedburner.com/RockPaperShotgun',
    'http://www.gameinformer.com/b/MainFeed.aspx?Tags=preview',]

feeds = []

posts = []
for url in RSS_URLS:
    posts.extend(feedparser.parse(url).entries)

for post in posts:
    print (post.title)