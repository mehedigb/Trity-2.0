# coding: utf-8
#!/usr/bin/env python
import sys, platform, subprocess, socket, time, os, urllib, platform, random, string, smtplib, requests, urllib2, getpass, zipfile
from urllib2 import urlopen
from time import sleep
from getpass import getpass
from subprocess import call
sys.path.append('trity/')
from smtp import *
from sms import *
from gmail import *
from crafttable import *
from clickjacking import *
from info import *
from twitter import *
from whoisweb import *
from coder import *
from clone import *
from admin import *
from banner import *
from joke import *
from facebook import *
from quote import *
from anon import *
from web import *
from qr import *
from siteexists import *
from hex import *
from google import *
from zip import *
from emaill import *
try:
    import netifaces
    import scapy
    import readline
    import pip
    import pythonwhois
    import argparse
    import google
    import search_google
except ImportError:
    print (color.UNDERLINE + "\033[91m" + "You don't have some modules installed! \nPlease run install.py to install this tool fully! " + color.END)
    sys.exit()
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta
os.system('clear')
if str(platform.system()) != "Linux":
	sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "You are not using a Linux Based OS! Linux is a must-have for this script!" + color.END)
if not os.geteuid() == 0:
    sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Must be run as root. :/" + color.END)
if 'no' in open('agree.txt').read():# take out the trity/
    print color.BOLD + """
Note that Trity is provided as is, and is a royalty free open-source application.

Feel free to modify, use, change, market, do whatever you want with it as long as you give the appropriate credit where credit is due (which means giving the authors the credit they deserve for writing it).

Also by using this tool, you should try to make this tool better, try to stay positive, try to help others, try to learn from one another, try stay out of drama, try offer free hugs when possible (and make sure recipient agrees to mutual hug), and try to do everything you can to be awesome.
Trity is designed purely for good and not evil. If you are planning on using this tool for malicious purposes that are not authorized by the company you are performing assessments for, you are violating the terms of service and license of this toolset. By hitting yes (only one time), you agree to the terms of service and that you will only use this tool for lawful purposes only.
"""
    agree = raw_input(''+G+'' + color.UNDERLINE + 'Do you agree to these terms and conditions?>' + color.END)
    if agree == "yes":
	print (''+G+'' + color.UNDERLINE + 'Thanks!' + color.END)
	time.sleep(3)
	FILE = open("agree.txt","w")# take out the trity/
        FILE.write('yes')
        FILE.close()
    elif agree == "y":
	print (''+G+'' + color.UNDERLINE + 'Thanks!' + color.END)
	time.sleep(3)
	FILE = open("agree.txt","w")# take out the trity/
        FILE.write('yes')
        FILE.close()
    elif agree == "Yes":
	print (''+G+'' + color.UNDERLINE + 'Thanks!' + color.END)
	time.sleep(3)
	FILE = open("agree.txt","w")# take out the trity/
        FILE.write('yes')
        FILE.close()
    else:
	print (''+R+'' + color.UNDERLINE + '[!] You have to agree!' + color.END)
	time.sleep(1)
	sys.exit()
os.system('clear')
banner()
#============================================================#
#------------------- Onto the real stuff --------------------#
#============================================================#
def banner1():
    print ""
    print ""+M+"|----- Made by _t0x1c aka toxic -----|"
    print color.DARKCYAN +"|-----      Version: 3.0.1      -----|"
    print color.WARNING + "|-----   1 tool - 35 choices    -----|"
    print color.RED + "|-----  www.toxic-ig.github.io  -----|"
    print color.PURPLE + "\n|----- A Warm Welcome to Trity! -----|"
    print color.BLUE + "|----- Network Pentesting tool! -----|"
    print color.YELLOW + "|----- Have Fun and Stay Legal! -----|"

time.sleep(0.1)
print ""
time.sleep(0.1)
print ""+M+"|----- Made by _t0x1c aka toxic -----|" 
time.sleep(0.1)
print color.DARKCYAN + "|-----      Version: 3.0.1      -----|"
time.sleep(0.1)
print color.WARNING + "|-----   1 tool - 35 choices    -----|"
time.sleep(0.1) 
print color.RED + "|-----  www.toxic-ig.github.io  -----|"
time.sleep(0.1)
print color.PURPLE + "\n|----- A Warm Welcome to Trity! -----|"
time.sleep(0.1)
print color.BLUE + "|----- Awesome Pentesting tool! -----|"
time.sleep(0.1)
print color.YELLOW + "|----- Have Fun and Stay Legal! -----|"
time.sleep(0.1)
r = requests.get('http://pastebin.com/raw/vYcBSV4w') 

if '3.1' not in r.text:
    print (''+R+'\nYou need to update! The newest version is: ' + color.BOLD + color.UNDERLINE + r.text + '\n')
