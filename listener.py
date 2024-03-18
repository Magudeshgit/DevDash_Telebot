import requests as r
import csv
from config import bot
import os

cwd = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

@bot.message_handler(commands=['start'])
def initial(message):
    print('Chat ID',message.chat.id)
    tresp = message.chat.id
    datafile = open(cwd + "ChatID.csv", "w")
    wr = csv.writer(datafile)
    wr.writerow([tresp])
    datafile.close()

    tresp = 'Welcome to DevDash\n\nAn AWS management application\nYou will receive timely updates regarding your AWS architecture\nThank you for signing up!.'
    bot.send_message(message.chat.id, tresp)

@bot.message_handler(commands=['status'])
def status(message):
    resp = r.get('https://mglabs.onrender.com/Instancedata/')
    print(resp.status_code)
    data=resp.json()
    tresp = f"Instance Name: {data['InstanceName']} \nInstance ID: {data['InstanceID']}\nStatus: {data['Status']}"
    bot.send_message(message.chat.id, tresp)

@bot.message_handler(commands=['bill'])
def bill(message):
    bot.send_message(message.chat.id, "Fetching data from AWS Servers")
    resp = r.get('https://mglabs.onrender.com/getcostdetails/')
    data=resp.json()
    response = f"DevDash\n\nAWS Billing information\nFrom: {data[0]['Start']}\nTo: {data[0]['End']}\n\nCost as of today:\nYour Total Amount is: {round(float(data[1]['Amount'])*82,2)}INR\n\nPay now by clicking the below link: \n\n With Regards\nDevDash"

    print(response)
    #tresp = f"Instance Name: {data['InstanceName']}\nInstance ID: {data['InstanceID']}\nStatus: {data['Status']}"
    bot.send_message(message.chat.id, response)



print("Polling...")
bot.polling()
    
   
    



# if __name__ == '__main__':
#     while True:
#         hour = time.localtime().tm_hour

#         if hour == 00:
#             timely_update()
#         elif hour==13:
#             timely_update()
#         time.sleep(2)
    
    
