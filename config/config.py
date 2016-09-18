""" RSS2IRC Bot Configuration File """

# DO NOT REMOVE ANY BRACKETS, QUOTES etc, just replace the default values

# Feed Resources: The feed resources (usually URLs to XML feeds) go here
feed_resources = {
    "https://github.com/areeb-beigh.atom"
}

# IRC Stuff
NET = 'irc.freenode.net'                   # The network to connect to
PORT = 6667                                # Server port (default = 6667)
NICK = "RSS2IRC"                           # Bot's nickname
ALT_NICK = "RSS2IRC_"                      # Bot's alternate nickname
IDENT = "Areeb"                            # You might wanna enter your name here
REALNAME = "RSS2IRC Bot by Areeb - github.io/areeb-beigh"  # Keep my name in there? Thanks :)
CHANNELS = ["#rss2irc", "#lobby"]          # The channels the bot will join and work
PASSWORD = "rss2ircisawsm"                 # (Optional) The bot's account PASSWORD, works only with NickServ
REFRESH_RATE = 5                           # Checks for new feed_manager after every n seconds
# *BEEP* Important config *BEEP*
ENABLE_KILL_SOCKET = False                 # If 'True' then !killsocket command is made available
# Replace this with your <:NICK>!<IDENT>@<HOSTMASK> to use !killsocket (kills the bot connection)
ADMIN = ":Areeb!~Areeb@this.is.a.vhost"    # You can leave this part if ENABLE_KILL_SOCKET is False

