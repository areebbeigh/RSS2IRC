#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python RSS2IRC bot by M4Shooter
# :M4Shooter!M4Shooter@oper.irchound.tk PRIVMSG #lobby :!credits
# Above is a reference to how the bot sees messages, you'll need to understand this if you want to add custom commands

import socket, string, feedparser, os, time
from threading import Timer
import sys

# Info stuff
feedList = ["http://www.irchound.tk/forum/syndication.php?fid=2,14,18,4,5,11,17,6,21,23,24,22&limit=5"]
feedData = []
feedDataAgain = []
feedHasBeen = []

# Print some stuff
header = """
-----------------------------------------------
 RSS2IRC Bot by - M4Shooter - www.areeb-beigh.tk)
-----------------------------------------------
"""
print header

# The bot config
net = 'irc.irchound.tk'									# The network to connect to
port = 6667												# Server port (default = 6667)
nick = "RSS2IRC"										# Bot's nickname
ident = "M4Shooter"										# You might wanna enter your name here
real = "RSS2IRC Bot by M4Shooter - www.areeb-beigh.tk"	# Optional
default_channel = "#lobby"								# The channel the bot will join and work
password = "PASSWORD"									# The bot's account password if it's registered (Works with NickServ)
if default_channel[0] != '#':
	default_channel = '#'+default_channel

# ----> Danger ahead, please edit only if you know what you're doing!

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

# Function to send a message to the default_channel
def msg(default_channel, msg):
	s.send('PRIVMSG '+str(default_channel)+' :'+str(msg)+'\r\n')
	
# Fetches the latest feed
def feed_refresh():
	print "\nRefreshing feed list..."
	first_time = False
	if len(feedData) == 0:
		first_time = True
 	for feed in feedList:
  		f = feedparser.parse(feed)
  		for entry in f.entries:
			m = "4"+entry.title.encode('utf-8')+ " | "+"12"+entry.link.encode('utf-8')
			if m in feedData:
				first_time = False
			else:
				time.sleep(1)
				msg(default_channel, m)
				feedData.append(m)

# Return the latest feed (depends on n which by default is 1 max value for n is 4 - You can edit this) 
def last_feed(n=1):
	max_feed = 4		# Maximum number of feeds user can request
	if n > max_feed or n < 1:
		msg(default_channel, 'Error: Can send only maximum %s feeds and minimum 1' % max_feed)
	else:
		try:
			for feed in feedList:
				f = feedparser.parse(feed)
				for x in range(0,n):
					m = "4"+f.entries[x].title.encode('utf-8')+" | "+"12"+f.entries[x].link.encode('utf-8')
					msg(default_channel, m)
		except IndexError:									# Sends an error message instead of letting the bot crash
			msg(default_channel, 'No more feeds')			# due to IndexError if there are less or no feeds

# Iterate over the feedList and return results to default_channel
def feed_list():
    for feed in feedList:
        time.sleep(1)
        msg(default_channel,feed)

# Checks for feeds every 60 seconds
def update():
	x = Timer(60.0, update)
	x.daemon=True
	x.start()
	feed_refresh()

update()

# Login with NickServ
def identify():
	print "\nLogging in with NickServ in 10 seconds"
	time.sleep(10.0)
	s.send('PRIVMSG NickServ IDENTIFY '+str(password)+'\r\n')
	
identify()
		
# Let's join a default_channel
def join_channel(channel):
	print "\nJoining %s in 10 seconds" % default_channel
	time.sleep(10.0)
	s.send('JOIN '+default_channel+'\r\n') 									# Join the default_channel
	msg(default_channel, "%s Now Online - Checking latest feed - !feed help to view commands" % nick) 	# Message stuff to channel
	last_feed(1)

join_channel(default_channel)
		
while(True):
	readbuffer=readbuffer+s.recv(4096)
	temp=string.split(readbuffer, "\n")
	readbuffer=temp.pop()
	for line in temp:
		line=string.rstrip(line)
		line=string.split(line)
		
	if(line[0]=='PING'):
		s.send('PONG '+line[1]+'\r\n')
		
	if(len(line)==4)and(line[2]==default_channel)and(line[3]==':!feed'):
		msg(default_channel, "3Last three feeds:")
		last_feed(3)
			
	if(len(line)==6)and(line[2]==default_channel)and(line[3]==':!feed')and(line[4]=='last'):
		try:
			last_feed(int(line[5]))
		except ValueError:
			msg(default_channel, 'Error: Invalid parameters')
			
	if(len(line)==5)and(line[2]==default_channel)and(line[3]==':!feed')and(line[4]=='list'):
		msg(default_channel, '3Feed list:')
		feed_list()
	
	if(len(line)==5)and(line[2]==default_channel)and(line[3]==':!feed')and(line[4]=='help'):
		msg(default_channel, '3Commands:')
		msg(default_channel, '4!feed             -   13Returns last 3 feeds')
		msg(default_channel, '4!feed last (1-4)  -   13Returns last \'n\' number of feeds')
		msg(default_channel, '4!feed list        -   13Returns the feed list currently being used')
		msg(default_channel, '4!credits          -   13View bot credits')
		msg(default_channel, '4!feed help        -   13View this help dialogue')
			
	if(len(line)==4)and(line[2]==default_channel)and(line[3]==':!credits'):
		msg(default_channel, '3Python RSS2IRC Bot v2.0 by M4Shooter')
		msg(default_channel, "4Based On         -  McNally's 12 https://github.com/maK-/rss2irc-bot")
		msg(default_channel, "4RSS2IRC v2.0 by  -  M4Shooter 12 https://github.com/M4Shooter")
		
	# NOTE: This will disconnect the bot from the server and exit the program. Make sure you allow it to work only
	# 		with your nick, if you can't simply remove it / comment it out.
	# 		Replace M4Shooter!M4Shooter@oper.irchound.tk with your mask. Don't forget the ':'
	if(len(line)==4)and(line[0]==':M4Shooter!M4Shooter@oper.irchound.tk')and(line[2]==default_channel)and(line[3]==':!killsocket'):
		s.close()
		sys.exit(0)
		
