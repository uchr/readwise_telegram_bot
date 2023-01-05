# Telegram Bot for ReadWise

Telegram bot for https://readwise.io

## How to Run?

```bash
python ./app.py
```

You can deploy this bot [anywhere](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Where-to-host-Telegram-Bots).
## How It Works?
```mermaid
sequenceDiagram
    User->>+TelegramBot: Forwards post to highlight it
    TelegramBot->>+ReadWise API: Using ReadWise API token sends post text and link to the ReadWise
    TelegramBot-->>-User: Responses "Message from channel was highlighted"
```

## Features

1. Forward post from someone or some channel in Telegram and this bot will send text and link (and the first link in the post itself) to ReadWise
2. If some commentary is provided to the message, it will be added to ReadWise as a note

## Security considerations

1. To make this bot work you have to provide to the bot ReadWise API token.
2. Because I don't want to store your tokens, you have to set up a separate bot for yourself.
3. From my perspective Telegram Bot API doesn't provide secure way to store sensitive data, that is why you have to [create your own bot](https://core.telegram.org/bots/features#botfather). 

