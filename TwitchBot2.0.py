from test import string
HOST = "irc.twitch.tv"
NICK = "Botnick"
PORT = 6667
PASS = "Oauthkey"
readbuffer = ""
MODT = False
mood = 0

#EMOTES
illuminati = " TheIlluminati "
salty = " PJSalt "
smile = " :) "
tongue = " :P "
surprised = " :o "
angry = " >( "
bigsmile = " :D "  
bored = " :z "
confused = " o_O "
undecided = " :\ "
wink = " ;p "
winking =" ;) "
cool = "  B)  "
heart = " <3 "
sad = " :( "
classickappa = " Kappa "
kappalgbt = " KappaPride "
keepo = " Keepo "
dog = " OhMyDog "

s = socket.socket()
s.connect ((HOST, PORT))
s.send("PASS " + PASS + "\r\n")
s.send("NICK " + NICK + "\r\n")
s.send("JOIN <Channelname> \r\n")

#message
def Send_message(message):
    s.send("PRIVMSG #STREAMERNICK:" + message + "\r\n")

#Set your commands, i gonna use only "!time" and "!kappa" for example
def time():
    Send_message("Commands: !time, !kappa")

t = threading.Timer(7.0, time)
t.start()

while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        if (line[0] == "PING"):
            s.send("PING %s\r\n" % line[1])
        else:
            parts = string.split(line, ":")

            if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
                try:
                    message = parts[1][:len(parts[2]) - 1]
                except: 
                    message = ""

                usernamesplit = string.split(parts[1], "!")
                username = usernamesplit[0]
               
                #MODT = Message of the day
                if MODT:
                    print username + ": " + message

                    #Put your commands here
                    if message == "Hello":
                        Send_message("Hello " + username + cool)

                    if message == "How are you?":
                        mood = random.randint(3,6)
                        if mood == 3: Send_message("Nice, " + username  + smile)                        
                        elif mood == 4: Send_message("Fine, " + username  + tongue)
                        elif mood == 5: Send_message("Not bad, " + username  + bored)
                        elif mood == 6: Send_message("OK, " + username   + undecided)

                    if message == "!time":
                        Send_message(strftime("Now" + "%a, %d %b %Y %H:%M:%S", gmtime())+ "," + username)

                    if message == "!kappa":
                        mood = random.radiant(1,3)
                        if mood == 1: Send_message(classickappa)
                        elif mood == 2: Send_message(kappalgbt)
                        elif mood == 3: Send_message(keepo)

               for l in parts:
                    if "End of /NAMES list" in l:
                        MODT = True