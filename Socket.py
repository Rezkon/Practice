import socket # import Socket. 
import math
import os
import string
import pygame

pygame.init() # Start Pygame Engine


logo= '''
________                      ___         ____              
`MMMMMMMb.                    `MM        6MMMMb             
 MM    `Mb                     MM       8P    Y8            
 MM     MM   ____   _________  MM   __ 6M      Mb ___  __   
 MM     MM  6MMMMb  MMMMMMMMP  MM   d' MM      MM `MM 6MMb  
 MM    .M9 6M'  `Mb /    dMP   MM  d'  MM      MM  MMM9 `Mb 
 MMMMMMM9' MM    MM     dMP    MM d'   MM      MM  MM'   MM 
 MM  \M\   MMMMMMMM    dMP     MMdM.   MM      MM  MM    MM 
 MM   \M\  MM         dMP      MMPYM.  YM      M9  MM    MM 
 MM    \M\ YM    d9  dMP    /  MM  YM.  8b    d8   MM    MM 
_MM_    \M\_YMMMM9  dMMMMMMMM _MM_  YM._ YMMMM9   _MM_  _MM_
                                                            
'''


print logo



print "Please enter a 1. FTP Scanner. 2. SSH Botnet 3. Nmap Client 4. Chat.. "
User_input = input()
if User_input == 1:

	print ("User_ip Please:.. ")	
	User_ip = raw_input()
	socket.setdefaulttimeout(2) # If Socket longer then 2 
	s = socket.socket()   # connect s to socket.socket()
	s.connect((User_ip,902))  # S.connect User_ip, port 902
	ans = s.recv(1024) # Connect Ans s.recv(1024) // Look this up. //  
	print User_ip
	print "[+] The Ip "+str(User_ip)+" on port: "+str(ans) # Pront user ip and ans from above string

if User_input == 2:
	print "SSH BotNet Alpha"
	print "Version 1.0.0"
	print "Coming soon.."
	size = (700, 500)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("SSH BotNET Alpha 1.0.0")
	pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
	print "Exiting!...."
	exit(3)
if User_input == 3: 
	print "NMAP Coming Soon.."
	exit()