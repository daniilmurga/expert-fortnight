from logging import getLogger

from telegram import Bot
from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.utils.request import Request

from archive_bot.config import load_config
from archive_bot.db import init_db
from archive_bot.db import add_message
from archive_bot.db import change_status
from archive_bot.db import count_messages
from archive_bot.db import list_messages

#IMPORTING BUTTONS FROM BUTTONS FILE
import archive_bot.buttons as bt

#IMPORTING TEXT FROM TEXT FILE
import archive_bot.texts as tx

from archive_bot.utils import debug_requests


logger = getLogger(__name__)

COMMAND_COUNT = 'count'
COMMAND_LIST = 'list'


def debug_requests(f):
    """ Декоратор для отладки событий от телеграма
        Логгер подключается в самый последний момент чтобы быть уверенными в том, что конфиг логирования уже загружен
    """
    from logging import getLogger
    logger = getLogger(__name__)

    def inner(*args, **kwargs):
        try:
            logger.debug('Обращение в функцию {}'.format(f.__name__))
            return f(*args, **kwargs)
        except Exception:
            logger.exception('Ошибка в обработчике {}'.format(f.__name__))
            raise

    return inner


#ETOT KUSOK STRANNOGO KODA HRENOGO RABOTAET bt.[TILES] NO
#RABOTAET ETOT KUSOK bt.TILES[bt.CALLBACK_BUTTON1]
@debug_requests
def get_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON1], callback_data=COMMAND_COUNT),
            ],
            [
                InlineKeyboardButton(text=bt.CALLBACK_BUTTON2, callback_data=COMMAND_LIST),
            ],
        ],
    )
@debug_requests
def get_keyboard_1():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON1], callback_data=bt.CALLBACK_BUTTON1)
            ],
        ],
    )

@debug_requests
def get_keyboard_2():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON2], callback_data=bt.CALLBACK_BUTTON2)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON3], callback_data=bt.CALLBACK_BUTTON3)
            ],
        ],
    )
@debug_requests
def get_keyboard_3():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON4], callback_data=bt.CALLBACK_BUTTON4)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON5], callback_data=bt.CALLBACK_BUTTON5)
            ],
        ],
    )

@debug_requests
def get_keyboard_4():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON6], callback_data=bt.CALLBACK_BUTTON6)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON7], callback_data=bt.CALLBACK_BUTTON7)
            ],
        ],
    )

@debug_requests
def get_keyboard_5():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON8], callback_data=bt.CALLBACK_BUTTON8)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON9], callback_data=bt.CALLBACK_BUTTON9)
            ],
        ],
    )

@debug_requests
def get_keyboard_6():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON10], callback_data=bt.CALLBACK_BUTTON10)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON11], callback_data=bt.CALLBACK_BUTTON11)
            ],
        ],
    )

@debug_requests
def get_keyboard_7():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON12], callback_data=bt.CALLBACK_BUTTON12)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON13], callback_data=bt.CALLBACK_BUTTON13)
            ],
        ],
    )

@debug_requests
def get_keyboard_8():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON14], callback_data=bt.CALLBACK_BUTTON14)
            ],
        ],
    )

@debug_requests
def get_keyboard_9():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON15], callback_data=bt.CALLBACK_BUTTON15)
            ],
        ],
    )

@debug_requests
def get_keyboard_10():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON16], callback_data=bt.CALLBACK_BUTTON16)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON17], callback_data=bt.CALLBACK_BUTTON17)
            ],
        ],
    )

@debug_requests
def get_keyboard_11():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON18], callback_data=bt.CALLBACK_BUTTON18)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON19], callback_data=bt.CALLBACK_BUTTON19)
            ],
        ],
    )

@debug_requests
def get_keyboard_12():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON20], callback_data=bt.CALLBACK_BUTTON20)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON21], callback_data=bt.CALLBACK_BUTTON21)
            ],
        ],
    )

@debug_requests
def get_keyboard_13():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON22], callback_data=bt.CALLBACK_BUTTON22)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON23], callback_data=bt.CALLBACK_BUTTON23)
            ],
        ],
    )

@debug_requests
def get_keyboard_14():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON24], callback_data=bt.CALLBACK_BUTTON24)
            ],
            [
                InlineKeyboardButton(bt.TILES[bt.CALLBACK_BUTTON25], callback_data=bt.CALLBACK_BUTTON25)
            ],
        ],
    )


@debug_requests
def message_handler(update: Update, context:CallbackContext):
    user = update.effective_user
    if user:
        name = user.first_name
    else:
        name = 'Anonimus'

    text = update.effective_message.text
    reply_text = 'Привет {} \nТвое сообщение \n\n {}'.format(name, text)

    update.message.reply_text(
        text=tx.text1,
        reply_markup=get_keyboard_1()
    )

    if text:
        add_message(
            user_id=user.id,
            text=text
        )


