//
//  hackathon.cpp
//  
//
//  Created by Bryce Jacobson on 9/16/17.
//
//

import unirest

# These code snippets use an open-source library. http://unirest.io/python
response = unirest.get("https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous&count=10",
                       headers={
                       "X-Mashape-Key": "OARcormYCrmshEmzSssSO4CZu8bSp1VTwajjsnkE0TeVKx7kxv",
                       "Accept": "application/json"
                       }
                       )

print(response)
