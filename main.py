from typing import Counter
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


class MyBot():
    def __init__(self) -> None:
        self.emoji = 'Heavy Check Mark'
        self.counter = 0
        keys = [['شروع برنامه ریزی']]
        self.key = ReplyKeyboardMarkup(keys,resize_keyboard=True)
        keys2 = [[InlineKeyboardButton('شروع برنامه ریزی', callback_data='1')]]
        self.key2 = InlineKeyboardMarkup(keys2)
        keys3 = [[InlineKeyboardButton('متوجه شدم', callback_data='2')]]
        self.key3 = InlineKeyboardMarkup(keys3)
        self.keys4 = []
        self.key5 = InlineKeyboardMarkup(self.keys4)
        delprogram = [[InlineKeyboardButton('لغو برنامه' , callback_data='123456789123456789')],[InlineKeyboardButton('ادامه با برنامه قبلی', callback_data='987654321987654321')]]
        self.delete = InlineKeyboardMarkup(delprogram)

    def start(self, update:Update, context:CallbackContext):
        if len(self.keys4) == 0:
            update.message.reply_text('''به ربات برنامه ریزی خوش آمدید
شما میتوانید در این ربات
برنامه روزانه خود را ذخیره کرده
و پس از انجام هر کار، انجام آن را
ثبت کنید''', reply_markup=self.key2)

        else:
            update.message.reply_text('''شما درحال حاضر یک برنامه نا تمام دارید
لطفا ابتدا آن را به پایان رسانده
و یا برنامه را لغو کنید
سپس دوباره ربات را استارت کنید''', reply_markup=self.delete)



    def Button(self, update:Update, context:CallbackContext):
        query = update.callback_query
        if query.data == '1':
           query.delete_message() 
           query.message.reply_text('''لطفا برنامه خود را به این شکل بنویسید
و پس از کامل شدن ارسال کنید:           

برنامه اول
برنامه دوم
برنامه سوم''', reply_markup=self.key3)

        elif query.data == '2':
            query.delete_message()
            self.counter += 1

        elif query.data == '123456789123456789':
            query.delete_message()
            for i in range(len(self.keys4)):
                for j in self.keys4:
                    self.keys4.remove(j)
            query.message.reply_text('لطفا ربات را دوباره راه اندازی کنید')

        elif query.data == '987654321987654321':
            query.delete_message()

        elif query.data == '963852741963852741':
            for i in range(len(self.keys4)):
                for j in self.keys4:
                    self.keys4.remove(j)
            query.delete_message()
            self.counter = 1        
            query.message.reply_text('لطفا برنامه خود را دوباره بفرستید')             

        elif query.data in self.program_dict_numbers:
            if len(self.keys4) > 1:
                self.index = int(query.data) - 3
                self.keys4.remove([InlineKeyboardButton(self.program_dict_numbers[query.data], callback_data=query.data)])
                query.edit_message_text('برنامه امروز شما', reply_markup=self.key5)
                query.message.reply_text(self.program_dict_numbers[query.data] + "\N{Heavy Check Mark}")
            else:
                self.index = int(query.data) - 3
                self.keys4.remove([InlineKeyboardButton(self.program_dict_numbers[query.data], callback_data=query.data)])
                query.message.reply_text(self.program_dict_numbers[query.data] + "\N{Heavy Check Mark}")    
                query.edit_message_text('شما برنامه خود را با موفقیت به پایان رساندید', reply_markup=self.key5)

            

    def text(self, update:Update, context:CallbackContext):
        string = 'qwertyuiopasdfghjklzxcvbnm,./\1234567890-=!@#$%^&*()_ضصثقفغعهخحجچشسیبلاتنمکگظطزرذدئوژؤژًٌٍريال،؛,][\}{َُِّۀآـ«»:"ةيژؤإأء<>؟'
        if self.counter > 0:
            for i in string:
                if i in update.message.text:
                    program = str(update.message.text).split(sep='\n')
                    self.program_dict = dict()
                    self.program_dict_numbers = dict()
                    self.count = 3
                    for i in program:
                        self.program_dict[i] = str(self.count)
                        self.program_dict_numbers[str(self.count)] = i
                        self.count += 1
                    for i in program:
                        self.keys4.append([InlineKeyboardButton(i, callback_data=self.program_dict.get(i))])
                    break
            self.keys4.append([InlineKeyboardButton('تغییر برنامه', callback_data='963852741963852741')])    
            update.message.reply_text('برنامه امروز شما', reply_markup=self.key5)
            self.counter = 0                     
        else:
            None         
                     



    def main(self):
        updater = Updater("token")
        updater.dispatcher.add_handler(CommandHandler('start', self.start))  
        updater.dispatcher.add_handler(MessageHandler(Filters.text, self.text))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.Button))
        updater.start_polling()
        updater.idle()  


bot = MyBot()
bot.main()        