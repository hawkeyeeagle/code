
from pprint import pprint
import unirest

# These code snippets use an open-source library. http://unirest.io/python
get = unirest.get("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=1",
                       headers={
                       "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                       "Accept": "application/json"
                       }
                       )
# These code snippets use an open-source library. http://unirest.io/python
post = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=10",
                        headers={
                        "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                        "Content-Type": "application/x-www-form-urlencoded",
                        "Accept": "application/json"
                        }
                        )
text = get._raw_body
text = text.split('"')
full = post.body[0]
quote = str(full['quote'])
author = str(full['author'])
keyword = "world"
keyword = str (raw_input("Your hashtag plz:"))
x=0
y=0
while x == 0:
    full = post.body[y]
    quote = str(full['quote'])
    author = str(full['author'])
    checker = keyword in quote
    y = y+1
    if checker == True:
        print quote
        print author
        print y
        x=2
    if y == 10:
        print "Sorry your keyword is not found please try again"
        x=2
