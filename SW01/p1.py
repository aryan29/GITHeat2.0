import requests
import time
import hashlib
from PIL import Image
import urllib.request
import random
import io
import pyttsx3
engine = pyttsx3.init()
engine.say('Welcome to the lazy stalker')
engine.runAndWait()
time.sleep(2)
dict={}
dict2={}
dict3={}
fil=open('newfile.txt','w')
# millis=str(round(time.time()))
# f=requests.get('http://codeforces.com/api/contest.hacks?contestId=566&apiKey=a82024a544ab1e42ae7d7bb6e9558d8ffbec50cf &time='+millis+'&apiSig=123456'+hashlib.sha512(('123456/contest.hacks?contestID=566&apiKey=a82024a544ab1e42ae7d7bb6e9558d8ffbec50cf&contestId=566&time='+millis+'#89c70675896b1ae8e15dfd65114d21c24fc0338b').encode('utf-8')).hexdigest())
# print(f.json())
engine.say('Do you want a list of upcoming contest')
engine.runAndWait()
ans=input("Do you want a list of upcoming contest(y/n)")
if(ans=='y'):
    inp=input('Do you want to add these tasks to your reminder(y/n)')
    con=requests.get('http://codeforces.com/api/contest.list?gym=false')
    dict3=con.json()
    dicts=dict3['result']
    #print(dicts)
    for i in range(len(dicts)):
        dict4=dicts[i]
        if(dict4['phase']=='BEFORE'):
              print(dict4['name'],"  Contest start in",int((dict4['relativeTimeSeconds'])/(60*60*24*-1)),"days")
              if(inp=='y'):
                  print(dict4['startTimeSeconds'],file=fil)
time.sleep(1)
engine.say('Enter name of user you want to stalk')
engine.runAndWait()
n=input("Enter Name")
res=requests.get('http://codeforces.com/api/user.info?handles='+n)
sub=requests.get('http://codeforces.com/api/user.status?handle='+n+'&from=1&count=1')
#res.encoding='utf-8'
dict=res.json()
dict2=sub.json()
if(dict['status']=='OK'):
    print("Name :",dict['result'][0]['firstName'],dict['result'][0]['lastName'])
    print("Rating :",dict['result'][0]['rating'])
    print("Rank :",dict['result'][0]['rank'])
    print("Location :",dict['result'][0]['city'],",",dict['result'][0]['country'])
    url="https:"+dict['result'][0]['titlePhoto']
    print("Img Url :",url)
    print("College :",dict['result'][0]['organization'])
    print("Last Problem Solved :",dict2['result'][0]['problem']['name'],"(",dict2['result'][0]['problem']['rating'],")")
    print("Max Rating :",dict['result'][0]['maxRating'])
    print("Max Rank :",dict['result'][0]['maxRank'])
    print("Want to see user title pic here(y/n)")
    inp=input()
    if(inp=='y' or inp=='yes' or inp=='Y'):
        urllib.request.urlopen(url)
        with urllib.request.urlopen(url) as ur:
            f = io.BytesIO(ur.read())
        img = Image.open(f)
        img.show()
    inp=input("More Details(y/n)")
    if(inp=='y' or inp=='yes' or inp=='Y'):
        tim= str(round(time.time()))
        xxx = input("key")
        yyy = input("secret")
        rand = random.randint(100000,999999)
        #print(rand)
        bash = f"{rand}/user.friends?apiKey={xxx}&onlyOnline=false&time={tim}#{yyy}"
        hsh = hashlib.sha512(bash.encode()).hexdigest()
        url = f"http://codeforces.com/api/user.friends?onlyOnline=false&apiKey={xxx}&time={tim}&apiSig={rand}{hsh}"
        f = requests.get(url)
        print("List of friends :",f.json()['result'])






else:
    print(dict['comment'])


