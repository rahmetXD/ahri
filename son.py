import telebot
import requests
import random
from datetime import datetime

# Telegram Bot Token'ınızı buraya ekleyin
bot_token = '5855083962:AAECsJm4bHM2sF5u0r4B0mV6djGiCP4pHJs'

# Bot sahibinin kullanıcı ID'si
owner_user_id = 5944841427

# Grupların yasaklı olduğu bir liste oluşturun
blocked_groups = set()

# Botun etkin/pasif durumu
bot_active = False

# Bot nesnesini oluşturun
bot = telebot.TeleBot(bot_token)

# /start komutuna yanıt veren bir işlev
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    user_username = message.from_user.username  # Kullanıcının kullanıcı adını alın

    # İşte düğmeleri eklemek için gerekli olan kod
    markup = telebot.types.InlineKeyboardMarkup()
    btn_bot = telebot.types.InlineKeyboardButton('🎉 ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ 🎉', url='https://t.me/AhriTrBot?startgroup=a')
    btn_owner = telebot.types.InlineKeyboardButton('🛡 ᴏᴡɴᴇʀ 🛡', url='https://t.me/whatdediingulum')
    btn_dev = telebot.types.InlineKeyboardButton('👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀs 👨‍💻', url='https://t.me/rahmetiNC')
    markup.add(btn_bot)
    markup.add(btn_owner)
    markup.add(btn_dev)

    welcome_message = f"👋🏻 ᴍᴇʀʜᴀʙᴀ {user_username}, ʙᴇɴ ᴀʜʀɪ!, ʙᴀᴢı ᴛᴇʟᴇɢʀᴀᴍ ᴇɢ̆ʟᴇɴᴄᴇ ᴠᴇ ʏᴀʀᴀʀʟı ᴋᴏᴍᴜᴛʟᴀʀᴀ sᴀʜɪᴘ ʙɪʀ ʙᴏᴛᴜᴍ.\n\n📚 ᴋᴏᴍᴜᴛʟᴀʀıᴍı ɢᴏ̈ʀᴍᴇᴋ ɪ̇ᴄ̧ɪɴ /help, ᴋᴏᴍᴜᴛᴜɴᴜ ᴋᴜʟʟᴀɴᴀ ʙɪʟɪʀsɪɴɪᴢ."


    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)



# /help komutuna yanıt veren bir işlev
@bot.message_handler(commands=['help'])
def send_welcome(message):
    user_id = message.from_user.id
    user_username = message.from_user.username  # Kullanıcının kullanıcı adını alın

    # İşte düğmeleri eklemek için gerekli olan kod
    markup = telebot.types.InlineKeyboardMarkup()
    btn_dev = telebot.types.InlineKeyboardButton('👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀs 👨‍💻', url='https://t.me/rahmetiNC')
    markup.add(btn_dev)

    help_message = f" ⚙️ Merhaba! İşte komutlarım ⚙️\n\n- /start: Botu başlatır ve hoş geldin mesajını gönderir.\n- /help: Bu yardım mesajını gösterir.\n- /sus: Botu pasif hale getirir.\n- /konus: Botu aktif hale getirir.\n- /blok <grup_id>: Belirli bir grubu yasaklar.\n- /unblok <grup_id>: Belirli bir grubun yasağını kaldırır.\n- /ip <IP_adresi>: IP adresi sorgular.\n- /dns <DOMAİN_adresi>: Domain İp adresi sorgular.\n- /dart: Rastgele dart sonucu üretir.\n- /yas <gg.aa.yyyy>: Doğum tarihinize göre yaşınızı ve doğum gününüzü hesaplar.\n- /burc <gg.aa.yyyy>: Doğum tarihinize göre burcunuzu hesaplar.\n\nNot: Bot sadece gruplarda çalışır ve yasaklı gruplarda komutları kullanamazsınız, Botun sahibiyseniz, /blok ve /unblok komutlarını kullanarak grupları yönetebilirsiniz."


    bot.send_message(message.chat.id, help_message, reply_markup=markup)

# /sus komutuna yanıt veren bir işlev
@bot.message_handler(commands=['sus'])
def deactivate_bot(message):
    global bot_active
    bot_active = False
    bot.reply_to(message, "Bot şu an pasif.")

# /konus komutuna yanıt veren bir işlev
@bot.message_handler(commands=['konus'])
def activate_bot(message):
    global bot_active
    bot_active = True
    bot.reply_to(message, "Bot şu an aktif.")

# /blok komutuna yanıt veren bir işlev
@bot.message_handler(commands=['blok'])
def block_group(message):
    if message.from_user.id == owner_user_id:
        try:
            # Komutla verilen grup ID'sini alın
            group_id = int(message.text.split(' ')[1])
            # Grubu yasaklı gruplar listesine ekleyin
            blocked_groups.add(group_id)
            bot.reply_to(message, f"Grup {group_id} yasaklandı.")
        except (IndexError, ValueError):
            bot.reply_to(message, "Geçersiz komut. Doğru kullanım: /blok <grup_id>")
    else:
        bot.reply_to(message, "Bu komutu kullanma izniniz yok.")

