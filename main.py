'''БОТ КОНВЕРТЕР ВАЛЮТ'''
import requests
import telebot
import json
from config import TOKEN,curency
from utils import CurrensyConverter, ConversionExeption


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def help(message: telebot.types.Message):
    text = 'Для того чтобы начать работу введите команду в следующем формате: \n--> имя валюты \ в какую ' \
           'валюту перевести \ количество переводимой валюты. \n \n Увидеть список доступных валют /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for curenc in curency.keys():
        text = '\n -'.join((text, curenc,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConversionExeption('Не верное количестко параметров.')

        quote, base, amount = values
        total_base = CurrensyConverter.get_pryce(quote, base, amount) * float(amount)
    except ConversionExeption as e:
        bot.reply_to(message, f'Ошибка \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
