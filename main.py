import os
from telebot import types, TeleBot, logger
import markups as nav
from menu_data import *
from tg_token import BOT_TOKEN, APP_URL
from flask import Flask, request
import logging



gobot = TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger.setLevel(logging.DEBUG)

CHANNEL_URL = '@ACE_14Karat'

@gobot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        photo=open('./content/img/photo_2022-08-17_12-05-22.jpg', 'rb')
        gobot.send_photo(message.chat.id, photo,start_message.format(message.from_user), parse_mode='html', reply_markup=nav.mainMenu)

@gobot.callback_query_handler(func=lambda call:True)
def call_feedback(call):
        if call.data == '✍️ Оставить отзыв':
                send = gobot.send_message(call.message.chat.id, 'Напишите пожалуйста ваш отзыв\n\nПри написании отзыва соблюдайте несколько простых правил:\n\n- Напишите ваш отзыв в одном сообщении\n(для перехода на новую строку используйте shift+enter)\n\n- Не употребляйте мат и оскорбления\n\n- Минимальная длина сообщения 20 символов')
                gobot.register_next_step_handler(send, user_feedback_message)


def user_feedback_message(message):
        if(len(message.text) < 20):
                gobot.send_message(message.from_user.id, "Отзыв слишком короткий 🔄 (минимум 20 символов)")
        else:        
                gobot.forward_message(CHANNEL_URL,message.chat.id, message.message_id)
    
@gobot.message_handler(content_types=['text'])
def get_user_text(message):
        if message.chat.type == 'private':
                if message.text == '💩 Отзывы':
                        gobot.send_message(message.chat.id, feedback_message, reply_markup=nav.feedbackMenu)
                 
                elif message.text == '👀 Посмотреть отзывы':
                        gobot.send_message(message.chat.id,'adadad', reply_markup=nav.look_feedback_link)

                elif message.text == '👀 Предложения':
                        gobot.send_message(message.chat.id, offer_message)

                elif message.text == '🎁 Донат в игру':
                        photo=open('./content/img/photo_2022-06-21_10-41-39.jpg', 'rb')
                        gobot.send_photo(message.chat.id, photo, shop_message)

                elif message.text == '🔗 Ссылки':
                        gobot.send_message(message.chat.id, links_message, parse_mode='html', disable_web_page_preview=True)

                elif message.text == '🆘 Helper':
                        photo=open('./content/img/hlp.png', 'rb')
                        gobot.send_photo(message.chat.id, photo, helper_message,reply_markup=nav.helperMenu)

                elif message.text == '🚀 Полезное':
                        gobot.send_message(message.chat.id, useful_message,parse_mode='html', disable_web_page_preview=True,reply_markup=nav.usefulMenu)

                elif any(message.text in it for it in promocodes_words )  :
                        gobot.send_message(message.chat.id, promocodes, parse_mode='html', disable_web_page_preview=True)

                elif message.text == '👀 Прайс':
                        photo=open('./content/img/photo_2022-08-17_17-19-41.jpg', 'rb')
                        gobot.send_photo(message.chat.id, photo, price_message)

                elif message.text == '🔙 Назад':
                        photo=open('./content/img/photo_2022-08-17_12-05-22.jpg', 'rb')
                        gobot.send_photo(message.chat.id, photo, reply_markup=nav.mainMenu)
                
                elif any(message.text in it for it in hello_words ): 
                        photo=open('./content/img/photo_2022-08-17_12-05-22.jpg', 'rb')
                        gobot.send_photo(message.chat.id, photo,hello_message.format(message.from_user), parse_mode='html')

                else:
                        gobot.send_message(message.chat.id, short_hello_message.format(message.from_user), parse_mode='html')

        elif message.chat.type == 'supergroup':
                if message.text.lower() in promocodes_words :
                        gobot.reply_to(message, text=promocodes, parse_mode='html', disable_web_page_preview=True)

                elif message.text.lower() in last_update_words:
                        gobot.reply_to(message, text=last_update_link, parse_mode='html', disable_web_page_preview=True)
                        

@server.route(f'/{BOT_TOKEN}', methods=['POST'])
def redirect_message():
        json_string = request.get_data().decode("utf-8")
        update = types.Update.de_json(json_string)
        gobot.process_new_updates([update])
        return '!', 200


if __name__ == '__main__':
    gobot.remove_webhook()
    gobot.set_webhook(url=APP_URL)
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
