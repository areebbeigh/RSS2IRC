# Python RSS2IRC Bot

This is a simple IRC bot that'll return feeds from an RSS source to 1 or more IRC channels.

<hr>

## Configuration

To configure the bot open `config/config.py` with any text editor and being with the configuration. All the details about
different fields are already included as comments in the file.

<hr>

## Commands

<table width="50%">
<td>Command</td>
<td>Description</td>
<tr>
<td>!feed</td><td>Returns last 3 feeds</td>
</tr>
<tr>
<td>!feed last (1-5)</td><td>Returns last 'n' number of feeds</td>
</tr>
<tr>
<td>!feed list</td><td>Returns the feed list currently being used</td>
</tr>
<tr>
<td>!feed help</td><td>View this help dialogue</td>
</tr>
<tr>
<td>!credits</td><td>View bot credits</td>
</tr>
</table>

<hr>

## Admin commands

<table>
<tr><td>!login</td><td>Uses NickServ to login with the bot password set in the config</td></tr>
<tr><td>!killsocket</td><td>Kills the bot connection</td></tr>
</table>

The bot can have only 1 admin. The admin is determined by the complete nick, ident and hostmask and hence, you need to configure this properly. You can look at the debug messages in the console while the bot is running to get your nick, ident
and hostmask string.

<hr>

## Possible Snags

### 1. Bot is not joining the channel

Check if the bot actually connected to the network by using /whois <bot_nick> or <bot_alt_nick> if the bot is not connected
then both the nick and alt_nick are occupied. If the bot is connected and yet it is not joining the channels then check the channel settings (ban masks, invite only, registered only etc.).

### 2. No feeds

Check if the URL you provided is working and it is a valid feed source. Here's what an RSS page looks like: https://github.com/areebbeigh.atom
</a>.

### 3. Bot is not logging in

This bot uses NickServ to login which will happen only if the nick name it uses is regsitered. Make sure
the nickname is registered and the password you have entered is correct. Also try the `!login` command and see if it identifies. If it still does not work the network you're connecting to probably does not use NickServ.

### 4. Bugs

If you find any bugs / miss typed stuff in the code please feel free to make a pull request / open an issue on this repo.
You can also contact me via areebbeigh@gmail.com

Cheers :coffee:
<hr>
**Developer**: Areeb Beigh <areebbeigh@gmail.com><br>
**Version**: 2.2<br>
**GitHub Repo:** https://github.com/areebbeigh/RSS2IRC
