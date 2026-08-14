from openai import OpenAI
from dotenv import load_dotenv #use to access data from .env file for program to process
import os
import requests #this allows python to communincate with website/api over http

load_dotenv() # this finds the .env file and runs it



client = OpenAI(api_key = os.getenv("GROQ_API_KEY"), #it gives clinet access to our hidden.txt file which contains api key
                 base_url="https://api.groq.com/openai/v1") # this directs client to use opnerouter to respond rather than openAI

def weather_api(city):
    api_key = os.getenv("weather_api") #get the value from .env file 
    url = "https://api.openweathermap.org/data/2.5/weather" # it connects with openweather webiste

    parameters = {
        "q":city,
        "appid":api_key,
        "units":"metric"
    }
    response = requests.get(url,parameters=parameters) # this line contacts openweather using url and the parameters

    if response.status_code == 200:
        data = response.json()

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

        return weather

    else:
        return f"Could not get weather data: {response.status_code}"
    


messages = []
while True:
    user = input("YOU: ")

    if user.lower() =="exit":
        break

    messages.append({
        "role":"user",
        "content": user
        })

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages
    )

    bot = response.choices[0].message.content
    print("BOT:", bot)

    messages.append({
        "role":"assistant",
        "content": bot
    })


# List [] → keeps multiple messages in sequence/order.
# Dictionary {} → describes one message using key-value pairs.
# "role" → key telling the API who sent the message.
# "user" / "assistant" → values telling who sent it.
# "content" → key telling the API where the actual message is.
# The text → value containing what was actually said.