import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ABS_PERCENT = 5

# For Alpha Vantage
AV_API_KEY = "U0TL1N899AZIY85U"
AV_API_ENDPOINT = "https://www.alphavantage.co/query"

# for News API
NEWS_API_KEY = "bd39a3d5f66641708b2971ac8eb10779"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

# For Twilio API
SENDER = "+12565768232"
RECEIVER = "+639162143943"
account_sid = "ACd465ad963b49b777dea265b84e6f80ac"
auth_token = "e9c55a38f5a5c102a152807ad89bf442"


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_percent_change() -> float:
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": STOCK,
        "apikey": AV_API_KEY,
    }

    response = requests.get(url=AV_API_ENDPOINT, params=params)
    response.raise_for_status()
    return float(response.json()["Global Quote"]["10. change percent"].strip("%"))


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news() -> list:
    params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "pageSize": 3
    }

    response = requests.get(url=NEWS_API_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()["articles"]


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
# Optional: Format the SMS message like this:
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
# file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st,
# near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to
# file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height
# of the coronavirus market crash.
# """
def send_text(news_articles: list, percent: float):
    if percent >= 0:
        abs_percent = percent
        sign = "🔺"
    else:
        abs_percent = -1 * percent
        sign = "🔻"

    formatted_message = f"{STOCK}: {sign}{abs_percent}\n"

    for article in news_articles:
        formatted_message += f"Headline: {article['title']} ({STOCK})?.\n" \
                             f"Brief: {article['description']}\n"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=formatted_message,
        from_=SENDER,
        to=RECEIVER
    )
    print(message.status)


# MAIN
change_percent = get_percent_change()

# # for checking purposes
# print("vv Checking begins below: ")
# print(change_percent)
# articles = get_news()
# print(articles)
# send_text(articles, change_percent)
# print("^^ For checking of functionality only\n")

if (change_percent >= ABS_PERCENT) or (change_percent <= -ABS_PERCENT):
    articles = get_news()
    print(articles)
    send_text(articles, change_percent)
else:
    print("No significant change in stock value.")