@debug_requests
def callback_handler(update: Update, callback: CallbackContext):
    callback_data = update.callback_query.data
    user = update.effective_user
    print(user.id)
    if callback_data == bt.CALLBACK_BUTTON1:
        add_message(
            user_id=user.id,
            text=bt.CALLBACK_BUTTON1,
        )
        update.effective_message.reply_text(
            text=tx.text2,
            reply_markup= get_keyboard_2(),
        )
    elif callback_data == bt.CALLBACK_BUTTON2:
        update.callback_query.edit_message_text(
            text=tx.text3,
            reply_markup=get_keyboard_3(),
        )
    elif callback_data == bt.CALLBACK_BUTTON3:
        update.callback_query.edit_message_text(
            text=tx.text2,
            reply_markup=get_keyboard_1(),
        )
    elif callback_data == bt.CALLBACK_BUTTON4:
        update.effective_message.reply_text(
            text=tx.text4,
            reply_markup=get_keyboard_4(),
        )
    elif callback_data == bt.CALLBACK_BUTTON5:
        update.effective_message.reply_text(
            text=tx.text2,
            reply_markup=get_keyboard_2(),
        )
    elif callback_data == bt.CALLBACK_BUTTON6:
        update.effective_message.reply_text(
            text=tx.text5,
            reply_markup=get_keyboard_5(),
        )
    elif callback_data == bt.CALLBACK_BUTTON7:
        update.effective_message.reply_text(
            text=tx.text3,
            reply_markup=get_keyboard_3(),
        )
    elif callback_data == bt.CALLBACK_BUTTON8:
        update.effective_message.reply_text(
            text=tx.text6,
            reply_markup=get_keyboard_6(),
        )
    elif callback_data == bt.CALLBACK_BUTTON9:
        update.effective_message.reply_text(
            text=tx.text9,
            reply_markup=get_keyboard_9(),
        )
    elif callback_data == bt.CALLBACK_BUTTON10:
        update.effective_message.reply_text(
            text=tx.text7,
            reply_markup=get_keyboard_7(),
        )
    elif callback_data == bt.CALLBACK_BUTTON11:
        update.effective_message.reply_text(
            text=tx.text5,
            reply_markup=get_keyboard_5(),
        )
    elif callback_data == bt.CALLBACK_BUTTON12:
        update.effective_message.reply_text(
            text=tx.text8,
            reply_markup=get_keyboard_8(),
        )
    elif callback_data == bt.CALLBACK_BUTTON13:
        update.effective_message.reply_text(
            text=tx.text6,
            reply_markup=get_keyboard_6(),
        )
    elif callback_data == bt.CALLBACK_BUTTON14:
        update.effective_message.reply_text(
            text=tx.text14,
            reply_markup=get_keyboard_14(),
        )
    elif callback_data == bt.CALLBACK_BUTTON15:
        update.effective_message.reply_text(
            text=tx.text10,
            reply_markup=get_keyboard_10(),
        )
    elif callback_data == bt.CALLBACK_BUTTON16:
        update.effective_message.reply_text(
            text=tx.text11,
            reply_markup=get_keyboard_11(),
        )
    elif callback_data == bt.CALLBACK_BUTTON17:
        update.effective_message.reply_text(
            text=tx.text9,
            reply_markup=get_keyboard_9(),
        )
    elif callback_data == bt.CALLBACK_BUTTON18:
        update.effective_message.reply_text(
            text=tx.text12,
            reply_markup=get_keyboard_12(),
        )
    elif callback_data == bt.CALLBACK_BUTTON19:
        update.effective_message.reply_text(
            text=tx.text10,
            reply_markup=get_keyboard_10(),
        )
    elif callback_data == bt.CALLBACK_BUTTON20:
        update.effective_message.reply_text(
            text=tx.text13,
            reply_markup=get_keyboard_13(),
        )
    elif callback_data == bt.CALLBACK_BUTTON21:
        update.effective_message.reply_text(
            text=tx.text11,
            reply_markup=get_keyboard_11(),
        )
    elif callback_data == bt.CALLBACK_BUTTON22:
        update.effective_message.reply_text(
            text=tx.text14,
            reply_markup=get_keyboard_14(),
        )
    elif callback_data == bt.CALLBACK_BUTTON23:
        update.effective_message.reply_text(
            text=tx.text12,
            reply_markup=get_keyboard_12(),
        )
    #FINAL PART NEEDS TO BE REWORKED
    elif callback_data == bt.CALLBACK_BUTTON24:
        change_status(
            user_id=user.id,
            text='CHANGE OF STATUS',
            member=1,
        )
        update.effective_message.reply_text(
            text='Теперь ты один из участников клуба трейдеров. Жди информацию о моих сделках',
            reply_markup=get_keyboard_14(),
        )
    elif callback_data == bt.CALLBACK_BUTTON25:
        update.effective_message.reply_text(
            text='Данная функция в процесее разработки.\nСейчас вы можете лично задать вопрос админу xD',
            reply_markup=get_keyboard_14(),
        )
        #count = count_messages(user_id=user.id)
        #text = tx.text1
        #text = 'У вас {} сообщений. Читайте'.format(count)
    #elif callback_data == COMMAND_LIST:
    #    messages = list_messages(user_id=user.id, limit=5)
    #    text = 'Вы написали вот эти сообщения к нам в базу данных \n\n {}'.format(messages)
    else:
        text = 'Произошла ошибка'
        update.effective_message.reply_text(
            text=text
        )

@debug_requests
def main():
    print("Starting bot with SQL \n Starting new Era")

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
    print(info)

    init_db()

    updater.dispatcher.add_handler(MessageHandler(Filters.all, message_handler))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()