"""Um bot de Telegram que envia fun facts sobre o Sistema Solar."""
import logging

# import os

import random

from messages import facts, help_msg, start_msg, TOKEN, photos

# import telegram

from telegram.ext import CommandHandler, Updater, MessageHandler, Filters

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(bot, update):
    """Responde ao comando '/start'."""
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=start_msg)


def trigger(percentage=15):
    """Calcula probabilidade para resposta automatica."""
    return random.randrange(100) < percentage


def second_trigger(percentage=10):
    """Calcula probabilidade para fotos."""
    return random.randrange(100) < percentage


def random_facts(bot, update):
    """Dispara uma resposta automática."""
    if trigger():
        if second_trigger():
            bot.send_photo(chat_id=update.message.chat_id,
                           photo=random.choice(photos))
        else:
            bot.sendMessage(chat_id=update.message.chat_id,
                            text=random.choice(facts))


def help_cmd(bot, update):
    """Responde ao comando '/help'."""
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=help_msg)


def fun_facts(bot, update):
    """Responde ao comando '/fact', e envia um dos fatos da lista."""
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=random.choice(facts))


def fun_pics(bot, update):
    """Responde ao comando '/pic', e envia uma das imagens da lista."""
    bot.send_photo(chat_id=update.message.chat_id,
                   photo=random.choice(photos))


token = TOKEN
updater = Updater(token)
dispatcher = updater.dispatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
help_handler = CommandHandler('help', help_cmd)
dispatcher.add_handler(help_handler)
facts_handler = CommandHandler('fact', fun_facts)
dispatcher.add_handler(facts_handler)
pic_handler = CommandHandler('pic', fun_pics)
dispatcher.add_handler(pic_handler)
dispatcher.add_handler(MessageHandler(Filters.all, random_facts))

updater.start_polling()
updater.idle()
