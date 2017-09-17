
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
post = unirest.post("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=10",
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

reply = "@"
OGtweet = "I am a little teapot short and stout"
text = get._raw_body
text = text.split('"')
full = post.body[0]
quote = str(full['quote'])
author = str(full['author'])
replyID = 899457000618295297
qTweet = ""
keyword = "world"
reply = str (raw_input("Who would you like to tweet at:  @"))
replyID = str (raw_input("TweetID you want to reply too: "))
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
        qTweet = str ("@" + reply + " "+quote + \
                      "  -"+ author)
    if y == 10:
        print "Sorry your keyword is not found please try again"
        x=3

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

if __name__ == "__main__":
    main()





