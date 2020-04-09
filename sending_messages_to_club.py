from telegram import Bot
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters

from telegram.utils.request import Request
import json

#THIS IS FOR PASSING ARGUMENTS TO SCRIPT
import sys


#ARGUMENTS TO BE PASSED as testing arguments
arg1 ='club_file_2020-04-07_13:32:55.615214.txt'
arg2 = 'test_image_1.png'


#READING FILE txt as JSON is working okay
with open(sys.argv[1], 'r') as f:
    list_with_user_id = json.loads(f.read())

def main():

    req = Request (
        connect_timeout= 0.5,
        read_timeout= 1.0,
    )

    bot = Bot(
        token="1055794463:AAHjlsw8sK8NNf6vq1bRS2DbiWN2j98CDrc",
        request=req,
        base_url='https://telegg.ru/orig/bot'
    )

    updater = Updater(
        bot=bot,
        use_context=True
    )

    info = bot.get_me()
    print("Confirmation that bot is online")
    print(info)

    for i in range(len(list_with_user_id)):
        bot.send_photo(
            chat_id=list_with_user_id[i],
            photo=open(sys.argv[2], 'rb'),
            caption='This is automatic sending from outside of the script the code of the Bot'

        )
    print('Sending complete')

if __name__ == '__main__':
    main()