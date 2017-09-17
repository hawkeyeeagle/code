from pprint import pprint
import unirest
import twitter
import tweepy

# These code snippets use an open-source library. http://unirest.io/python
get = unirest.get("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=1",
                  headers={
                  "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                  "Accept": "application/json"
                  }
                  )
# These code snippets use an open-source library. http://unirest.io/python
fq1 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )
fq2 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )
fq3 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )
fq4 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )
fq5 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )
mq1 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )
mq2 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )
mq3 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )
mq4 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )
mq5 = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies&count=10",
                   headers={
                   "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "application/json"
                   }
                   )

#TWITTER STUFF

api = twitter.Api(consumer_key='6cHfiyCxaLrmYyGmnbhDCirdH',
                  consumer_secret='c9OyqSxfzg4hSABbvzjOA4yJryB0vXr3dP5LFwT75bAekf00TE',
                  access_token_key='464149988-3OKqzWGvv4LcGHn0bRyhNRPGjtwDq8jgHrVHDLwa',
                  access_token_secret='lZzv9bptAneZRRazjoWN4sXuOXqDhgKtxda3mBMVKgTLq')



def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

url = str(raw_input("what is the url for the tweet?"))
urlText = url.split('/')

reply = urlText[3]
replyID = urlText[5]
keyword = str (raw_input("Your keyword please: "))



y=0
x=0
quote = ""
while x==0:
    quote = fq1.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    quote = fq2.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    quote = fq3.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    quote = fq4.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    quote = fq5.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    quote = mq1.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    quote = mq2.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    quote = mq3.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    quote = mq4.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    quote = mq5.body[y]
    q = str (quote['quote'])
    a = str (quote['author'])
    test = str(q+ "  " + a)
    if keyword in q:
        qTweet = str ("@" + reply + " "+q + \
                      "  -"+ a)
        x = 2
    y= y+1
    if y == 9:
        print "Error please try another keyword"
        x = 5




def main():
    # keys for connecting to account
    cfg = {
        "consumer_key"        : "6cHfiyCxaLrmYyGmnbhDCirdH",
        "consumer_secret"     : "c9OyqSxfzg4hSABbvzjOA4yJryB0vXr3dP5LFwT75bAekf00TE",
        "access_token"        : "464149988-3OKqzWGvv4LcGHn0bRyhNRPGjtwDq8jgHrVHDLwa",
        "access_token_secret" : "lZzv9bptAneZRRazjoWN4sXuOXqDhgKtxda3mBMVKgTLq"
    }
    api = get_api(cfg)
    if x == 2:
        if len(qTweet) <= 140:
            tweet = qTweet
            status = api.update_status(status=tweet, in_reply_to_status_id = replyID)
        else:
            print "tweet too long"

if __name__ == "__main__":
    main()