# /unblok komutuna yanıt veren bir işlev
@bot.message_handler(commands=['unblok'])
def unblock_group_command(message):
    if message.from_user.id == owner_user_id:
        try:
            # Komutla verilen grup ID'sini alın
            group_id = int(message.text.split(' ')[1])
            # Grubu yasaklı gruplar listesinden kaldırın
            if group_id in blocked_groups:
                blocked_groups.remove(group_id)
                bot.reply_to(message, f"Grup {group_id} yasağı kaldırıldı.")
            else:
                bot.reply_to(message, f"Grup {group_id} zaten yasaklı değil.")
        except (IndexError, ValueError):
            bot.reply_to(message, "Geçersiz komut. Doğru kullanım: /unblok <grup_id>")
    else:
        bot.reply_to(message, "Bu komutu kullanma izniniz yok.")

# /ip komutuna yanıt veren bir işlev
@bot.message_handler(commands=['ip'])
def ip_sorgu(message):
    try:
        ip = message.text.split()[-1]

        # IP sorgusu işlemi
        response = requests.get(f"http://ip-api.com/json/{ip}").json()

        if response["status"] == "success":
            # IP sorgusu başarılı ise sonucu özelleştirin
            result = "🌐 IP Bilgileri 🌐\n\n"
            result += f"🔹 **IP Adresi:** `{response['query']}`\n"
            result += f"🔹 **Ülke:** `{response['country']}`\n"
            result += f"🔹 **Şehir:** `{response['city']}`\n"
            result += f"🔹 **Posta Kodu:** `{response['zip']}`\n"
            result += f"🔹 **Koordinatlar:** `{response['lat']}, {response['lon']}`\n"

            bot.reply_to(message, result)
        else:
            bot.reply_to(message, "IP sorgusu başarısız oldu.")
    except IndexError:
        bot.reply_to(message, "❌ İşlem Başarısız\n❗️ Lütfen Geçerli Bir IP Adresi Giriniz!\n\nÖrnek: /ip 8.8.8.8")
    except Exception as e:
        bot.reply_to(message, "❌ Bir Hata Oluştu\n\nLütfen Daha Sonra Tekrar Deneyin. . .⏳")

# /dart komutuna yanıt veren bir işlev
@bot.message_handler(commands=['dart'])
def dart_at(message):
    dart_result = random.randint(1, 20)  # 1 ile 20 arasında rastgele bir dart sonucu seçin
    bot.send_message(message.chat.id, f"🎯 Dart Sonucu: {dart_result}")

# /yas komutuna yanıt veren bir işlev
@bot.message_handler(commands=['yas'])
def calculate_age(message):
    try:
        # Komutu kullanan kullanıcının doğum tarihini alın
        birthday_str = message.text.split()[-1]
        birthday = datetime.strptime(birthday_str, "%d.%m.%Y")

        # Şu anki tarihi alın
        current_date = datetime.now()

        # Kullanıcının yaşını hesaplayın
        age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))

        # Doğum gününün ne kadar zaman sonra olduğunu hesaplayın
        next_birthday = datetime(current_date.year, birthday.month, birthday.day)
        if current_date > next_birthday:
            next_birthday = datetime(current_date.year + 1, birthday.month, birthday.day)
        days_until_birthday = (next_birthday - current_date).days

        # Kullanıcıya cevap verin
        reply_message = f"🎈 Sevgili {message.from_user.username},"
        reply_message += f"Şuanda {age} yaşındasın.\n\n"
        reply_message += f"🎂 Doğum Günün {days_until_birthday} gün sonra!"
        bot.reply_to(message, reply_message)
    except ValueError:
        bot.reply_to(message, "❌ Geçersiz tarih formatı! Lütfen doğru bir tarih formatı kullanın (örnek: 30.01.2000)")
    except Exception as e:
        bot.reply_to(message, "❌ Bir hata oluştu:\nLütfen daha sonra tekrar deneyin.")

