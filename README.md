# Discord.py bot with slash command and context menu

### Pre-Setup

If you don't already have a discord bot, click [here](https://discordapp.com/developers/), accept any prompts then click "New Application" at the top right of the screen.  Enter the name of your bot then click accept.  Click on Bot from the panel from the left, then click "Add Bot."  When the prompt appears, click "Yes, do it!" 
![Left panel](https://i.imgur.com/hECJYWK.png)

Then, click copy under token to get your bot's token. Your bot's icon can also be changed by uploading an image.

![Bot token area](https://i.imgur.com/da0ktMC.png)

### Setup

In replit Secrets, add `token=<your bot token>`

After adding your bot token to your replit Secrets, hit start everything should startup fine.

### Uptime

So now, all you have to do to keep your bot up is setup something to ping the site your bot made every 5 minutes or so.

Go to [betteruptime.com](https://betteruptime.com/) and create an accout if you dont have one.  After verifying your account, click "Create monitor".

+ For Monitor Type select "HTTP(s)"
+ In Friendly Name put the name of your bot
+ For your url, put the url of the website made for your repl.
+ Select any alert contacts you want, then click "Create Monitor" 

If you have running personal server, consider [uptime-kuma](https://github.com/louislam/uptime-kuma) as alternative.

Your bot should now be good to go, with near 100% uptime.



