import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

EMAIL=config('EMAIL')
PASSWORD=config('PASSWORD')
NEWS_API_KEY=config('NEWS_API_KEY')
WEATHER_APP_ID=config('WEATHER_APP_ID')
IP_API_KEY=config('IP_API_KEY')

def find_my_ip():
    ip_address=requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def get_city():
    ip_address=find_my_ip()
    city=requests.get(f"https://api.ip2location.io/?key={IP_API_KEY}&ip={ip_address}").json()
    city=city['city_name']
    return city

def search_on_wikipedia(query):
    results=wikipedia.summary(query, sentences=3)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_whatsapp_message(number,message):
    kit.sendwhatmsg_instantly(f'+91{number}',message)

def send_email(receiver_address,subject,message):
    try:
        email=EmailMessage()
        email['To']=receiver_address
        email['Subject']=subject
        email['From']=EMAIL
        email.set_content(message)
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(EMAIL,PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
    
def get_latest_news():
    news_headlines=[]
    res=requests.get(f"https://saurav.tech/NewsAPI/top-headlines/category/general/in.json").json()
    articles=res['articles']
    for articles in articles:
        news_headlines.append(articles['title'])
    return news_headlines[:5]

def get_weather_report(city):
    res=requests.get(f"https://api.weatherapi.com/v1/current.json?key={WEATHER_APP_ID}&q={city}").json()
    weather=res['current']['condition']['text']
    temperature=res['current']['temp_c']
    feels_like=res['current']['feelslike_c']
    return weather,f"{temperature}℃",f"{feels_like}℃"

def get_random_joke():
    headers={'Accept': 'application/json'}
    res=requests.get("https://icanhazdadjoke.com/",headers=headers).json()
    return res['joke']

def get_random_advice():
    res=requests.get('https://api.adviceslip.com/advice').json()
    return res['slip']['advice']
    

