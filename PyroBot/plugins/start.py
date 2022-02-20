from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton  
from PyroBot.db.my import *


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Hello there!", reply_markup=ReplyKeyboardMarkup( [ ["A", "B", "C", "D"],["E", "F", "G"],["H", "I"],["J"]], resize_keyboard=True ) )
       


'''

states = {}

captchas = {}

userinfo = {}

def randomString(stringLength=5):

    letters = string.ascii_lowercase

    return ''.join(random.choice(letters) for i in range(stringLength))

def gen_captcha(userid):

    string = randomString()

    data = image.generate(string)

    image.write(string, './captcha/{}.png'.format(str(userid)))

    states[str(userid)+'_captcha'] = string

    print(states[str(userid)+'_captcha'])

def captcha_query(_,message):

    user_id = message.from_user.id

    try:

        a = states[str(user_id)] == 'captcha_true'

    except:

        a = 0

    if a:

        return True

def tg_verify_query(_,query):

    a = query.data

    if 'verify_tg' in a:

        return True 

    else:

        return False

    

def twitter_verify_query(_,query):

    pass

def medium_verify_query(_,query):

    a = query.data

    if 'medium_verify' in a:

        return True

    else:

        return False

def medium_verify_time(_,query):

    a = query.data

    if 'verify_medium_time' in a:

        return True

    else:

        return False

def show_menu(_,query):

    a = query.data

    if a == 'show_menu':

        return True

    else:

        return False

    

def check_bal(_,query):

    a = query.data

    if 'show_balance' in a:

        return True

    else:

        return False

def check_ref(_,query):

    a = query.data

    if a == 'show_referral':

        return True

    else:

        return False

def twitter_verify_(_,query):

    a = query.data

    if 'twitter_verify' in a:

        return True

    else:

        return False

def twitter_input_query(client,message):

    user_id = message.from_user.id

    print(user_id)

    print(states[str(user_id)])

    try:

        state = states[str(user_id)]

    except:

        state = 'None'

    print('State =',state )

    if state == 'twitter_input':

        return True

    else:

        return False

def show_referral(_,query):

    a = query.data

    if 'show_referral' in a:

        return True

    else:

        return False

def show_menu_query(_,query):

    a = query.data

    if 'show_menu' in a:

        return True

    else:

        return False

        
 
@Client.on_message(filters.command(["sta"]))

def start(client,message):

    user_id  = message.from_user.id

    chat_id = message.chat['id']

    try:

        rreffid = int(message.text.split(" ",1)[1])

        rreff = True

    except:

        rreff = False

    try:

        level = userinfo[str(user_id)+'_task_level']

    except:

        user = check_user(user_id)

        if user:

            level = user[5]

            userinfo[str(user_id)+'_task_level'] = level

        else:

            if rreff:

                create_user(user_id,rreffid)

                new_ref(rreffid,user_id)

                try:

                    balance = userinfo[str(rreffid)+'_balance'] 

                except:

                    user = check_user(rreffid)

                    balance = user[5]

                balance = balance + 5

                update_user(rreffid,balance,'n','n','n')

                userinfo[str(rreffid)+'_balance'] = balance

                bot.send_message(chat_id = rreffid,text = 'Congrats you have a referral and have got 5 MTDL tokens!')

                userinfo[str(user_id)+'_task_level'] = 1

                userinfo[str(user_id)+'_total_referrals'] = 0

            else:

                create_user(user_id,'n')

                userinfo[str(user_id)+'_task_level'] = 1

                userinfo[str(user_id)+'_total_referrals'] = 0

            user = check_user(user_id)

            level = user[5]

            userinfo[str(user_id)+'_task_level'] = level

    firstname = Client.get_users(user_id).first_name

    if level == 1:

        message.reply('Hello [{}](tg://user?id={}),\nTo continue please solve the captcha below!'.format(firstname,user_id))

        gen_captcha(user_id)

        bot.send_photo(chat_id = chat_id,photo = './captcha/{}.png'.format(str(user_id)))

        states[str(user_id)] = 'captcha_true'        

    elif level == 2:

        keyboard = [[InlineKeyboardButton("Join Group", url = 'https://t.me/medalte')],

                        [InlineKeyboardButton('Join Channel', url = 'https://t.me/medalteAnn')],

                        [InlineKeyboardButton('Done!', callback_data = 'verify_tg:{}'.format(user_id))]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        message.reply('To be able to participate in the AirDrop you need to complete some tasks.\n\n Firstly join @medalte and @medalteAnn',reply_markup = reply_markup)

    elif level == 3:

        states[str(user_id)] = 'twitter_input'

        keyboard = [[InlineKeyboardButton('Visit Our twitter Page',url = 'https://twitter.com/medaltetoken')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        message.reply('The next task is to visit our twitter profile and follow us,retweet and share our pinned post \nThen Send your username to me without @',reply_markup = reply_markup)

    elif level == 4:

        

        states[str(user_id)] = 'medium_wait_13'

        def change_wait_time(userid):

            import time

            n = 12

            while n >= 0:

                time.sleep(1)

                states[str(userid)] = 'medium_wait_{}'.format(n)

                n = n-1

        t = Thread(target = change_wait_time,args=(user_id,))

        t.start()

        keyboard = [[InlineKeyboardButton('Our medium page!',url = 'https://medium.com/@support_28864')],

            [InlineKeyboardButton("Done!", callback_data = 'verify_medium_time')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        message.reply('Now visit our medium page and like/clap on any one of our posts!',reply_markup  = reply_markup)

    elif level == 5:

        keyboard = [[InlineKeyboardButton('My Token Balance',callback_data = 'show_balance')],[InlineKeyboardButton('Referral link',callback_data = 'show_referral')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        message.reply('Menu:',reply_markup = reply_markup)
'''
