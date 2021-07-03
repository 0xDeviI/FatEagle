from math import trunc
import sys
import fescripts.libs.fescripts
from fescripts.libs.PFable import fable,fable_mode
from colorama import init
init()
from colorama import Fore,Back
import requests
import tldextract
import threading
import signal

class WhoIsWho:
    def signal_handler(self,sig, frame):
      self._end()
    signal.signal(signal.SIGINT, signal_handler)
    _fs = fescripts.libs.fescripts.FE_SCRIPTS("WhoIsWho","a multi threaded FeScript to find accounts of a username in websites","""a multi threaded FeScript to find accounts of a username in most popular websites\nlike instagram , e.t.c. coded by 0xDeviI.to use this FeScript,\n load it , set requirements , and BOMB , start it :)""",{'USERNAME': {'Body': '', 'Description': 'username to search', 'Require': True}},"0xDeviI")
    
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


    def checkUser(self,_url,output):
      nonExistWords = ['Sorry','Not','Couldn\'t','Can\'t','Miss','Missed','404']
      try:
        r = requests.head(url=_url)
        if (r.status_code < 400):
          output[_url] = 'Exist'
        else:
          found = False
          for i in nonExistWords:
            if (i.casefold() in r.text):
              output[_url] = 'NotExist'
              found = True
              break
          if (found == False):
            output[_url] = "MayExist"
          else:
            output[_url] = 'NotExist'
      except requests.exceptions.Timeout as e:
        output[_url] = 'TimeOut'
      except requests.exceptions.ConnectionError as ee:
        output[_url] = 'ConError'

    def _start(self):
      print("\nFatEagle Script ' " + Fore.YELLOW + self.__class__.__name__ + Fore.RESET + " '" + Fore.GREEN + " Started!" + Fore.RESET)
      # --------------------------------------------> Script Started!
      username = self._fs._Opt["USERNAME"]["Body"]

      instagram = f'https://www.instagram.com/{username}'
      facebook = f'https://www.facebook.com/{username}'
      twitter = f'https://www.twitter.com/{username}'
      youtube = f'https://www.youtube.com/{username}'
      blogger = f'https://{username}.blogspot.com'
      google_plus = f'https://plus.google.com/s/{username}/top'
      reddit = f'https://www.reddit.com/user/{username}'
      wordpress = f'https://{username}.wordpress.com'
      pinterest = f'https://www.pinterest.com/{username}'
      github = f'https://www.github.com/{username}'
      tumblr = f'https://{username}.tumblr.com'
      flickr = f'https://www.flickr.com/people/{username}'
      steam = f'https://steamcommunity.com/id/{username}'
      vimeo = f'https://vimeo.com/{username}'
      soundcloud = f'https://soundcloud.com/{username}'
      disqus = f'https://disqus.com/by/{username}'
      medium = f'https://medium.com/@{username}'
      deviantart = f'https://{username}.deviantart.com'
      vk = f'https://vk.com/{username}'
      aboutme = f'https://about.me/{username}'
      imgur = f'https://imgur.com/user/{username}'
      flipboard = f'https://flipboard.com/@{username}'
      slideshare = f'https://slideshare.net/{username}'
      fotolog = f'https://fotolog.com/{username}'
      spotify = f'https://open.spotify.com/user/{username}'
      mixcloud = f'https://www.mixcloud.com/{username}'
      scribd = f'https://www.scribd.com/{username}'
      badoo = f'https://www.badoo.com/en/{username}'
      patreon = f'https://www.patreon.com/{username}'
      bitbucket = f'https://bitbucket.org/{username}'
      dailymotion = f'https://www.dailymotion.com/{username}'
      etsy = f'https://www.etsy.com/shop/{username}'
      cashme = f'https://cash.me/{username}'
      behance = f'https://www.behance.net/{username}'
      goodreads = f'https://www.goodreads.com/{username}'
      instructables = f'https://www.instructables.com/member/{username}'
      keybase = f'https://keybase.io/{username}'
      kongregate = f'https://kongregate.com/accounts/{username}'
      livejournal = f'https://{username}.livejournal.com'
      angellist = f'https://angel.co/{username}'
      last_fm = f'https://last.fm/user/{username}'
      dribbble = f'https://dribbble.com/{username}'
      codecademy = f'https://www.codecademy.com/{username}'
      gravatar = f'https://en.gravatar.com/{username}'
      pastebin = f'https://pastebin.com/u/{username}'
      foursquare = f'https://foursquare.com/{username}'
      roblox = f'https://www.roblox.com/user.aspx?username={username}'
      gumroad = f'https://www.gumroad.com/{username}'
      newsground = f'https://{username}.newgrounds.com'
      wattpad = f'https://www.wattpad.com/user/{username}'
      canva = f'https://www.canva.com/{username}'
      creative_market = f'https://creativemarket.com/{username}'
      trakt = f'https://www.trakt.tv/users/{username}'
      five_hundred_px = f'https://500px.com/{username}'
      buzzfeed = f'https://buzzfeed.com/{username}'
      tripadvisor = f'https://tripadvisor.com/members/{username}'
      hubpages = f'https://{username}.hubpages.com'
      contently = f'https://{username}.contently.com'
      houzz = f'https://houzz.com/user/{username}'
      blipfm = f'https://blip.fm/{username}'
      wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'
      hackernews = f'https://news.ycombinator.com/user?id={username}'
      codementor = f'https://www.codementor.io/{username}'
      reverb_nation = f'https://www.reverbnation.com/{username}'
      designspiration = f'https://www.designspiration.net/{username}'
      bandcamp = f'https://www.bandcamp.com/{username}'
      colourlovers = f'https://www.colourlovers.com/love/{username}'
      ifttt = f'https://www.ifttt.com/p/{username}'
      ebay = f'https://www.ebay.com/usr/{username}'
      slack = f'https://{username}.slack.com'
      okcupid = f'https://www.okcupid.com/profile/{username}'
      trip = f'https://www.trip.skyscanner.com/user/{username}'
      ello = f'https://ello.co/{username}'
      tracky = f'https://tracky.com/user/~{username}'
      basecamp = f'https://{username}.basecamphq.com/login'
      WEBSITES = [
      instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
      wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus, 
      medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
      mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
      goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
      dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
      wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
      contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
      bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
      ]
      threads = []
      output = {}
      for i in WEBSITES:
        t = threading.Thread(target=self.checkUser, args=(i,output),daemon=True)
        threads.append(t)
      for i in threads:
        i.start()
      for i in threads:
        i.join()
      keys = output.keys()
      for i in keys:
        if (output[i] == "Exist"):
          print(Fore.GREEN + "[+] " + i + Fore.RESET)
        elif (output[i] == "MayExist"):
          print(Fore.YELLOW + "[*] " + i + "  --->  May Exist" + Fore.RESET)
        elif (output[i] == "TimeOut"):
          print(Fore.LIGHTRED_EX + "[!] " + i + "  --->  Timeout" + Fore.RESET)
        elif (output[i] == "ConError"):
          print(Fore.LIGHTRED_EX + "[!] " + i + "  --->  Connection Error" + Fore.RESET)
        elif (output[i] == "NotExist"):
          print(Fore.RED + "[-] " + i + Fore.RESET)

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
