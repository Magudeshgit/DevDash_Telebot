import telebot
import requests as r
import time

print("Initiating API requests")
bot = telebot.TeleBot("7186208464:AAHkhJl1KDxzBSEeLuEfTVA-ZjzC2OHPqLE")
time.localtime()


@bot.message_handler(commands=['start'])
def initial(message):
    print('asd',message.chat.id)
    #resp = r.get('https://mglabs.onrender.com/Instancedata/')
    #data=resp.json()
    #print(data)
    tresp = message.chat.id
    #tresp = f"Instance Name: {data['InstanceName']}\nInstance ID: {data['InstanceID']}\nStatus: {data['Status']}"
    tresp = 'Welcome to DevDash\n\nAn AWS management application\nYou will receive timely updates regarding your AWS architecture\nThank for signing up!.'
    bot.send_message(message.chat.id, tresp)



print("Polling...")
bot.polling()


def timely_update():
    resp = r.get('https://mglabs.onrender.com/Instancedata/')
    data=resp.json()
    tresp = f"Instance Name: {data['InstanceName']}\nInstance ID: {data['InstanceID']}\nStatus: {data['Status']}"
    bot.send_message(message.chat.id, tresp)



# if __name__ == '__main__':
#     while True:
#         hour = time.localtime().tm_hour

#         if hour == 00:
#             timely_update()
#         elif hour==13:
#             timely_update()
#         time.sleep(2)
    
    
