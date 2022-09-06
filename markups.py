from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
feedback = KeyboardButton('💩 Отзывы')
offer = KeyboardButton('👀 Предложения')
shop = KeyboardButton('🎁 Донат в игру')
helper = KeyboardButton('🆘 Helper')
donate = KeyboardButton('🎉 Поддержать')
links = KeyboardButton('🔗 Ссылки')
useful = KeyboardButton('🚀 Полезное')
friends = KeyboardButton('🤝 Добаление друзей')
support = KeyboardButton('🍺 Поддержать команду 14Karat')
mainMenu.add(shop, helper, links,useful, feedback, offer)

feedbackMenu = InlineKeyboardMarkup(row_width=2)
link1 = InlineKeyboardButton(text='✍️ Оставить отзыв', callback_data='✍️ Оставить отзыв')
item2 = InlineKeyboardButton(text='👀 Посмотреть отзывы', url = 'https://t.me/ACE_14Karat')
feedbackMenu.add(link1, item2)

usefulMenu = InlineKeyboardMarkup(row_width=2)
link1 = InlineKeyboardButton(text='🟢Разное🟢', url = 'https://t.me/AWAKEN_NEWS/65')
item2 = InlineKeyboardButton(text='🟢Промокоды🟢', url = 'https://t.me/AWAKEN_NEWS/630')
usefulMenu.add(link1, item2)

look_feedback_link = InlineKeyboardMarkup(row_width=1)
link1 = InlineKeyboardButton(text='Отзывы', url = 'https://t.me/ACE_14Karat')
look_feedback_link.add(link1)

helperMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
price = KeyboardButton('👀 Прайс')
go_back = KeyboardButton('🔙 Назад')
helperMenu.add(price, go_back)

optionMenu = InlineKeyboardMarkup(row_width=3)
helperButton = InlineKeyboardButton(text='Helper',callback_data='helper')
shopButton = InlineKeyboardButton(text='Shop',callback_data='shop')
anotherButton = InlineKeyboardButton(text='Другое',callback_data='another')
optionMenu.add(helperButton, shopButton, anotherButton)

friendsMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
friends_list = KeyboardButton('📜 Список')
add_yoursef = KeyboardButton('➕ Добавиться в список')
go_back = KeyboardButton('🔙 Назад')
helperMenu.add(friends_list,add_yoursef, go_back)




 


        

        
