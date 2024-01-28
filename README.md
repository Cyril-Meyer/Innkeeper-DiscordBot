# Innkeeper-DiscordBot
Greeting and Chat Discord Bot

### Usage
* Create a `token.txt` file and place your Discord bot token inside.
  * you can also use the `--token` parameter instead.
* Create `config.json` file and `chatbot.json` like examples in [configuration section](#configuration).

```
usage: main.py [-h] [--token TOKEN] [--command-prefix COMMAND_PREFIX]
               [--print-guilds-info]

optional arguments:
  -h, --help            show this help message and exit
  --token TOKEN         discord token
  --command-prefix COMMAND_PREFIX
                        command prefix
  --print-guilds-info
```

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

**run with docker**
```
# build
docker build -t innkeeperdiscordbot .
# run
docker run --rm -it -d -v $(pwd):/usr/src/app --name innkeeperdiscordbot-container innkeeperdiscordbot python main.py
# logs
docker logs -f innkeeperdiscordbot-container
# kill
docker attach innkeeperdiscordbot-container
- CTRL+C -
```

#### Configuration

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
* `hello` is also message for member join.
```
{
  "hello": "Hello !",
  "helpme": "Is this helping ?"
}
```
