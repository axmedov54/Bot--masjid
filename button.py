from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder


menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Quran Audio🫀"), KeyboardButton(text="Qibla🕋",web_app=WebAppInfo(url='https://qiblafinder.withgoogle.com/intl/ru/desktop/finder'))],
       [KeyboardButton(text="Xiva Namoz Vaqtlari⏲️"),KeyboardButton(text="Namoz Oqishni Organamiz☪️")] ,
       [KeyboardButton(text="Tongi Zikirlar🤲"),KeyboardButton(text="Tungi Zikirlar🤲")],
       [KeyboardButton(text='Allohnig 99 Ismi'), KeyboardButton(text="tasbih  📿",web_app=WebAppInfo(url='https://www.tasbih.org/'))],
       [KeyboardButton(text='G`usl Olish Tartibi🚿'),KeyboardButton(text='Taxorat Olish Tartibi🚿')],
       [KeyboardButton(text='Xiva Masjidlar Joylashuvi🕌'),KeyboardButton(text='Yangi Masjid Uchun Hayriya🕌')],
       [KeyboardButton(text='Nafil Namozlar☪️')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


nafil=ReplyKeyboardMarkup(
    keyboard=[
        
        [KeyboardButton(text=('Kurbon Xayit Namozi'))],
        [KeyboardButton(text=('Janaza Namozi'))],
        [KeyboardButton(text="ORTGA <-")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)




Shaxarlar = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Andijon'), KeyboardButton(text='Angren')],
        [KeyboardButton(text='Buxoro'), KeyboardButton(text='Guliston')],
        [KeyboardButton(text='Jizzax'), KeyboardButton(text='Qarshi')],
        [KeyboardButton(text='Marg`ilon'), KeyboardButton(text='Namangan')],
        [KeyboardButton(text='Navoiy'), KeyboardButton(text='Nukus')],
        [KeyboardButton(text='Samarqand'), KeyboardButton(text='Termiz')],
        [KeyboardButton(text='Toshkent'), KeyboardButton(text='Urganch')],
        [KeyboardButton(text='Farg`ona'), KeyboardButton(text='Xiva')],
        [KeyboardButton(text='Ortga:')]
    ],
    resize_keyboard=True  # optional: foydalanuvchi interfeysini qulayroq qilish uchun
)



masjid=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=('🕌Said Niyoz Sholikor🕌'))],
        [KeyboardButton(text=('🕌Xasan Basriy🕌'))],
        [KeyboardButton(text=('🕌Kasmabot jomey Masjidi🕌'))],
        [KeyboardButton(text="Ortga<-")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
oqish = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Erkaklar🧔")],
        [KeyboardButton(text="Ayollar🧕")],
        [KeyboardButton(text='ortga🔙')]
    ], resize_keyboard=True,
    one_time_keyboard=True
)

erkaklar= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Bomdod")],
        [KeyboardButton(text="Peshin")],
        [KeyboardButton(text="Asr")],
        [KeyboardButton(text="Shom")],
        [KeyboardButton(text="Xufton")],
        [KeyboardButton(text="Juma Naomzi")],
        [KeyboardButton(text='ortga⬅️')]
    ], resize_keyboard=True,
    one_time_keyboard=True
)
ayollar= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="bomdod")],
        [KeyboardButton(text="peshin")],
        [KeyboardButton(text="asr")],
        [KeyboardButton(text="shom")],
        [KeyboardButton(text="xufton")],
        [KeyboardButton(text='ortga⬅️')]
    ], resize_keyboard=True,
    one_time_keyboard=True
)

gusl= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="erkaklar🧔")],
        [KeyboardButton(text="ayollar🧕")],
        [KeyboardButton(text='ortga🔙')]
    ], resize_keyboard=True,
    one_time_keyboard=True
)

