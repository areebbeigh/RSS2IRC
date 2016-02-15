# Python RSS2IRC Bot
This is a simple IRC bot that'll return feeds from an RSS source to an IRC channel.
I've used <a href="https://github.com/maK-/rss2irc-bot" target="_blank">this rss2irc</a> bot features for the basic functionality and made many additions,
bug fixes and improvisations.
<hr>
## Configuration
To configure the bot open rss2irc.py with any text editor, scroll down to the config part and replace the default info with the desired one.
Description for each feild is marked after the "#" hastag.
<hr>
## Commands
<table width="50%">
<td>Command</td>
<td>Description</td>
<tr>
<td>!feed</td><td>Returns last 3 feeds</td>
</tr>
<tr>
<td>!feed last (1-4)</td><td>Returns last 'n' number of feeds</td>
</tr>
<tr>
<td>!feed list</td><td>Returns the feed list currently being used</td>
</tr>
<tr>
<td>!credits</td><td>View bot credits</td>
</tr>
<tr>
<td>!feed help</td><td>View this help dialogue</td>
</tr>
</table>
<hr>
## Possible Snags
##### 1. Bot is not joining the channel
Once the script is started the bot will take sometime to login and join the channel (minimum 40 seconds),
yet it depends on the latency. You can do a /whois <bot nick> to check if the bot has at least connected to the network.
If it does not join try restarting the script.

##### 2. No feeds
Check if the URL you provided is working and it is an RSS feed. 
<a href="http://www.irchound.tk/forum/syndication.php?fid=2,14,18,4,5,11,17,6,21,23,24,22&limit=5" target="_blank">
here's what an RSS page looks like
</a>.

##### 3. Bot is not logging in
This bot uses NickServ to login and which will happen only if the nick name it uses is regsitered. Make sure
the nickname is registered and the password you have entered is correct. If it still does not work the network you're connecting to
probably does not use NickServ.

##### 4. Bugs
If you find any bugs / miss typed stuff in the code please feel free to make a pull request / open an issue on this repo.
You can also contact me <a href="http://www.areeb-beigh.tk/contact.html" target="_blank">here</a>

Cheers!
<hr>
**Developer**: Areeb Beigh (M4Shooter)<br>
**Website**: <a href="www.areeb-beigh.tk" target="_blank">www.areeb-beigh.tk</a><br>
**Mail:** areebbeigh@gmail.com<br>
**Version**: 2.0