# /burc komutuna yanıt veren bir işlev
@bot.message_handler(commands=['burc'])
def calculate_zodiac_sign(message):
    try:
        # Komutu kullanan kullanıcının doğum tarihini alın
        birthday_str = message.text.split()[-1]
        birthday = datetime.strptime(birthday_str, "%d.%m.%Y")

        # Burçları ve tarih aralıklarını tanımlayın
        zodiac_signs = [
            {"name": "Koç", "start_date": datetime(birthday.year, 3, 21), "end_date": datetime(birthday.year, 4, 19)},
            {"name": "Boğa", "start_date": datetime(birthday.year, 4, 20), "end_date": datetime(birthday.year, 5, 20)},
            {"name": "İkizler", "start_date": datetime(birthday.year, 5, 21), "end_date": datetime(birthday.year, 6, 20)},
            {"name": "Yengeç", "start_date": datetime(birthday.year, 6, 21), "end_date": datetime(birthday.year, 7, 22)},
            {"name": "Aslan", "start_date": datetime(birthday.year, 7, 23), "end_date": datetime(birthday.year, 8, 22)},
            {"name": "Başak", "start_date": datetime(birthday.year, 8, 23), "end_date": datetime(birthday.year, 9, 22)},
            {"name": "Terazi", "start_date": datetime(birthday.year, 9, 23), "end_date": datetime(birthday.year, 10, 22)},
            {"name": "Akrep", "start_date": datetime(birthday.year, 10, 23), "end_date": datetime(birthday.year, 11, 21)},
            {"name": "Yay", "start_date": datetime(birthday.year, 11, 22), "end_date": datetime(birthday.year, 12, 21)},
            {"name": "Oğlak", "start_date": datetime(birthday.year, 12, 22), "end_date": datetime(birthday.year, 1, 19)},
            {"name": "Kova", "start_date": datetime(birthday.year, 1, 20), "end_date": datetime(birthday.year, 2, 18)},
            {"name": "Balık", "start_date": datetime(birthday.year, 2, 19), "end_date": datetime(birthday.year, 3, 20)},
        ]

        # Kullanıcının burcunu bulun
        zodiac_sign = None
        for sign in zodiac_signs:
            if sign["start_date"] <= birthday <= sign["end_date"]:
                zodiac_sign = sign["name"]
                break

        if zodiac_sign:
            bot.reply_to(message, f"🌟 {birthday_str} Tarihinde Doğduğunuza Göre burcunuz: {zodiac_sign}")
        else:
            bot.reply_to(message, "❌ Geçersiz tarih veya burç hesaplanamadı.")
    except ValueError:
        bot.reply_to(message, "❌ Geçersiz tarih formatı! Lütfen doğru bir tarih formatı kullanın (örnek: 30.01.2000)")
    except Exception as e:
        bot.reply_to(message, "❌ Bir hata oluştu:\nLütfen daha sonra tekrar deneyin.")

# Diğer komutları ekleyin
# /hava, /dns veya diğer komutları buraya ekleyebilirsiniz.

# Yasaklanan bir grupta botu kullanmak isteyenlere yanıt veren bir işlev
@bot.message_handler(func=lambda message: message.chat.id in blocked_groups)
def send_blocked_group_message(message):
    bot.reply_to(message, "Bu grupta komutları kullanmak yasaklandı. Lütfen yöneticiye başvurun veya /unblok komutuyla yasağı kaldırın.")

# Tüm mesajlara yanıt veren bir işlev
@bot.message_handler(func=lambda message: bot_active)
def echo_all(message):
    try:
        # Eğer kullanıcı yasaklı bir gruptan mesaj gönderiyorsa hata mesajı gönder
        if message.chat.id in blocked_groups:
            bot.reply_to(message, "Bu grupta komutları kullanmak yasaklandı. Lütfen /unblok komutuyla yasağı kaldırın.")
        else:
            bot.send_message(message.chat.id, message.text)
    except Exception as e:
        error_message = "Bir hata oluştu: {}".format(e)
        bot.send_message(message.chat.id, error_message)

# /dns komutunu işleyin
@bot.message_handler(commands=['dns'])
def dns_sorgu(message):
    try:
        domain = message.text.split()[-1]

        # DNS sorgusu işlemi
        response = requests.get(f"http://ip-api.com/json/{domain}").json()

        if response["status"] == "success":
            # DNS sorgusu başarılı ise sonucu özelleştirin
            result = "🌐 DNS Sorgusu 🌐\n\n"
            result += f"🔹 **Domain Adı:** `{domain}`\n"
            result += f"🔹 **IP Adresi:** `{response['query']}`\n"

            bot.reply_to(message, result, parse_mode='Markdown')
        else:
            bot.reply_to(message, "❌ DNS sorgusu başarısız oldu veya bu domain için herhangi bir IP adresi bulunamadı.")
    except IndexError:
        bot.reply_to(message, "❌ İşlem Başarısız\n❗️ Lütfen Geçerli Bir Domain Adı Giriniz!\n\nÖrnek: /dns example.com")
    except Exception as e:
        bot.reply_to(message, f"❌ Bir Hata Oluştu\n\nHata Detayı: {str(e)}")

@bot.message_handler(commands=['dart'])
def dart_at(message):
    dart_result = random.randint(1, 20)  # 1 ile 20 arasında rastgele bir dart sonucu seçin
    bot.send_message(message.chat.id, f"🎯 Dart Sonucu: {dart_result}")

# /alive komutuna yanıt veren bir işlev
@bot.message_handler(commands=['alive'])
def alive(message):
    user_username = message.from_user.username  # Kullanıcının kullanıcı adını alın

    # "Hey gardaş (username), bot aktif!" mesajını gönderin
    bot.send_message(message.chat.id, f"Hey gardaş {user_username}, bot aktif!")

# Bot'u çalıştırın
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        pass  # Hata mesajlarını yöneticiye bildirmemek için herhangi bir işlem yapmayın