quran1=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Al-Fatiha"), KeyboardButton(text="Al-Baqarah"), KeyboardButton(text="Al-Imran")],
        [KeyboardButton(text="An-Nisa"), KeyboardButton(text="Al-Maidah"), KeyboardButton(text="Al-Anam")],
        [KeyboardButton(text="Al-Araf"), KeyboardButton(text="Al-Anfal"), KeyboardButton(text="At-Tawbah")],
        [KeyboardButton(text="Yunus"), KeyboardButton(text="Hud"), KeyboardButton(text="Yusuf")],
        [KeyboardButton(text="Ar-Rad"), KeyboardButton(text="Ibrahim"), KeyboardButton(text="Al-Hijr")],
        [KeyboardButton(text="An-Nahl"), KeyboardButton(text="Al-Isra"), KeyboardButton(text="Al-Kahf")],
        [KeyboardButton(text="Maryam"), KeyboardButton(text="Ta-Ha"), KeyboardButton(text="Al-Anbiya")],
        [KeyboardButton(text="Al-Hajj"), KeyboardButton(text="Al-Muminun"), KeyboardButton(text="An-Nur")],
        [KeyboardButton(text="Al-Furqan"), KeyboardButton(text="Ash-Shuara"), KeyboardButton(text="An-Naml")],
        [KeyboardButton(text="Al-Qasas"), KeyboardButton(text="Al-Ankabut"), KeyboardButton(text="Ar-Rum")],
        [KeyboardButton(text="Luqman"), KeyboardButton(text="As-Sajda"), KeyboardButton(text="Al-Ahzab")],
        [KeyboardButton(text="Saba"), KeyboardButton(text="Fatir"), KeyboardButton(text="Ya-Sin")],
        [KeyboardButton(text="As-Saffat"), KeyboardButton(text="Sad"), KeyboardButton(text="Az-Zumar")],
        [KeyboardButton(text="Ghafir"), KeyboardButton(text="Fussilat"), KeyboardButton(text="Ash-Shura")],
        [KeyboardButton(text="Az-Zukhruf"), KeyboardButton(text="Ad-Dukhan"), KeyboardButton(text="Al-Jathiya")],
        [KeyboardButton(text="Al-Ahqaf"), KeyboardButton(text="Muhammad"), KeyboardButton(text="Al-Fath")],
        [KeyboardButton(text="Al-Hujurat"), KeyboardButton(text="Qaf"), KeyboardButton(text="Adh-Dhariyat")],
        [KeyboardButton(text="At-Tur"), KeyboardButton(text="An-Najm"), KeyboardButton(text="Al-Qamar")],
        [KeyboardButton(text="Ar-Rahman"), KeyboardButton(text="Al-Waqia"), KeyboardButton(text="Al-Hadid")],
        [KeyboardButton(text="Al-Mujadila"), KeyboardButton(text="Al-Hashr"), KeyboardButton(text="Al-Mumtahina")],
        [KeyboardButton(text="As-Saff"), KeyboardButton(text="Al-Jumua"), KeyboardButton(text="Al-Munafiqun")],
        [KeyboardButton(text="At-Taghabun"), KeyboardButton(text="At-Talaq"), KeyboardButton(text="At-Tahrim")],
        [KeyboardButton(text="Al-Mulk"), KeyboardButton(text="Al-Qalam"), KeyboardButton(text="Al-Haqqa")],
        [KeyboardButton(text="Al-Maarij"), KeyboardButton(text="Nuh"), KeyboardButton(text="Al-Jinn")],
        [KeyboardButton(text="Al-Muzzammil"), KeyboardButton(text="Al-Muddathir"), KeyboardButton(text="Al-Qiyama")],
        [KeyboardButton(text="Al-Insan"), KeyboardButton(text="Al-Mursalat"), KeyboardButton(text="An-Naba")],
        [KeyboardButton(text="An-Naziat"), KeyboardButton(text="Abasa"), KeyboardButton(text="At-Takwir")],
        [KeyboardButton(text="Al-Infitar"), KeyboardButton(text="Al-Mutaffifin"), KeyboardButton(text="Al-Inshiqaq")],
        [KeyboardButton(text="Al-Buruj"), KeyboardButton(text="At-Tariq"), KeyboardButton(text="Al-Ala")],
        [KeyboardButton(text="Al-Ghashiyah"), KeyboardButton(text="Al-Fajr"), KeyboardButton(text="Al-Balad")],
        [KeyboardButton(text="Ash-Shams"), KeyboardButton(text="Al-Layl"), KeyboardButton(text="Ad-Duha")],
        [KeyboardButton(text="Ash-Sharh"), KeyboardButton(text="At-Tin"), KeyboardButton(text="Al-Alaq")],
        [KeyboardButton(text="Al-Qadr"), KeyboardButton(text="Al-Bayyina"), KeyboardButton(text="Az-Zalzala")],
        [KeyboardButton(text="Al-Adiyat"), KeyboardButton(text="Al-Qaria"), KeyboardButton(text="At-Takathur")],
        [KeyboardButton(text="Al-Asr"), KeyboardButton(text="Al-Humaza"), KeyboardButton(text="Al-Fil")],
        [KeyboardButton(text="Quraish"), KeyboardButton(text="Al-Maun"), KeyboardButton(text="Al-Kawthar")],
        [KeyboardButton(text="Al-Kafirun"), KeyboardButton(text="An-Nasr"), KeyboardButton(text="Al-Masad")],
        [KeyboardButton(text="Al-Ikhlas"), KeyboardButton(text="Al-Falaq"), KeyboardButton(text="An-Nas")],
        [KeyboardButton(text='ortga<-')]
    ], resize_keyboard=True,
    one_time_keyboard=True
 )