import snscrape.modules.twitter as sntwitter
import pandas as pd
import sys

tweets = []
limit = 1000

query = ""

print(query)

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.user.id, tweet.user.created, tweet.rawContent, tweet.retweetCount,
                       tweet.likeCount, tweet.replyCount, tweet.lang, tweet.user.location, tweet.user.followersCount, str(tweet.id)])

df = pd.DataFrame(tweets, columns=['Date', 'User', 'UserID', 'Fecha de creacion del usuario', 'Tweet', "RTs", "Favoritos", "Citados",
                                   "Idioma", "Ubicacion", "Followers del usuario", "Link"])

df["Link"] = "https://twitter.com/twitter/statuses/" + df["Link"]
df = df.sort_values(by=['RTs'], ascending=False)

df['Date'] = df['Date'].dt.tz_localize(None)
df['Fecha de creacion del usuario'] = df['Fecha de creacion del usuario'].dt.tz_localize(None)


# to csv
df.to_excel('tweets.xlsx', index=False, header=True)