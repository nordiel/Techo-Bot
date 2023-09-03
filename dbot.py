import requests
import random

import discord
from discord.ext import commands

from keys import DISCORD_TOKEN
from keys import NEWS_API_KEY

discord_token = DISCORD_TOKEN
news_key = NEWS_API_KEY

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    
    print("Techo is up and running! ^_^")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("API: NewsAPI")
    print("Project: Tech News Discord Bot")

@client.command()
async def News(ctx):
    
    try:
        
        main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" + news_key
        response = requests.get(main_url)
        news_data = response.json()

        if response.status_code == 200:
            articles = news_data["articles"]
            
            random_article = random.choice(articles)

            title = random_article['title']
            description = random_article.get('description', 'No description available')
            url = random_article.get('url', 'No URL available')

            await ctx.send(f"Here is one of the top news articles from TechCrunch:\n\n Title: {title}\n\n{description}\n\n Read here: {url}")
            
        else:
            await ctx.send("Failed to fetch news. Please try again later.")
            
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

print(f"Discord Token: {discord_token}")

client.run(discord_token)