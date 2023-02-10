import telebot
from telebot import types

bot = telebot.TeleBot('5619197827:AAH5hKgSGJkjZ9Pv_l1Z-RRKh6rvP1hFtwc')
TO_CHAT_ID = '@YouTubeBirz'
banned_users = [5380685424, 5272676030, 731918546, 1772411051, 297820198, 5710190212, 5657609486, 5828378741]
admin = [1807653203]

joinedFile = open('chatid.txt', 'r')
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

def start_markup():
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton(text='Биржа', url='https://t.me/YouTubeBirz')
    item2 = types.InlineKeyboardButton(text='Проверить✅', callback_data='check1')
    markup.add(item1, item2)
    return markup

@bot.message_handler(commands=["sendall"])
def send(message):
    for user in joinedUsers:
        if message.chat.id in admin:
            bot.send_message(user, message.text[message.text.find(' '):])


@bot.message_handler(commands=["start"])
def start(message):
    if not message.chat.id in joinedUsers:
        joinedFile = open('chatid.txt', 'a')
        joinedFile.write(str(message.chat.id) + '\n')
        joinedUsers.add(message.chat.id)

    bot.send_message(message.chat.id, 'Чтобы пользоваться ботом подпишись на нашу биржу!', reply_markup=start_markup())


def check(call):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id='-1001538332180', user_id=call.message.chat.id).status:
            if call.message.chat.id in banned_users:
                bot.send_message(call.message.chat.id,
                                 "Вы заблокированы в боте⛔ Для разблокировки напишите админу (@EgorSelischev)")
                return True
            else:
                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton('Выложить объявление', callback_data='post1')
                item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/EgorSelischev')
                item2 = types.InlineKeyboardButton('Правила', url='https://telegra.ph/Pravila-ispolzovaniya-12-13')

                markup.add(item, item1, item2)

                bot.send_message(call.message.chat.id,
                                 f'Привет👋 Я менеджер <a href="https://t.me/YouTubeBirz">ютуб-биржи</a>.\nЧтобы выложить объявление, выбери соответсвующий раздел ниже.',
                                 parse_mode='html', reply_markup=markup)
            break

    else:
        bot.send_message(call.message.chat.id, 'Подпишитесь на канал!', reply_markup=start_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'check1':
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
            check(call)

        if call.data == 'post1':
            status = ['creator', 'administrator', 'member']
            for i in status:
                if i == bot.get_chat_member(chat_id='-1001538332180', user_id=call.message.chat.id).status:

                    if call.message.chat.id in banned_users:
                        bot.send_message(call.message.chat.id,
                                         "Вы заблокированы в боте⛔ Для разблокировки напишите админу (@EgorSelischev)")
                        return True
                    else:
                        markup = types.InlineKeyboardMarkup(row_width=1)
                        item = types.InlineKeyboardButton('Выложить объявление', callback_data='post1')
                        item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/EgorSelischev')
                        item2 = types.InlineKeyboardButton('Правила',
                                                           url='https://telegra.ph/Pravila-ispolzovaniya-12-13')

                        markup.add(item, item1, item2)

                        mesg = bot.send_message(call.message.chat.id, 'Чтобы выложить объявление, отправь мне его')
                        bot.register_next_step_handler(mesg, post)

                    break

            else:
                bot.send_message(call.message.chat.id, 'Подпишитесь на канал!', reply_markup=start_markup())


def lrlr(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Выложить объявление', callback_data='post1')
    item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/EgorSelischev')
    item2 = types.InlineKeyboardButton('Правила', url='https://telegra.ph/Pravila-ispolzovaniya-12-13')

    markup.add(item, item1, item2)

    bot.send_message(message.chat.id, 'Пост был успешно опубликован✅', reply_markup=markup)


def post(message):
    status = ['creator', 'administrator', 'member']
    for i in status:
        if i == bot.get_chat_member(chat_id='-1001538332180',
                                    user_id=message.chat.id).status:

            if message.chat.id in banned_users:
                bot.send_message(message.chat.id,
                                 "Вы заблокированы в боте⛔ Для разблокировки напишите админу (@EgorSelischev)")

            else:
                bot.forward_message(TO_CHAT_ID, message.chat.id, message.message_id)
                bot.send_message(1807653203, f'Пост от @{message.from_user.username}')

                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton('Выложить объявление', callback_data='post1')
                item1 = types.InlineKeyboardButton('Поддержка', url='https://t.me/EgorSelischev')
                item2 = types.InlineKeyboardButton('Правила', url='https://telegra.ph/Pravila-ispolzovaniya-12-13')

                markup.add(item, item1, item2)

                bot.send_message(message.chat.id, 'Пост был успешно опубликован✅', reply_markup=markup)

            break
    else:
        bot.send_message(message.chat.id, 'Подпишитесь на канал!',
                         reply_markup=start_markup())

bot.polling(none_stop=True)