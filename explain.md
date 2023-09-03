# Step-by-step explanation

## Import necessary libraries

     Including "requests" for making HTTP requests, "random" for random selection, os for environment variables, and the Discord-related libraries.

## Import the Discord token (DISCORD_TOKEN) and News API key (NEWS_API_KEY)
    
     From an external file named keys.py, these keys are used to authenticate and access the Discord API and News API, respectively.

## Configure Discord "intents"

    Used to specify which events the bot should be aware of.

## Create an instance of a Discord bot 

    (client) with a command prefix (!) and the configured intents.

## Define an event handler

    Used for when the bot is ready (on_ready). This event is triggered when the bot successfully logs in and is ready to respond to commands.

## Define a custom command

    The command called News, this command fetches a random news article from TechCrunch using the News API and sends the article's title, description, and URL to the Discord channel where the command was invoked.

## Inside the News command function, the code performs the following steps:

- Constructs the URL to fetch news data from the News API using the provided API key.
- Sends a GET request to the API and parses the JSON response.
- Checks if the response status code is 200 (indicating a successful request).
- Randomly selects one article from the list of articles in the response.
- Extracts information (title, description, and URL) from the selected article.
- Sends a message to the Discord channel with the article details or an error message if the request fails or encounters an exception.
- Prints the Discord token to the console for debugging purposes.

- Starts the Discord bot (client.run(discord_token)) using the specified Discord token to authenticate and connect the bot to the Discord servers.

This code creates a Discord bot that can respond to the !News command by fetching and sharing a random news article from TechCrunch.