# Telegram Bot for ReadWise

Telegram bot for https://readwise.io

## How to Run?

### Get Tokens

1. Get bot token from https://core.telegram.org/bots/features#botfather
2. Get Readwise API token from https://readwise.io/access_token
3. Set environment variables in `.env` file

### Option 1. Run using docker

* `docker-compose up -d`

### Option 2. Run local  
1. Install dependencies `pip install -r ./requirements.txt`
2. Run `python ./app.py`

## How It Works?

```mermaid
sequenceDiagram
    User->>+TelegramBot: Forwards post to highlight it
    TelegramBot->>+ReadWise API: Using ReadWise API token sends post text and link to the ReadWise
    TelegramBot-->>-User: Responses "Message from channel was highlighted"
```

## Features

Forward post from someone or some channel in Telegram and this bot will send text and link to ReadWise Reader.

## What are the Differences in the Forked Repository?

- Removed support for Readwise highlights. The default behavior now is to send posts to Readwise Reader.
- Improved the quality of the HTML page from the Telegram post. The Readwise parser now creates more readable pages.