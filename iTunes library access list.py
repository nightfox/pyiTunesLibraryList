#Python 2.7
#Author n!ghtf0x
#email anirvan.mandal@gmail.com
#Script for finding the ip addresses and hostnames of people accessing your iTunes Library


import subprocess
import string
import os
import re
import shlex
import socket

output = subprocess.Popen(['netstat','-bn'], stdout=subprocess.PIPE) #Command used to list all the processes using the network card of the PC
outpart = output.communicate()[0]

outputReplaced = string.replace(outpart,'\n [',' [')

my_split = shlex.shlex(outputReplaced,posix=True)
my_split.whitespace = '\n'
my_split.whitespace_split = True

listitunes = []
for x in list(my_split):
		if 'iTunes.exe' in x :
				listitunes.append(x)				
				
my_split2 = shlex.shlex(listitunes[0],posix=True)
my_split2.whitespace = ' '
my_split2.whitespace_split = True

listipwithport = []
listipwithport.append(list(my_split2)[2])


my_split3 = shlex.shlex(listipwithport[0],posix=True)
my_split3.whitespace = ':'
my_split3.whitespace_split = True

listip = []
listip.append(list(my_split3)[0])


print (socket.gethostbyaddr(listip[0]))[0]
