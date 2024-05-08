# Book - Violent Python

# Introduction
Python variables: Strings, lists, dictionaries.
Python flow structure flows: if, for, while
## TODOS
- Research
    - exceptions
- Test
    - import `socket`
    - import `sys`
        - sys.argv
    - import `os`
        - check file exists
        - write to file
    - import `crypt` (it is deprecated in python 3.13)
    - import `zipfile`, read and write zip files
        - crack passwords protected zips

# Penetration testing w python
## TODOS
    - import `optparse`, is there any other better?
    - How to use threads `Thread()`
    - `from pexpect import pxssh` For SSH Connections
    - `import nmap` to work with Nmap

# Forensics investigations w python
## TODOS
- `import pypdf` to get PDF Metadata and parse information
- `import exifread` to read EXIF data from images
- Download images from a web page with `urllib2` and `beautifulsoup4`
- `import sqlite3` to read firefox sqlite database information and browsing histoy, also cookies

# Network traffic analysis w python
## TODOS
- `pygeoip` to get lat and long of a given ip addres
- `dpkt` to work with pcap files
- `scapy` to work with packets
- `IPy` to work with IP addresses in python
- Study: H. D. Moore and petagon's dilema on TTLs and decoys
- Learn `tcpdump` basics
- Study: domain-flux dns attack and how Conficker used it to spread malware
- Study: Kevin Mitnick's tcp sequence prediction attack to shimomura machine, in python

# Wireless network cracking w python
## TODOS
- Research: how wireless networks work 802.11
- `scapy` lib to `sniff()` the network and capture the raw.load packages and use python `re` to extract
    - info like: credit cards, google searches, ftp creds, hiden networks (de-cloaking), cookies (like wordpress_)
- `pybluez` for python to scan and list bluetooth discoverable devices
    - for hiden bluetooths on phones, we can find its wifireless MAC and increase it one number, that should be the bluetooth MAC hidden device. Keep in mind that some phones in power-save mode can disable bluetooth radio
    - Test python bluetooth connections to printers

# Web hacking w python
## TODOS
- Research: Aurora and Stuxnet attacks
- `mechanize` python lib to open a website
    - set random user agents
    - set random proxies
    - `import cookielib` to store cookies and use them in the next requests
    - clean cookies, change user agents, change proxies to anonymize the requests
- `beautifulsoup4` to parse html
    - to get href and a urls
    - save images to disk with help of `mechanize` and `optparse`
# Antivirus evasion w python
## TODOS
- `ctypes` python lib to run c-style shellcodes for cmd.exe (windows)
