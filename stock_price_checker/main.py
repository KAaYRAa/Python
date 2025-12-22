import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOK_API_KEY=""
NEWS_API_KEY=""
TWILIO_SID=''
TWILIO_AUTH_TOKEN=''
stok_param={
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOK_API_KEY,
}
response=requests.get(STOCK_ENDPOINT, params=stok_param)
data= response.json()["Time Series (Daily)"]
data_list=[values for (key, values) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)


difference=float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down=None
if difference>0:
    up_down="BUY"
else:
    up_down="SELL"

print(difference)


diff_procent=round((difference/float(yesterday_closing_price))*100,3)
print(diff_procent)

if abs(diff_procent )>1:
    news_param={
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,

    }
    new_response=requests.get(NEWS_ENDPOINT,params=news_param)
    article=new_response.json()["articles"]
    print(article)
    three_articles=article[:3]
    print(three_articles)

    formatted_articles = [
        f"Headline: {article['title']}\nBrief: {article['description']}"
        for article in three_articles
    ]

    client=Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message=client.messages.create(
            body=article,
            from_="+19786375487",
            to=''
        )




