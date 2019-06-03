# The Lazy Stalker
#### 1)
#### You can get List of All Upcoming Codeforces contest  with time in which it is about to start not only this you can set a message reminder for all contest too You have to just click y onadding reminder and run the command
```
nohup python3 -u run.py &
```
#### in your terminal everytime before starting your laptop or you can run following code on terminal so that you dont have to run that command each time you start you laptop(Specific for Ubuntu-Gnome)
```
cd .config/autostart
sudo nano my.desktop
```
#### And add these lines to the new desktop entry created
```
[Desktop Entry]
Type=Application
Name=Python script
Exec=/home/aryan/PycharmProjects/githeat/venv/bin/python3.6<Python Path> /home/aryan/PycharmProjects/githeat/venv/run.py<File Path>
Icon=<full path to icon>
Comment=<optinal comments>
X-GNOME-Autostart-enabled=true

```

#### this program will automatically send message to the phone number added in run.py file 4 hours before contest start added in reminder but requirement is your pc should be active atleast 1 time b/w the contest start and 4 hours before it
#### Requirement is your phone number should be registered on twilio
#### And you have to add Your account_sid ,auth_token , Both Phone Numbers from which you want to receive and send message in run.py
```
Sent from your Twilio trial account-Contest is about to start in few minutes be ready for it
```

#### 2)
#### This program can return rating,rank,maxRank,maxRating,city,rank as well as title pic of any codeforces user by just entering his username
#### 3)
#### Not only all this you can also view name of the last problem submitted by the user as well asuser friends list by just adding key and secret
------------------------------------------------------------------------------------------------------------------------
#### Edit
##### I just added a flask app through which you can get details of user you enter on localhost:5000 by just activating server from flash.py
Note--Most of the Messaging client which comes with autoscheduling which people have used are not free of cost so there is no harm in running a python script in background of your lappy
