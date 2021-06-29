import requests
from twilio.rest import Client
Stock_Name="TSLA"
Company_Name="Tesla Inc"

Stock_Endpoint="https://www.alphavantage.co/query"
News_Endpoint="https://newsapi.org/v2/everything"
api_key='NW9ZV0GZ39HHDFR6'
News_apikey="2d1df8b60aa14f489aaf62e6b8297a95"
Twilio_SID="ACb6fe9237d880a6650a2da97859e531c3"
Twilio_Auth="ab6a6a02753f5f0f4e3ca873e0d8274b"
stock_params={
    "function":"TIME_SERIES_DAILY",
    "symbol":Stock_Name,
    "apikey":api_key,
}

#task1
response=requests.get(Stock_Endpoint,params=stock_params)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
print(yesterday_closing_price)

#task2
dy_bfr_ytd_data=data_list[1]
dy_bfr_ytd_cls_pr=dy_bfr_ytd_data["4. close"]
print(dy_bfr_ytd_cls_pr)

#task3
difference= float(yesterday_closing_price)-float(dy_bfr_ytd_cls_pr)
up_down=None
if difference>0:
    up_down="🔺"
else:
    up_down="🔻"

#task4
diff_percent=round(difference/float(yesterday_closing_price)*100)
print(diff_percent)

#task5
if abs(diff_percent)>0:
    news_params={
        "apiKey":News_apikey,
        "qInTitle":Company_Name,

    }
news_response=requests.get(News_Endpoint,params=news_params)
articles=news_response.json()["articles"]
three_articles=articles[:3]
print(three_articles)
#task6
formatted_articles=[f"{Stock_Name}:{up_down}{diff_percent}% \nHeadline:{article['title']}. \nBrief: {article['description']}" for article in three_articles]

client=Client(Twilio_SID,Twilio_Auth)
for article in formatted_articles:
    message=client.messages.create(
        body=article,
        from_=+12187369402,
        to=+919004659899
    )
