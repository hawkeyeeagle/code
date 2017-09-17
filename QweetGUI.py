from pprint import pprint
import unirest
import twitter
import tweepy
from Tkinter import *
import tkMessageBox
import Tkinter

root = Tkinter.Tk()
root.title("Qweet")
root.geometry("500x300")

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



keyword = ""
root.configure(background='#0084b4')
Lbl1 = Label(root, text="Input username here (ommit the @):")
Lbl1.pack(side=TOP,padx=5,pady=5)
Entry1 = Entry(root, bd =1)
Entry1.pack(side=TOP,padx=5,pady=5)
Lbl2 = Label(root, text="Input a tweet ID here:")
Lbl2.pack(side=TOP,padx=5,pady=5)
Entry2 = Entry(root, bd =1)
Entry2.pack(side=TOP,padx=5,pady=5)
Lbl3 = Label(root, text="Input a Keyword here:")
Lbl3.pack(side=TOP,padx=5,pady=5)
Entry3 = Entry(root, bd =1)
Entry3.pack(side=TOP,padx=5,pady=5)

def PrintCommand():
    z=8
    reply = str(Entry1.get())
    replyID = str(Entry2.get())
    keyword = str(Entry3.get())
    print reply
    print replyID
    print keyword
    if z == 8:
        z=3
        y=3
        x = 0
        compute(reply, replyID,keyword)

bttn1 = Tkinter.Button(root, text ="Tweet!", command = PrintCommand)
bttn1.pack(side = TOP,padx=10,pady=20)


def compute(reply, replyID, keyword):
    if keyword != "":
        print "whoopdie freaking do"
        
        y=0
        x=8
        z=3
        if y == 3:
            x=0
        # keys for connecting to account
        cfg = {
            "consumer_key"        : "6cHfiyCxaLrmYyGmnbhDCirdH",
            "consumer_secret"     : "c9OyqSxfzg4hSABbvzjOA4yJryB0vXr3dP5LFwT75bAekf00TE",
            "access_token"        : "464149988-3OKqzWGvv4LcGHn0bRyhNRPGjtwDq8jgHrVHDLwa",
            "access_token_secret" : "lZzv9bptAneZRRazjoWN4sXuOXqDhgKtxda3mBMVKgTLq"
        }
        if z == 3:
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
        api = get_api(cfg)
        if x == 2:
            print "you better work!"
            if len(qTweet) <= 140:
                tweet = qTweet
                status = api.update_status(status=tweet, in_reply_to_status_id = replyID)
            else:
                print "tweet too long"

#if __name__ == "__main__":
#    compute()
#    print keyword



root.mainloop()
