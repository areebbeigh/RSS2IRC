#!/usr/bin/python
# -*- coding: utf-8 -*-
# Thank you for using RSS2IRC ^_^!

# :Areeb!Areeb@oper.irchound.tk PRIVMSG #lobby :!credits
# Above is a reference to how the bot sees messages, you'll need to understand this if you want to add custom commands

import socket, string, feedparser, os, time, sys
from threading import Timer

# List of RSS feed URLs the bot will be reading
feedList = ["http://www.irchound.tk/forum/syndication.php?fid=2,14,18,4,5,11,17,6,21,23,24,22&limit=5"]
# Stores feed data
feedData = []
feedHasBeen = []

# Print some stuff
header = """
-------------------------------------------------
 RSS2IRC Bot by - Areeb Beigh - www.areeb-beigh.tk
-------------------------------------------------
"""
print header

#######

# Bot configuration starts here
net = 'irc.irchound.tk'									# The network to connect to
port = 6667												# Server port (default = 6667)
nick = "RSS2IRC"										# Bot's nickname
ident = "Areeb"											# You might wanna enter your name here
real = "RSS2IRC Bot by Areeb - www.areeb-beigh.tk"		# Optional
defaultChannel = "#lobby"								# The channel the bot will join and work
password = "PASSWORD"									# The bot's account password if it's registered (Works with NickServ)
refreshRate = 60										# Checks for new feeds after every n seconds
# Bot configuration ends here

#######

#### Danger ahead, please edit only if you know what you're doing! ####

if defaultChannel[0] != '#':
	defaultChannel = '#'+defaultChannel

# Assign some global variables
def initiate():
	global readbuffer, m
	readbuffer = ''
	m = ''
	print "Assigned global variables..."

initiate()

# Let's connect the bot
print "\nConnecting to %s..." % net
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((net,port))
s.send('USER '+ident+' '+net+' bla :'+real+'\r\n')
s.send('NICK '+nick+'\r\n')

# Function to send a message to the defaultChannel
def msg(defaultChannel, msg):
	s.send('PRIVMSG '+str(defaultChannel)+' :'+str(msg)+'\r\n')
	
# Fetches the latest feed
def feed_refresh():
	print "\nRefreshing feed list..."
	firstTime = False
	if len(feedData) == 0:
		firstTime = True
 	for feed in feedList:
  		f = feedparser.parse(feed)
  		for entry in f.entries:
			m = "4"+entry.title.encode('utf-8')+ " | "+"12"+entry.link.encode('utf-8')
			if m in feedData:
				firstTime = False
			else:
				time.sleep(1)
				msg(defaultChannel, m)
				feedData.append(m)

# Return the latest feed (depends on n which by default is 1 max value for n is 4 - You can edit this) 
def last_feed(n=1):
	maxFeed = 4		# Maximum number of feeds user can request
	if n > maxFeed or n < 1:
		msg(defaultChannel, 'Error: Can send only maximum %s feeds and minimum 1' % maxFeed)
	else:
		try:
			for feed in feedList:
				f = feedparser.parse(feed)
				for x in range(0,n):
					m = "4"+f.entries[x].title.encode('utf-8')+" | "+"12"+f.entries[x].link.encode('utf-8')
					msg(defaultChannel, m)
		except IndexError:							# Sends an error message instead of letting the bot crash
			msg(defaultChannel, 'No more feeds')	# due to IndexError if there are less or no feeds

# Iterate over the feedList and return results to defaultChannel
def feed_list():
    for feed in feedList:
        time.sleep(1)
        msg(defaultChannel,feed)

# Checks for feeds every 60 seconds
def update():
	x = Timer(refreshRate, update)
	x.daemon=True
	x.start()
	feed_refresh()

update()

# Login with NickServ
def identify():
	print "\nLogging in with NickServ in 10 seconds"
	time.sleep(10.0)
	s.send('PRIVMSG NickServ :IDENTIFY '+str(password)+'\r\n')
	
identify()
		
# Let's join a channel
def join_channel(channel):
	print "\nJoining %s in 10 seconds" % defaultChannel
	time.sleep(10.0)
	s.send('JOIN '+defaultChannel+'\r\n') 									# Join the defaultChannel
	msg(defaultChannel, "%s Now Online - Checking latest feed - !feed help to view commands" % nick) 	# Message stuff to channel
	last_feed(1)

# Joins the channel given in "defaultChannel"
join_channel(defaultChannel)

# Interacting with the IRC server events		
while(True):
	readbuffer=readbuffer+s.recv(4096)
	temp=string.split(readbuffer, "\n")
	readbuffer=temp.pop()
	for line in temp:
		line=string.rstrip(line)
		line=string.split(line)
		
	if(line[0]=='PING'):
		s.send('PONG '+line[1]+'\r\n')
	
	# Responses to different commands start here
	if(len(line)==4)and(line[2]==defaultChannel)and(line[3]==':!feed'):
		msg(defaultChannel, "3Last three feeds:")
		last_feed(3)
			
	if(len(line)==6)and(line[2]==defaultChannel)and(line[3]==':!feed')and(line[4]=='last'):
		try:
			last_feed(int(line[5]))
		except ValueError:
			msg(defaultChannel, 'Error: Invalid parameters')
			
	if(len(line)==5)and(line[2]==defaultChannel)and(line[3]==':!feed')and(line[4]=='list'):
		msg(defaultChannel, '3Feed list:')
		feed_list()
	
	if(len(line)==5)and(line[2]==defaultChannel)and(line[3]==':!feed')and(line[4]=='help'):
		msg(defaultChannel, '3Commands:')
		msg(defaultChannel, '4!feed             -   13Returns last 3 feeds')
		msg(defaultChannel, '4!feed last (1-4)  -   13Returns last \'n\' number of feeds')
		msg(defaultChannel, '4!feed list        -   13Returns the feed list currently being used')
		msg(defaultChannel, '4!credits          -   13View bot credits')
		msg(defaultChannel, '4!feed help        -   13View this help dialogue')
			
	if(len(line)==4)and(line[2]==defaultChannel)and(line[3]==':!credits'):
		msg(defaultChannel, '3Python RSS2IRC Bot v2.0 by Areeb')
		msg(defaultChannel, "4Based On         -  McNally's 12 https://github.com/maK-/rss2irc-bot")
		msg(defaultChannel, "4RSS2IRC v2.0 by  -  Areeb 12 https://github.com/areeb-beigh/RSS2IRC")
		
	# NOTE: This will disconnect the bot from the server and exit the program. Make sure you allow it to work only
	# 		with your nick, if you can't simply remove it / comment it out.
	# 		Replace Areeb!Areeb@oper.irchound.tk with your mask. Don't forget the ':'
	if(len(line)==4)and(line[0]==':Areeb!Areeb@oper.irchound.tk')and(line[2]==defaultChannel)and(line[3]==':!killsocket'):
		s.close()
		sys.exit(0)