else:
    print ('')
swear = "fuck", "shit", "nigga", "bitch", "dick", "pussy", "cunt", "nigger", "asshole", "ass"
spell = "helpp", "hellp", "bannerr", "baner", "emial", "HELP", "hwlp", "wesbite", "ehco", "anonymouss", "anonymouse", "toool", "tooll", "carft", "Info", "spooof", "spooff", "ecnode", "decde", "encde", "craftt", "qoute", "sitexists", "hlep", "claer"
def tritymain():
    while True:
        try:
            main = raw_input(''+G+'' + color.BOLD + color.UNDERLINE + 'Tri>' + color.END)
            if main in swear:
                print(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Watch your language!" + color.END)
	    elif main in spell:
                print(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Do you know how to spell?!" + color.END)
            elif main == "joke":
                joke()
            elif main == "info":
                info()
            elif main == "help":
                print ""+W+"+----------------------------+"
                print ""+C+"help "+W+"- displays this help message"
                print ""+C+"clear "+W+"- clears the screen"
                print ""+C+"exit "+W+"- exits tool"
                print ""+C+"tool "+W+"- displays info about the tool"
                print ""+C+"info "+W+"- displays computer and network info"
                print ""+C+"cd "+W+"- change working directories"
                print ""+C+"ls "+W+"- see files in working directory"
                print ""+W+"+----------------------------+"
                print ""+P+"echo "+W+"- echo given words"
                print ""+P+"speak "+W+"- text to speech"
                print ""+P+"ping "+W+"- ping a host"
                print ""+P+"banner "+W+"- print a new banner"
                print ""+P+"joke "+W+"- tell a joke"
                print ""+P+"quote "+W+"- print a quote"
                print ""+P+"contact "+W+"- contact me"
                print ""+W+"+----------------------------+"
                print ""+R+"website "+W+"- enter a website and get its ip"
	        print ""+R+"clone"+W+" - clone a websites source "
	        print ""+R+"whois"+W+" - whois a website"
	        print ""+R+"web"+W+" - extract info from a website"
	        print ""+R+"siteexists"+W+" - check if a site exists"
	        print ""+R+"google"+W+" - find google results for a query"
	        print ""+R+"clickjacking"+W+" - test websites for clickjacking vulnerability"
                print ""+W+"+----------------------------+"
	        print ""+G+"ip "+W+"- geolocate an ip"
                print ""+W+"+----------------------------+"
	        print ""+O+"spoof mac"+W+" - spoof mac address"
                print ""+W+"+----------------------------+"
	        print ""+T+"email "+W+"- bomb an email address"
	        print ""+T+"spoof email "+W+"- spoof an email address"
	        print ""+T+"sms"+W+" - spam text messages "
	        print ""+T+"crack"+W+" - bruteforce an email"
	        print ""+T+"anonymous"+W+" - send an anonymous email"
                print ""+T+"facebook"+W+" - bruteforce a facebook account"
                print ""+T+"twitter"+W+" - check the details of a twitter account"
                print ""+W+"+----------------------------+"
	        print color.CYAN + "craft"+W+" - generate useful scripts "
	        print color.CYAN + "qr"+W+" - generate a qr code"
	        print color.CYAN + "zip"+W+" - crack a password-protected zip file"
                print ""+W+"+----------------------------+"
	        print color.BLUE + "encode base64"+W+" - text to base64"
	        print color.BLUE + "decode base64"+W+" - base64 to text"
	        print color.BLUE + "encode hex"+W+" - text to hex"
	        print color.BLUE + "decode hex"+W+" - hex to text"
                print ""+W+"+----------------------------+"
            elif main == "spoof mac":
	        print ""+C+"1 - Random MAC address"
	        print ""+C+"2 - Set MAC address"
	        print ""+C+"3 - See available addresses"
	        while True:
	            spoofmac = raw_input(''+G+'' + color.UNDERLINE + 'Tri>Spoof>' + color.END)
	            if spoofmac == "1":
		        try:
	                    inter = raw_input(''+T+'' + color.UNDERLINE + 'Interface>' + color.END)
	                    os.system('spoof-mac.py randomize ' + inter)
	                    print ""+G+"[*] Done! "+C+"To change you MAC Address back to your original, restart your computer\n or set your MAC address to your original"
		        except:
		            print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Oops.... Something went wrong!" + color.END)
	            elif spoofmac == "2":
	                try:
	                    inter = raw_input(''+T+'' + color.UNDERLINE + 'Interface>' + color.END)
		            setmac = raw_input(''+T+'' + color.UNDERLINE + 'New MAC>' + color.END)
	                    os.system('spoof-mac.py set ' + setmac + ' ' + inter)
			    print ""+C+"Keep in mind you won't have internet during the time of your spoofed MAC!"
		            print ""+G+"[*] Done!"+C+" To change you MAC Address back to your original, restart your computer\n or set your MAC address to your original"
		        except:
		            print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Oops... Something went wrong!" + color.END)
	            elif spoofmac == "3":
		        os.system('spoof-mac.py list')
	            else:
		        print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "That is not an option!" + color.END)

	    elif main == "sms":
	        sms()
	    elif main == "encode base64":
	        encode()
	    elif main == "decode base64":
	        decode()
	    elif main == "email":
	        smtp()
	    elif main == "quote":
	        quote()
	    elif main == "spoof email":
	        spoofemail()
	    elif main == "zip":
	        zipfile()
	    elif main == "decode hex":
	        decode1()
	    elif main == "encode hex":
	        encode1()
	    elif main == "google":
	        googleSearch()
	    elif main == "web":
	        web()
	    elif main == "clickjacking":
	        clickjacking()
	    elif main == "siteexists":
	        siteexists()
	    elif main == "qr":
	        gen_qrcode()
	    elif main == "twitter":
	        twitter()
	    elif main == "crack":
	        gmail()
	    elif main == "anonymous":
	        anon()
	    elif main == "contact":
	        print(''+T+'' + color.UNDERLINE + 'Skype:'+W+'' + color.BOLD + ' infamouzgaming' + color.END)
	        print(''+T+'' + color.UNDERLINE + 'Instagram:'+W+'' + color.BOLD + ' @_t0x1c - www.instagram.com/_t0x1c' + color.END)
	        print(''+T+'' + color.UNDERLINE + 'Email me:'+W+'' + color.BOLD + ' t0x1cigyt@gmail.com' + color.END)
	        print(''+T+'' + color.UNDERLINE + 'XMPP:'+W+'' + color.BOLD + ' toxic-ig@exploit.im' + color.END)
	    elif main == "ping":
		while True:
	            hostname = raw_input(''+T+'' + color.UNDERLINE + 'Host>' + color.END)
	            os.system("ping " + hostname)
	    elif main == "craft":
		while True:
	            table()
	    elif main == "facebook":
	        facebook()
	    elif main == "whois":
	        whoisweb()
	    elif main == "admin":
	        admin()
	    elif main == "banner":
	        os.system('clear')
	        banner()
	        banner1()
	    elif main == "speak":
		while True:
	            speak = raw_input(''+T+'' + color.UNDERLINE + 'What to say>' + color.END)
	            os.system('espeak "' + speak + '"')
	    elif main == "echo":
		while True:
	            echo = raw_input(''+T+'' + color.UNDERLINE + 'What to echo>' + color.END)
	            os.system('echo ' + echo)
	    elif main == "clone":
	        clone()
	    elif main == "cd":
	        try:
	            path = raw_input(''+T+'' + color.UNDERLINE + 'Directory>' + color.END)
	            os.chdir(path)
	        except OSError:
	            print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "That is not a directory!" + color.END)
	    elif main == "ls":
	        os.system('ls')
	    elif main == "tool":
	        print(color.UNDERLINE + ''+C+'Version: 3.0.1' + color.END)
	        print(color.UNDERLINE + ''+C+'Time spent on it: 74 hours - 21 minutes' + color.END)
	        print(color.UNDERLINE + ''+C+'toxic is a sp00ky h4ck3r' + color.END)
	    elif main == "website":
		while True:
	            a = raw_input(''+T+'' + color.UNDERLINE + 'Website>' + color.END)
	            try:
	                print socket.gethostbyname(a)
	            except socket.gaierror:
	                print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Apparently host is unknown! :/" + color.END)
	    elif main == "ip":
	        ip = raw_input(''+T+'' + color.UNDERLINE + 'IP>' + color.END)
	        if ip is None or ip == "":
	            sys.exit(""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Please enter an IP!" + color.END)
	        reversed_dns = socket.getfqdn(ip)
	        geoip = urllib.urlopen('http://api.hackertarget.com/geoip/?q='
                               + ip).read().rstrip()
	        print (""+G+"[*] " + color.UNDERLINE + "\033[91m" + "IP Info" + color.END)
	        print geoip
	    elif main == "clear":
	        os.system('clear')
            elif main == "exit":
	        print (""+G+"[*] " + color.UNDERLINE + "\033[91m" + "Exiting..." + color.END)
	        print (""+G+"[*] " + color.UNDERLINE + "\033[92m" + "GoodBye!" + color.END)
	        time.sleep(0.2)
	        sys.exit()
	    elif main == "":
	        print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "Please enter an option!" + color.END)
            else:
	        print (""+R+"[!] " + color.UNDERLINE + "\033[91m" + "That is not an option!" + color.END)
        except KeyboardInterrupt:
		print "\n"
		tritymain()
tritymain()
