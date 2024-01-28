# Innkeeper-DiscordBot
Greeting and Chat Discord Bot

### Usage

**setup venv and install dependency**
```
python -m venv venv
# windows
.\venv\Scripts\activate.bat
pip install -U pip
pip install discord.py==1.7.3
```

Be sure to have given all rights to your bot, including:
![image](https://github.com/Cyril-Meyer/Innkeeper-DiscordBot/assets/69190238/e09cd42f-cdd8-4fff-acc9-9a015ecde342)


**config.json**
```
{
  "bots": [
    {
      "guildid": 4242123456798,
      "channelid": 4242987654321,
      "chatbot": "chatbot1.json"
    },
    {
      "guildid": 1234567984242,
      "channelid": 9876543214242,
      "chatbot": "chatbot2.json"
    }
  ]
}
```

**chatbot.json**
```
{
  "hello": "Hello !",
  "helpme": "Is this helping ?"
}
```
