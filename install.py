import os, sys
from time import sleep

if not os.geteuid() == 0:
    sys.exit("\033[1;31mPlease run this script as root!\033[0m")

header = """
            ------------------------------------------------------------
           +[!]* < !! Welcome To Most Advanced Pentesting Tools!! > *[!]+
            ------------------------------------------------------------
                            \  ^\__/^ CODE FIXED
                             \  (oo)\__________
                                (__)\    by    )\/
                                     \ MEHEDI  
                                    ||--------||
                                    ||        ||
"""

print header
print "\033[1;36mOperating Systems Available:\033[1;36m "
print "\n--------------------------"
print "(1) Kali Linux / Ubuntu / Raspbian"
print "--------------------------\n"

option = input("\033[0m[>] Select Operating System: \033[0m")

if option == 1:
    print "\033[1;33m[*] Loading...\033[0m"
    os.system('apt-get install python-pip')
    import pip
    install = os.system("apt-get update && apt-get install -y build-essential git")
    install2 = os.system("cp -R trity/ /opt/ && cp trity.py /opt/trity && cp run.sh /opt/trity && cp run.sh /usr/bin/trity && chmod +x /usr/bin/trity")
    os.system('apt-get install info')
    os.system('apt-get install sendemail')
    os.system('apt-get install lib32ncurses5-dev')
    os.system('apt-get install libncurses5-dev')
    os.system('pip install netifaces')
    os.system('pip install scapy')
    os.system('pip install SpoofMAC')
    os.system('pip install pythonwhois')
    os.system('pip install readline')
    os.system('pip install BeautifulSoup')
    os.system('pip install requests')
    os.system('pip install mechanize')
    os.system('pip install google')
    os.system('pip install qrcode')
    os.system('pip install search_google')

    print "\033[1;32m[!] Trity is now successfuly installed on your Kali Linux / Ubuntu! Run 'trity' to run program [!]\033[0m"
    sys.exit()
else:
    print "Whoops! Something went wrong!"
