# Fat Eagle
a hacking and cybersecurity framework

&nbsp;
<center><img src="resources/fwui.png"></center>

&nbsp;
### Description
*Fat Eagle* is a hacking and cybersecurity framework written in python.
you can easily run it everywhere like windows,linux,mac,android and everywehere python can run. with this framework you can access to top
security tools like exploits,payloads,hash crackers,phishing tools and
e.t.c . as main scripts , it uses customized python script called 'FeScript' that means 'Fat Eagle Script'.

&nbsp;
### How to install
```bash
git clone https://github.com/0xDeviI/FatEagle.git
cd FatEagle
python3 -m pip install -r requirements.txt
```

&nbsp;
### How to use
You can easily run framework by this command
```bash
python3 fEagle.py
```
*Note: if you just installed python3 on your machine, type 'python' instead python3 to run framework.*

&nbsp;
### Mainly Commands
framework uses some mainly command that all fescripts designed by that.
mainly commmands are:
- search [FeScript]:             search module
- load fescript [FeScript]:      load module
- unload fescript:    unload module
- fesOptions:         show all available switch in module
- fesRequire:         show all required switch in module
- fesInfo:            show info about module
- fesHelp:            show help that module author writted
- myIP:               show IP address of user
- myHost:             show user host name
- clear/cls:          clear screen(different in windows and others)
- banner:             show random banner
- set [Property] [Value]:                set a value for a module switch
- fesStart:           start a fescript
- update db:          update module database(require if new module added)
- exit:               exit framework
- add [FeScript] [ListName]:                add a module to custom lists
- show list [ListName]:          show custom list
- info [ListName]:               show info modules in  custom list
- start:              start custom list
- mset [Property] [Value] [FeScript]:               set value to custom module in custom list
- deltemp:            delete module's temp files
- version:            show framework version
- fwi:                show info of framework

&nbsp;
### Configuration
You can easily config framework using file 'feConfig.py'. for example you can disable modules database update status in startup by this setting:
```python
MODULE_DB_UPDATE_ON_START = False
```

### LICENSE
here is MIT [License](LICENSE)