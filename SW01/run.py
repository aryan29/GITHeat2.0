from twilio.rest import Client
import schedule
import time



# fil=open('newfile.txt','r')
# for line in fil:
#     print(int(line)-round(time.time()))

def func():
    k=0
    fil=open('newfile.txt',"r")
    tim=round(time.time())
    account_sid = 'ACed..............................'  #You will find this on your twilio account
    auth_token = 'f9f7...............................'
    client = Client(account_sid, auth_token)
    for line in fil:
        if(((int(line)-tim)<=15000)and(int(line)-tim)>0):
            k=1
            break
    if(k==1):
        message = client.messages.create(
            body='Contest is about to start in few minutes be ready for it',
            from_='+18577633812',
            status_callback='http://postb.in/1234abcd',
            to='+917906224093'
        )
        print(message.sid)
        #messages will be sent b/w 9am to 9pm only @twilio india
    else:
        print("Will send message when contest will be near")
schedule.every().hour.do(func)
while True:
    schedule.run_pending()
    time.sleep(60)
