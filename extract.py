#!/usr/bin/python3.8
import sys
from bs4 import BeautifulSoup
import requests
import re

# Source: https://stackoverflow.com/a/34718858

#url = 'http://cdimage.debian.org/debian-cd/8.2.0-live/i386/iso-hybrid/'
#ext = 'iso'
# url = sys.argv[1]
# ext = sys.argv[2]

def listFD(url, ext=''):
    try:
        page = requests.get(url).text
        #print(page)
        soup = BeautifulSoup(page, 'html.parser')
        #return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
        return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    except Exception as e:
        return ['Something went wrong! Please check the input.']

# for file in listFD(url, ext):
#     print(file)



#
#url = sys.argv[1]
#extension = sys.argv[2]
#
#print(url)
#print(extension)
#
##exit()
#
#with open('index.html') as html_file:
#    soup = BeautifulSoup(html_file, "lxml")
#
#for item in soup.select("a[href$='.mkv']"):
#    print(item['href'])
#
##links = []
##for link in soup.findAll('a'):
##        links.append(link.get('href'))    
##for link in links:
##    print(link)

