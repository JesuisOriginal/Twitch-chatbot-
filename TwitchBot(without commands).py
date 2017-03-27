import socket, string


#necessary to connect to Twitch#
HOST = "irc.twitch.tv"
NICK = "BOTNICK"
PORT = 6667
PASS = ""
Readbuffer = ""
MODT = False

s = socket.socket()
s.connect((HOST, PORT))
s.send("JOIN #LIVE \r\n")
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")

def Send_message(message):
	s.send("PRIVMSG #LIVE: " + message + "\r\n")

while True:
	readbuffer = readbuffer + s.recv(1024)
	temp = string.split(readbuffer, "\n")
	readbuffer = temp.pop()

	for line in temp:
		if(line[0] == "PING"):
			s.send("PING %s\r\n" % line[1])
		else:
			parts = string.split(line, ":")

			if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
				try:
					message = parts[2][:len(parts[2]) - 1]
				except:
					message = "<text>"

				if MODT:
					print username + ": " + message
					if message == "<text>":
						Send_message("<text>" + username)
				for l in parts:
					if "End of /NAMES list" in 1:
						MODT = True
