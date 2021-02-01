# ⚔️ Hunter's Guild Bot ⚔️
I made a bot for friends to use in a Discord channel where we talk about video games(mostly Monster Hunter). Guildbot can tell a random joke, as well as announce the intent to HUNT!
## Technologies Used
Python, Flask, Uptime Robot
## Instructions
### Accepted Commands
Below are the phrases currently recognized by the bot:

`!guildbot wake up` - Bot will awaken, and respond to things like:

* `!joke` - Bot will tell a random joke in channel
* `LET'S HUNT!` - Bot will announce the intent to hunt with a random message and mention the auhor in channel
* `!new + <whatever you want to say 😁 >` - Create a custom phrase to trigger the intent to hunt and random message! Bot will remember this message, so choose wisely...

`!guildbot + <literally anything that's not "wake up">` - Bot will "sleep" and no longer respond to commands above, except the "wake up" command

## Next Steps
- Repair bot's sleep status; at the moment the bot likes to say that it's not responding if you mention it while it's sleeping...
- Allow users to edit the list of custom phrases!
- When the new game comes out, allow users to share Room ID and Password from game session(TBA)
## Credits
Written by: ME(Kamali Means), with the help of [freeCodeCamp](https://www.freecodecamp.org/)

API for bot's jokes: [icanhazdadjoke](https://icanhazdadjoke.com/api)

[UptimeRobot](https://uptimerobot.com/) used to continuously ping this bot hosted in [the cloud](https://repl.it/)