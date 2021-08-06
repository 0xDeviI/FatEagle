import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import signal
from genericpath import getmtime
import requests
from gevent import monkey
from urllib.parse import urlparse, urljoin
import re
from lxml import html
from collections import *
from enum import Enum
from stem import Signal
from stem.control import Controller
from time import sleep

class Qrawler:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("Qrawler","a FeScript that performs crawling process","""this FeScript will starts a crawling process on any website and uses Tor Service to bypass server IP blocking""",{'url': {'Body': '', 'Description': 'website url in format [protocol]://[domain].[tld]', 'Require': True}},"0xDeviI")
    
    def __init__(self):
      pass
    
    def help(self):
        print(self._fs._totalDesc)

    def _help(self):
      return self._fs._totalDesc

    def _author(self):
      return self._fs._author
    
    def info(self):
      print(self._fs._miniDesc + "\n    Author: " + self._fs._author)
    
    def _info(self):
      return self._fs._miniDesc

    def allRequirement(self):
      keys = self._fs._Opt.keys()
      allKeys = []
      for i in keys:
        if (self._fs._Opt[i]['Require'] == True):
          allKeys.append(i)
      return allKeys

    def allSwitches(self):
      keys = self._fs._Opt.keys()
      allKeys = []
      for i in keys:
        allKeys.append(i)
      return allKeys

    def _pre_start(self):
      _all_req = self.allRequirement()
      found = False
      for i in _all_req:
        if (self._fs._Opt[i]["Body"] == ""):
          found = True
          break
      if (found):
        print(Fore.RED + "All requirement switches not filled!" + Fore.RESET)   
      else:
        self._start()

    def showSwitch(self,sw):
      print(self._fs._Opt[sw]["Body"])

    # <-------------- Tor Config -------------->
    def renew_connection(self):
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password="test")
            controller.signal(Signal.NEWNYM)
            
    def get_tor_session(self):
        session = requests.session()
        session.proxies = {'http':  'socks5://127.0.0.1:9050',
                          'https': 'socks5://127.0.0.1:9050'}
        return session

    class URL_TYPE(Enum):
        File = 0,
        Page = 1


    class _URL():
        _url = ""
        _url_type = None

        def __init__(self, url, url_type) -> None:
            self._url = url
            self._url_type = url_type

        def getUrl(self) -> str:
            return self._url

        def getUrlType(self) -> str:
            return self._url_type



    def getMainDomain(self,_url):
        domains = urlparse(_url).netloc.split(".")
        host = domains[len(domains) - 2] + '.' + domains[len(domains) - 1]
        return host


    def couldBeFile(self,url):
        allowed_file_ext = ["htm", "html", "htmls", "php", "php3", "asp", "aspx"]
        parsedURL = urlparse(url)
        if (parsedURL.scheme + "://" + parsedURL.netloc == url):
            return False
        elif (parsedURL.scheme + "://" + parsedURL.netloc + parsedURL.path == url and parsedURL.path == '/'):
            return False
        elif (parsedURL.query == ""):
            url = url[::-1]
            slashReached = False
            currentFileExt = ""
            for i in url:
                if (str(i) == '/'):
                    slashReached = True
                    return False
                if (str(i) == '.' and slashReached == False):
                    if (currentFileExt[::-1].casefold() in allowed_file_ext):
                        return False
                    return True
                else:
                    currentFileExt += str(i)
            return False
        else:
            return False


    def findPageLinks(self,webpage, content="", url=""):
        _url = ""
        if ('https://' in url):
            _url = 'https://' + urlparse(url).netloc
        elif ('http://' in url):
            _url = 'http://' + urlparse(url).netloc
        hrefs = webpage.xpath('//a/@href')
        srcs = re.findall(r'(?=src)src=\"(?P<src>[^\"]+)', content)
        allLinks = []
        for i in hrefs:
            if (' ' in i or "'" in i or '#' in i or i == _url or i == _url + '/' or len(i) == 0):
                continue
            if (i[0] == '/'):
                if (urlparse(url).query != ""):
                    allLinks.append(_url + '/' + i)
                else:
                    allLinks.append(url + '/' + i)
            elif (len(i) >= 3 and i[0:3] == "../"):
                allLinks.append(urljoin(url,i))
            elif ('http' not in i or 'https' not in i and i[len(i) - 1] == '/'):
                if (urlparse(url).query != ""):
                    allLinks.append(_url + '/' + i)
                else:
                    allLinks.append(url + '/' + i)
            else:
                allLinks.append(i)
        for i in srcs:
            if (' ' in i or "'" in i or '#' in i or i == _url or i == _url + '/' or len(i) == 0):
                continue   
            if (i[0] == '/'):
                if (urlparse(url).query != ""):
                    allLinks.append(_url + '/' + i)
                else:
                    allLinks.append(url + '/' + i)
            elif (len(i) >= 3 and i[0:3] == "../"):
                allLinks.append(urljoin(url,i))
            elif ('http' not in i or 'https' not in i and i[len(i) - 1] == '/'):
                if (urlparse(url).query != ""):
                    allLinks.append(_url + '/' + i)
                else:
                    allLinks.append(url + '/' + i)
            else:
                allLinks.append(i)
        return allLinks

    def UnDuplicate(self,x):
        return list(dict.fromkeys(x))

    crawled = []

    def urlCrawler(self,url):
        try:
            url = url[0:len(url) - 1] if url[len(url) - 1] == '/' else url
            try:
                page = self.session.get(url,headers={'User-Agent': 'Mozilla/5.0'})
            except requests.exceptions.ConnectionError:
                self.renew_connection()
                sleep(8)
            webpage = html.fromstring(page.content)
            links = self.UnDuplicate(self.findPageLinks(webpage,page.text,url))
            allLinks = []
            for i in links:
                allLinks.append(self._URL(i,self.URL_TYPE.File if self.couldBeFile(i) == True else self.URL_TYPE.Page))
            for i in allLinks:
                if (i.getUrl() not in self.crawled):
                    urlType = str(i.getUrlType()).replace("URL_TYPE.","")
                    if (i.getUrlType() == self.URL_TYPE.File):   print(f"[{Fore.YELLOW}xxx{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
                else:
                        try:
                            page = self.session.get(i.getUrl(),headers={'User-Agent': 'Mozilla/5.0'})
                        except requests.exceptions.ConnectionError:
                            self.renew_connection()
                            sleep(8)
                        if (int(page.status_code / 100) == 2):
                            print(f"[{Fore.GREEN}{page.status_code}{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
                        elif (int(page.status_code / 100) == 3):
                            print(f"[{Fore.YELLOW}{page.status_code}{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
                        elif (int(page.status_code / 100) == 4 or int(page.status_code / 100) == 5):
                            print(f"[{Fore.RED}{page.status_code}{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
                        else:
                            print(f"[{Fore.CYAN}{page.status_code}{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
                        self.crawled.append(i.getUrl())
            for i in allLinks:
                if (i.getUrlType() == self.URL_TYPE.Page and i.getUrl() not in self.crawled):
                    self.urlCrawler(i.getUrl())
                else:
                    self.crawled.append(i.getUrl())
        except:
            print(f"[{Fore.RED}unk{Fore.RESET}][{Fore.MAGENTA}unk{Fore.RESET}] {url}")
            pass
          
    monkey.patch_all(ssl=False)
    session = ""

    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      url = self._fs._Opt["url"]["Body"]
      url = url[0:len(url) - 1] if url[len(url) - 1] == '/' else url
      global session
      self.session = self.get_tor_session()
      page = self.session.get(url,headers={'User-Agent': 'Mozilla/5.0'})
      webpage = html.fromstring(page.content)
      links = self.UnDuplicate(self.findPageLinks(webpage,page.text,url))
      allLinks = []
      for i in links:
          allLinks.append(self._URL(i,self.URL_TYPE.File if self.couldBeFile(i) == True else self.URL_TYPE.Page))
      for i in allLinks:
          urlType = str(i.getUrlType()).replace("URL_TYPE.","")
          if (i.getUrlType() == self.URL_TYPE.File):   print(f"[{Fore.YELLOW}xxx{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
          else:
              if (i.getUrl() not in self.crawled):
                  page = self.session.get(i.getUrl(),headers={'User-Agent': 'Mozilla/5.0'})
                  if (int(page.status_code / 100) == 2):
                      print(f"[{Fore.GREEN}{page.status_code}{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
                  elif (int(page.status_code / 100) == 3):
                      print(f"[{Fore.YELLOW}{page.status_code}{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
                  elif (int(page.status_code / 100) == 4 or int(page.status_code / 100) == 5):
                      print(f"[{Fore.RED}{page.status_code}{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
                  else:
                      print(f"[{Fore.CYAN}{page.status_code}{Fore.RESET}][{Fore.MAGENTA}{urlType}{Fore.RESET}] {i.getUrl()}")
                  self.crawled.append(i.getUrl())
      for i in allLinks:
          if (i.getUrlType() == self.URL_TYPE.Page):
              self.urlCrawler(i.getUrl())
          else:
              self.crawled.append(i.getUrl())
              
      print(f"\n{Fore.GREEN}Url Crawled!{Fore.RESET}")
      # --------------------------------------------> Script Stopped!
      self._end()

    def _end(self):
      print("FatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.RED + " Stopped!\n\n" + Fore.RESET)
    
    def missedSwitch(self):
      fable_data = []
      keys = self._fs._Opt.keys()
      for i in keys:
        if (self._fs._Opt[i].get("Require") == True and self._fs._Opt[i].get("Body") == ""):
          fable_data.append([i,self._fs._Opt[i].get("Body"),self._fs._Opt[i].get("Description")])
      fabled = fable(["switch name","value","descrption"],fable_data,fable_mode.SLICED)
      print(fabled.popData())

    def switchInfo(self):
      fable_data = []
      keys = self._fs._Opt.keys()
      for i in keys:
        fable_data.append([i,self._fs._Opt[i].get("Body"),str(self._fs._Opt[i].get("Require")),self._fs._Opt[i].get("Description")])
      fabled = fable(["switch name","value","required","descrption"],fable_data,fable_mode.SLICED)
      print(fabled.popData())
    
    def setSwitch(self,prop,value):
      self._fs._Opt[prop]["Body"] = value
