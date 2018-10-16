import requests
from bs4 import BeautifulSoup
import time
import random
import json
import datetime

user_agent_list = [
    #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

#place proxies in the displayed form of user:password@ip:port as shown below
proxy_list = [
    'http': 'http://sh:sh12345@54.174.250.196:3128',
    'https': 'http://sh:sh12345@54.174.250.196:3128',
     #If you want to add more proxies for a lower monitor delay just continue what i've done in the proxy_list
]
#insert discord webhook
webhook = 'Replace this text with webhook'
linklist = []

#script will go through and send all current nike products to your discord
#afterward it will only send items to discord if an item link has changed
#or if a new item is loaded

#If you use this monitor please give me credit

def monitor():
    user_agent = random.choice(user_agent_list)
    headers = {"User-Agent": user_agent}
    proxy = random.choice(proxy_list)
    source = requests.get('https://www.nike.com/sitemap-launch-en-us.xml', allow_redirects=False, headers=headers, proxies=proxy).text
    soup = BeautifulSoup(source, 'html.parser')
    for links in soup.find_all('loc'):
        link = links.text
        try:
            title = link.split("/")[5]
            if link not in linklist:
                linklist.append(link)
                print(link)
                footer1 = {
                    "text": "Devloped by @snifferprime" #Please leave my twitter handle there
                    ""}
                
                embed = {
                    "title": title,
                    "color": 5305409,
                    "timestamp": str(datetime.datetime.now()),
                    "url": link,
                    "footer": footer1
                }
                embed = [embed]
                discordjson = {"embeds": embed, "username": "STARK Supply"}
                requests.post(webhook, json=discordjson)
            else:
                pass
        except:
            print("not able")
    time.sleep(60) #script will sleep for 60 seconds then execute again looking for new links
    #the sleep time is in seconds so you can lower it if you want but you'll need proxies for
    #long term monitoring

while True:
    monitor()
