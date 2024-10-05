
import asyncio
import logging
import sys
import sqlite3
from aiogram import Bot, Dispatcher, html, F,types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import BOT_TOKEN as token
from button import *
import requests

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()




@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu Aleykum, {html.bold(message.from_user.full_name)}!", reply_markup=menyu)

@dp.message(F.text=='Xiva Masjidlar Joylashuvi🕌')
async def echo_handler(message: Message) -> None:
    await message.answer(text="Masjidlar", reply_markup=masjid)

url = " https://islomapi.uz/api/present/week?region=Xiva"
response = requests.get(url).json()
for i in response:
     region=i['region']
     date=i['date'][1:10]
     hafta=i['weekday']
     xijriy_sana=i['hijri_date']['month']
     tong=i['times']['tong_saharlik']
     quyosh=i['times']['quyosh']
     peshin=i['times']['peshin']
     asr=i['times']['asr']
     shom_iftor=i['times']['shom_iftor']
     hufton=i['times']['hufton']

url1 = " https://islomapi.uz/api/present/week?region=Toshkent"
response = requests.get(url1).json()
for i in response:
     region1=i['region']
     date1=i['date'][1:11]
     hafta1=i['weekday']
     xijriy_sana1=i['hijri_date']['month']
     tong1=i['times']['tong_saharlik']
     quyosh1=i['times']['quyosh']
     peshin1=i['times']['peshin']
     asr1=i['times']['asr']
     shom_iftor1=i['times']['shom_iftor']
     hufton1=i['times']['hufton']


url2 = " https://islomapi.uz/api/present/week?region=Andijon"
response = requests.get(url2).json()
for i in response:
     region2=i['region']
     date2=i['date'][1:10]
     hafta2=i['weekday']
     xijriy_sana2=i['hijri_date']['month']
     tong2=i['times']['tong_saharlik']
     quyosh2=i['times']['quyosh']
     peshin2=i['times']['peshin']
     asr2=i['times']['asr']
     shom_iftor2=i['times']['shom_iftor']
     hufton2=i['times']['hufton']

url3 = " https://islomapi.uz/api/present/week?region=Angren"
response = requests.get(url3).json()
for i in response:
     region3=i['region']
     date3=i['date'][1:10]
     hafta3=i['weekday']
     xijriy_sana3=i['hijri_date']['month']
     tong3=i['times']['tong_saharlik']
     quyosh3=i['times']['quyosh']
     peshin3=i['times']['peshin']
     asr3=i['times']['asr']
     shom_iftor3=i['times']['shom_iftor']
     hufton3=i['times']['hufton']


url4 = " https://islomapi.uz/api/present/week?region=Buxoro"
response = requests.get(url4).json()
for i in response:
     region4=i['region']
     date4=i['date'][1:10]
     hafta4=i['weekday']
     xijriy_sana4=i['hijri_date']['month']
     tong4=i['times']['tong_saharlik']
     quyosh4=i['times']['quyosh']
     peshin4=i['times']['peshin']
     asr4=i['times']['asr']
     shom_iftor4=i['times']['shom_iftor']
     hufton4=i['times']['hufton']


url5 = " https://islomapi.uz/api/present/week?region=Guliston"
response = requests.get(url5).json()
for i in response:
     region5=i['region']
     date5=i['date'][1:10]
     hafta5=i['weekday']
     xijriy_sana5=i['hijri_date']['month']
     tong5=i['times']['tong_saharlik']
     quyosh5=i['times']['quyosh']
     peshin5=i['times']['peshin']
     asr5=i['times']['asr']
     shom_iftor5=i['times']['shom_iftor']
     hufton5=i['times']['hufton'] 


url6 = " https://islomapi.uz/api/present/week?region=Jizzax"
response = requests.get(url6).json()
for i in response:
     region6=i['region']
     date6=i['date'][1:10]
     hafta6=i['weekday']
     xijriy_sana6=i['hijri_date']['month']
     tong6=i['times']['tong_saharlik']
     quyosh6=i['times']['quyosh']
     peshin6=i['times']['peshin']
     asr6=i['times']['asr']
     shom_iftor6=i['times']['shom_iftor']
     hufton6=i['times']['hufton']


url7 = " https://islomapi.uz/api/present/week?region=Qarshi"
response = requests.get(url7).json()
for i in response:
     region7=i['region']
     date7=i['date'][1:10]
     hafta7=i['weekday']
     xijriy_sana7=i['hijri_date']['month']
     tong7=i['times']['tong_saharlik']
     quyosh7=i['times']['quyosh']
     peshin7=i['times']['peshin']
     asr7=i['times']['asr']
     shom_iftor7=i['times']['shom_iftor']
     hufton7=i['times']['hufton']



url8 = " https://islomapi.uz/api/present/week?region=Marg'ilon"
response = requests.get(url8).json()
for i in response:
     region8=i['region']
     date8=i['date'][1:10]
     hafta8=i['weekday']
     xijriy_sana8=i['hijri_date']['month']
     tong8=i['times']['tong_saharlik']
     quyosh8=i['times']['quyosh']
     peshin8=i['times']['peshin']
     asr8=i['times']['asr']
     shom_iftor8=i['times']['shom_iftor']
     hufton8=i['times']['hufton']


url9 = " https://islomapi.uz/api/present/week?region=Namangan"
response = requests.get(url9).json()
for i in response:
     region9=i['region']
     date9=i['date'][1:10]
     hafta9=i['weekday']
     xijriy_sana9=i['hijri_date']['month']
     tong9=i['times']['tong_saharlik']
     quyosh9=i['times']['quyosh']
     peshin9=i['times']['peshin']
     asr9=i['times']['asr']
     shom_iftor9=i['times']['shom_iftor']
     hufton9=i['times']['hufton'] 

url10 = " https://islomapi.uz/api/present/week?region=Navoiy"
response = requests.get(url10).json()
for i in response:
     region10=i['region']
     date10=i['date'][1:10]
     hafta10=i['weekday']
     xijriy_sana10=i['hijri_date']['month']
     tong10=i['times']['tong_saharlik']
     quyosh10=i['times']['quyosh']
     peshin10=i['times']['peshin']
     asr10=i['times']['asr']
     shom_iftor10=i['times']['shom_iftor']
     hufton10=i['times']['hufton']


url11 = " https://islomapi.uz/api/present/week?region=Nukus"
response = requests.get(url11).json()
for i in response:
     region11=i['region']
     date11=i['date'][1:10]
     hafta11=i['weekday']
     xijriy_sana11=i['hijri_date']['month']
     tong11=i['times']['tong_saharlik']
     quyosh11=i['times']['quyosh']
     peshin11=i['times']['peshin']
     asr11=i['times']['asr']
     shom_iftor11=i['times']['shom_iftor']
     hufton11=i['times']['hufton'] 


url12 = " https://islomapi.uz/api/present/week?region=Samarqand"
response = requests.get(url12).json()
for i in response:
     region12=i['region']
     date12=i['date'][1:10]
     hafta12=i['weekday']
     xijriy_sana12=i['hijri_date']['month']
     tong12=i['times']['tong_saharlik']
     quyosh12=i['times']['quyosh']
     peshin12=i['times']['peshin']
     asr12=i['times']['asr']
     shom_iftor12=i['times']['shom_iftor']
     hufton12=i['times']['hufton']


url13 = " https://islomapi.uz/api/present/week?region=Termiz"
response = requests.get(url13).json()
for i in response:
     region13=i['region']
     date13=i['date'][1:10]
     hafta13=i['weekday']
     xijriy_sana13=i['hijri_date']['month']
     tong13=i['times']['tong_saharlik']
     quyosh13=i['times']['quyosh']
     peshin13=i['times']['peshin']
     asr13=i['times']['asr']
     shom_iftor13=i['times']['shom_iftor']
     hufton13=i['times']['hufton'] 

url14 = " https://islomapi.uz/api/present/week?region=Urganch"
response = requests.get(url14).json()
for i in response:
     region14=i['region']
     date14=i['date'][1:10]
     hafta14=i['weekday']
     xijriy_sana14=i['hijri_date']['month']
     tong14=i['times']['tong_saharlik']
     quyosh14=i['times']['quyosh']
     peshin14=i['times']['peshin']
     asr14=i['times']['asr']
     shom_iftor14=i['times']['shom_iftor']
     hufton14=i['times']['hufton']


url15 = " https://islomapi.uz/api/present/week?region=Farg'ona"
response = requests.get(url15).json()
for i in response:
     region15=i['region']
     date15=i['date'][1:10]
     hafta15=i['weekday']
     xijriy_sana15=i['hijri_date']['month']
     tong15=i['times']['tong_saharlik']
     quyosh15=i['times']['quyosh']
     peshin15=i['times']['peshin']
     asr15=i['times']['asr']
     shom_iftor15=i['times']['shom_iftor']
     hufton15=i['times']['hufton']

@dp.message(F.text=='Urganch')
async def shaxar1(message: Message):
    await message.answer(f"""🌃Shaxar: {region14}\n
  🌃 Kun: {date14}\n
  🌃 Hafta: {hafta14}\n
  🌃 Xijriy-Sana: { xijriy_sana14}\n
  🌃 Bomdod vaqti {tong14} 🕰\n
  🌇 Quyosh vaqti {quyosh14} 🕰\n
  🏞  peshin vaqti {peshin14} 🕰\n
  🌇 asr vaqti {asr14} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor14} 🕰\n
  🌃 hufton vaqti {hufton14} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Andijon')
async def shaxar1(message: Message):
    await message.answer(f"""🌃Shaxar: {region2}\n
  🌃 Kun: {date2}\n
  🌃 Hafta: {hafta2}\n
  🌃 Xijriy-Sana: { xijriy_sana2}\n
  🌃 Bomdod vaqti {tong2} 🕰\n
  🌇 Quyosh vaqti {quyosh2} 🕰\n
  🏞  peshin vaqti {peshin2} 🕰\n
  🌇 asr vaqti {asr2} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor2} 🕰\n
  🌃 hufton vaqti {hufton2} 🕰\n
    """,reply_markup=Shaxarlar)


@dp.message(F.text=='Angren')
async def shaxar1(message: Message):
    await message.answer(f"""🌃Shaxar: {region3}\n
  🌃 Kun: {date3}\n
  🌃 Hafta: {hafta3}\n
  🌃 Xijriy-Sana: { xijriy_sana3}\n
  🌃 Bomdod vaqti {tong3} 🕰\n
  🌇 Quyosh vaqti {quyosh3} 🕰\n
  🏞  peshin vaqti {peshin3} 🕰\n
  🌇 asr vaqti {asr3} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor3} 🕰\n
  🌃 hufton vaqti {hufton3} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Buxoro')
async def shaxar1(message: Message):
   await message.answer(f"""🌃Shaxar: {region4}\n
  🌃 Kun: {date4}\n
  🌃 Haftab: {hafta4}\n
  🌃 Xijriy-Sana: { xijriy_sana4}\n
  🌃 Bomdod vaqti {tong4} 🕰\n
  🌇 Quyosh vaqti {quyosh4} 🕰\n
  🏞  peshin vaqti {peshin4} 🕰\n
  🌇 asr vaqti {asr4} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor4} 🕰\n
  🌃 hufton vaqti {hufton4} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Guliston')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region5}\n
  🌃 Kun: {date5}\n
  🌃 Hafta: {hafta}\n
  🌃 Xijriy-Sana: { xijriy_sana5}\n
  🌃 Bomdod vaqti {tong5} 🕰\n
  🌇 Quyosh vaqti {quyosh5} 🕰\n
  🏞  peshin vaqti {peshin5} 🕰\n
  🌇 asr vaqti {asr5} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor5} 🕰\n
  🌃 hufton vaqti {hufton5} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Jizzax')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region6}\n
  🌃 Kun: {date6}\n
  🌃 Hafta: {hafta6}\n
  🌃 Xijriy-Sana: { xijriy_sana6}\n
  🌃 Bomdod vaqti {tong6} 🕰\n
  🌇 Quyosh vaqti {quyosh6} 🕰\n
  🏞  peshin vaqti {peshin6} 🕰\n
  🌇 asr vaqti {asr6} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor6} 🕰\n
  🌃 hufton vaqti {hufton6} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Qarshi')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region7}\n
  🌃 Kun: {date7}\n
  🌃 Haftab: {hafta7}\n
  🌃 Xijriy-Sana: { xijriy_sana7}\n
  🌃 Bomdod vaqti {tong7} 🕰\n
  🌇 Quyosh vaqti {quyosh7} 🕰\n
  🏞  peshin vaqti {peshin7} 🕰\n
  🌇 asr vaqti {asr7} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor7} 🕰\n
  🌃 hufton vaqti {hufton7} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Marg`ilon')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region8}\n
  🌃 Kun: {date8}\n
  🌃 Hafta: {hafta}\n
  🌃 Xijriy-Sana: { xijriy_sana8}\n
  🌃 Bomdod vaqti {tong8} 🕰\n
  🌇 Quyosh vaqti {quyosh8} 🕰\n
  🏞  peshin vaqti {peshin8} 🕰\n
  🌇 asr vaqti {asr8} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor8} 🕰\n
  🌃 hufton vaqti {hufton8} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Namangan')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region9}\n
  🌃 Kun: {date9}\n
  🌃 Hafta: {hafta9}\n
  🌃 Xijriy-Sana: { xijriy_sana9}\n
  🌃 Bomdod vaqti {tong9} 🕰\n
  🌇 Quyosh vaqti {quyosh9} 🕰\n
  🏞  peshin vaqti {peshin9} 🕰\n
  🌇 asr vaqti {asr9} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor9} 🕰\n
  🌃 hufton vaqti {hufton9} 🕰\n
    """,reply_markup=Shaxarlar)


@dp.message(F.text=='Navoiy')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region10}\n
  🌃 Kun: {date10}\n
  🌃 Hafta: {hafta10}\n
  🌃 Xijriy-Sana: { xijriy_sana10}\n
  🌃 Bomdod vaqti {tong10} 🕰\n
  🌇 Quyosh vaqti {quyosh10} 🕰\n
  🏞  peshin vaqti {peshin10} 🕰\n
  🌇 asr vaqti {asr10} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor10} 🕰\n
  🌃 hufton vaqti {hufton10} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Nukus')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region11}\n
  🌃 Kun: {date11}\n
  🌃 Hafta: {hafta11}\n
  🌃 Xijriy-Sana: { xijriy_sana11}\n
  🌃 Bomdod vaqti {tong11} 🕰\n
  🌇 Quyosh vaqti {quyosh11} 🕰\n
  🏞  peshin vaqti {peshin11} 🕰\n
  🌇 asr vaqti {asr11} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor11} 🕰\n
  🌃 hufton vaqti {hufton11} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Samarqand')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region12}\n
  🌃 Kun: {date12}\n
  🌃 Hafta: {hafta12}\n
  🌃 Xijriy-Sana: { xijriy_sana12}\n
  🌃 Bomdod vaqti {tong12} 🕰\n
  🌇 Quyosh vaqti {quyosh12} 🕰\n
  🏞  peshin vaqti {peshin12} 🕰\n
  🌇 asr vaqti {asr12} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor12} 🕰\n
  🌃 hufton vaqti {hufton12} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Termiz')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region13}\n
  🌃 Kun: {date13}\n
  🌃 Hafta: {hafta13}\n
  🌃 Xijriy-Sana: { xijriy_sana13}\n
  🌃 Bomdod vaqti {tong13} 🕰\n
  🌇 Quyosh vaqti {quyosh13} 🕰\n
  🏞  peshin vaqti {peshin13} 🕰\n
  🌇 asr vaqti {asr13} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor13} 🕰\n
  🌃 hufton vaqti {hufton13} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Toshkent')
async def shaxar1(message: Message):
 await message.answer(f"""🌃Shaxar: {region1}\n
  🌃 Kun: {date1}\n
  🌃 Hafta: {hafta1}\n
  🌃 Xijriy-Sana: { xijriy_sana1}\n
  🌃 Bomdod vaqti {tong1} 🕰\n
  🌇 Quyosh vaqti {quyosh1} 🕰\n
  🏞  peshin vaqti {peshin1} 🕰\n
  🌇 asr vaqti {asr1} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor1} 🕰\n
  🌃 hufton vaqti {hufton1} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Farg`ona')
async def shaxar1(message: Message):
  await message.answer(f"""🌃Shaxar: {region15}\n
  🌃 Kun: {date15}\n
  🌃 Hafta: {hafta15}\n
  🌃 Xijriy-Sana: { xijriy_sana15}\n
  🌃 Bomdod vaqti {tong15} 🕰\n
  🌇 Quyosh vaqti {quyosh15} 🕰\n
  🏞  peshin vaqti {peshin15} 🕰\n
  🌇 asr vaqti {asr15} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor15} 🕰\n
  🌃 hufton vaqti {hufton15} 🕰\n
    """,reply_markup=Shaxarlar)

@dp.message(F.text=='Xiva')
async def shaxar1(message: Message):
    await message.answer(f"""🌃Shaxar: {region}\n
  🌃 Kun: {date}\n
  🌃 Hafta: {hafta}\n
  🌃 Xijriy-Sana: { xijriy_sana}\n
  🌃 Bomdod vaqti {tong} 🕰\n
  🌇 Quyosh vaqti {quyosh} 🕰\n
  🏞  peshin vaqti {peshin} 🕰\n
  🌇 asr vaqti {asr} 🕰\n
  🌇 shom_iftor vaqti {shom_iftor} 🕰\n
  🌃 hufton vaqti {hufton} 🕰\n
    """,reply_markup=Shaxarlar)



@dp.message(F.text=='Nafil Namozlar☪️')
async def echo_handler(message: Message) -> None:
    await message.answer(text="Nafil Namozlar", reply_markup=nafil)


@dp.message(F.text=='Juma Naomzi')
async def echo_handler(message: Message) -> None:
    await message.answer_video(video="https://t.me/xivabotuchun/129",caption='Juma Namozi', reply_markup=erkaklar)

@dp.message(F.text=='Kurbon Xayit Namozi')
async def echo_handler(message: Message) -> None:
    await message.answer_video(video="https://t.me/xivabotuchun/130",caption='Qurbon Xayit Namozi', reply_markup=nafil)


@dp.message(F.text=='Zuxo Namozi')
async def echo_handler(message: Message) -> None:
    await message.answer_video(video="https://t.me/xivabotuchun/144",caption='''Расулуллоҳ саллоллоҳу алайҳи ва саллам айтдилар: "Кимки ўн икки ракаат зуҳо намози ўқиса, Аллоҳ унга жаннатда олтиндан бир қаср бино қилгайдир".
Термизий, Ибн Можа, Байҳақий, Табароний, Баззор ва Ибн Абу Осим ривоят қилишган.''', reply_markup=nafil)

@dp.message(F.text=='Janaza Namozi')
async def echo_handler(message: Message) -> None:
    await message.answer_video(video="https://t.me/xivabotuchun/131",caption='Janaza Namozi', reply_markup=nafil)



@dp.message(F.text=='Taxajjud Namozi')
async def echo_handler(message: Message) -> None:
    await message.answer_video(video="https://t.me/xivabotuchun/149",caption='Taxajjud Namozi', reply_markup=nafil)



 
@dp.message(F.text=='Istixora Namozi')
async def echo_handler(message: Message) -> None:
    await message.answer_video(video="https://t.me/xivabotuchun/150",caption='Istixora Namozi', reply_markup=nafil)   


@dp.message(F.text=='Taxorat Namozi')
async def echo_handler(message: Message) -> None:
    await message.answer_video(video="https://t.me/xivabotuchun/148",caption='Taxorat Namozi', reply_markup=nafil)


@dp.message(F.text=='Xojat Namozi')
async def echo_handler(message: Message) -> None:
    await message.answer_video(video="https://t.me/xivabotuchun/146",caption='''Абдуллоҳ ибн Абу Авфо розияллоҳу анҳудан ривоят қилинади: 

«Пайғамбар соллаллоҳу алайҳи васаллам: «Кимнинг Аллоҳга ва Бани одамдан бирортасига ҳожати бўлса, яхшилаб таҳорат қилсин, сўнгра икки ракат намоз ўқисин. Кейин Аллоҳга сано ва Пайғамбар соллаллоҳу алайҳи васалламга саловат айтсин. Сўнгра: «Ҳалийму Карим Аллоҳдан ўзга ҳеч илоҳи маъбуд йўқ. Улуғ Аршнинг Роббиси Аллоҳ покдир. Оламларнинг Роббиси Аллоҳга ҳамдлар бўлсин. Мен Сендан: раҳматингни вожиб қилувчи, мағфиратингни тақозо қилувчи нарсаларни ва ҳар бир яхшиликдан ғаниматни, ҳар бир ёмонликдан саломатлик сўрайман. Менинг ҳеч бир гуноҳимни қўймай мағфират қилгин, ҳеч бир ғамимни қўймай кушойиш эт, Ўзинг рози бўлган ҳеч бир ҳожатимни қўймай, албатта чиқаргин. Эй Арҳамар Роҳимийн», десин», дедилар» 

Имом Термизий ва Ибн Можа ривоят қилган.''', reply_markup=nafil)    
   



@dp.message(F.text=='Yangi Masjid Uchun Hayriya🕌')
async def echo_handler(message: Message) -> None:
    await message.answer_video(video='https://t.me/xivabotuchun/127', reply_markup=menyu)
    await message.answer(text="Xiva Shaxrida Yansi Masjid Qurilishi Davom Etmoqda \nSiz ham o`z hissangizni qo`shing\nEshchanov Erkin\n8600332986036360", reply_markup=menyu)

@dp.message(F.text=='🕌Said Niyoz Sholikor🕌')
async def echo_handler(message: Message) -> None:
    await message.answer('Joylashuvni kqrishingir mumkin')
    await message.answer_location(latitude=41.376788,longitude=60.362592)

@dp.message(F.text=='🕌Xasan Basriy🕌')
async def echo_handler(message: Message) -> None:
    await message.answer('Joylashuvni kqrishingir mumkin')
    await message.answer_location(latitude=41.408503,longitude=60.331076)
        
@dp.message(F.text=='🕌Kasmabot jome Masjidi🕌')
async def echo_handler(message: Message) -> None:
    await message.answer('Joylashuvni kqrishingir mumkin')
    await message.answer_location(latitude=41.391646,longitude=60.332701)


@dp.message(F.text=='Xiva Namoz Vaqtlari⏲️')
async def echo_handler(message: Message) -> None:
    await message.answer(text="O`z Shaxringirni tanglang",reply_markup=Shaxarlar)
   
@dp.message(F.text=='Tongi Zikirlar🤲')
async def zikir(message: Message) -> None:
    await message.answer(text="«1)Розийту биллаҳи роббан ва бил ислами дийнан ва бимуҳаммадин соллаллоҳу алайҳи васаллама росула»\n\nМаъноси: “Аллоҳни раббим деб, Исломни диним деб, Муҳаммад алайҳиссаломни расул деб рози бўлдим”\n\n\n«2)Розийту биллаҳи роббан ва бил ислами дийнан ва бимуҳаммадин соллаллоҳу алайҳи васаллама росула», деса, унга жаннат вожиб бўлади», дедилар.\n\nМаъноси: “Аллоҳни раббим деб, Исломни диним деб, Муҳаммад алайҳиссаломни расул деб рози бўлдим”\n\n\n3)«Аллоҳумма инний асбаҳту ушҳидука ва ушҳиду ҳамалата ъаршика ва малаикатика ва жамийъа холқик, аннака анталлоҳу лаа илаҳа илла анта ваҳдака лаа шарийка лака ва анна Муҳаммадан ъабдука ва росулук»\n\nМаъноси: “Аллоҳим, албатта, мен тонг оттирдим. Сени ҳамда аршингни кўтарувчи фаришталарингни ва ҳамма халқ қилган нарсаларингни гувоҳ қилиб айтаманки, Сендан бошқа илоҳ йўқ, Муҳаммад соллаллоҳу алайҳи васаллам Сенинг банданг ва расулингдир”", reply_markup=menyu)

@dp.message(F.text=='Tungi Zikirlar🤲') 
async def zikir2(message:Message):
    await message.answer(text='«1)Амсайнаа ва амсал мулку лиллаҳи роббил ъаламийн. Аллоҳумма асалука хойра ҳазиҳил лайлати фатҳаҳаа ва насроҳаа ва нуроҳаа ва барокатаҳаа ва ҳудаҳаа ва аъузу бика мин шарри ма фийҳаа ва шарри маа баъдаҳаа»\n\nМаъноси: “Биз ҳам, мулк ҳам оламлар парвардигори Аллоҳники бўлган ҳолда кеч киргиздик. Эй Раббим, бу кечанинг яхшисини, фатҳ бўлишини, ғалабасини, нурини, баракасини, ҳидоятини сўрайман. Ва Сендан бу кечанинг ва бу кечадан кейингисининг ёмонлигидан паноҳ тилайман”2)Амсайнаа ва амсал мулку лиллаҳи роббил ъаламийн. Аллоҳумма асалука хойра ҳазиҳил лайлати фатҳаҳаа ва насроҳаа ва нуроҳаа ва барокатаҳаа ва ҳудаҳаа ва аъузу бика мин шарри ма фийҳаа ва шарри маа баъдаҳаа», деб айтсин.\n\nМаъноси: “Биз ҳам, мулк ҳам оламлар парвардигори Аллоҳники бўлган ҳолда кеч киргиздик. Эй Раббим, бу кечанинг яхшисини, фатҳ бўлишини, ғалабасини, нурини, баракасини, ҳидоятини сўрайман.Ва Сендан бу кечанинг ва бу кечадан кейингисининг ёмонлигидан паноҳ тилайман”\n\n\n3)«Аллоҳумма анта роббий ла илаҳа илла анта холақтаний ва ана ъабдука ва ана ъала ъаҳдика ва ваъдика мастатоъту аъузу бика мин шарри ма сонаъту, абуу лака биниъматика ъалаййа ва абуу бизамбий фағфирлий фаиннаҳу ла йағфируз зунуба илла анта»\n\nМаъноси: “Аллоҳим, Сен парвардигоримсан, Сендан бошқа илоҳ йўқ. Мени халқ қилдинг ва мен Сенинг қулингман. Мен Сенга берган ваъдамда ва Сенга берган аҳдимда қодир бўлганимча турибман. Қилган нарсаларимнинг ёмонидан Сенинг номинг билан паноҳ тилайман. Менга ато қилган неъматларингга иқрор бўлдим. Ва яна гуноҳларимга ҳам иқрор бўлдим. Менинг гуноҳларимни кечир. Чунки Сендан бошқаси гуноҳларни кечира олмайди”', reply_markup=menyu)
            

@dp.message(F.text=='Namoz Oqishni Organamiz☪️')
async def namoz2(message:Message):
  await message.answer(text='namoz oqish',reply_markup=oqish)    

@dp.message(F.text=='Erkaklar🧔')
async def erkak(message:Message):
  await message.answer(text='namoz oqish',reply_markup=erkaklar)

@dp.message(F.text=='Ayollar🧕')
async def ayol(message:Message):
  await message.answer(text='namoz o`qish',reply_markup=ayollar) 

#erkaklar
#22:34
@dp.message(F.text=='Bomdod')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namozi_organish_Erkaklar_5_mahal/136',caption='Bomdod Namozi Erkaklar uchun',reply_markup=erkaklar)  
 
@dp.message(F.text=='Peshin')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namozi_organish_Erkaklar_5_mahal/137',caption='Peshin Namozi Erkaklar uchun',reply_markup=erkaklar)  

@dp.message(F.text=='Asr')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namozi_organish_Erkaklar_5_mahal/138',caption='Asr Namozi Erkaklar uchun',reply_markup=erkaklar)  

@dp.message(F.text=='Shom')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namozi_organish_Erkaklar_5_mahal/139',caption='Shom Namozi Erkaklar uchun',reply_markup=erkaklar)  

@dp.message(F.text=='Xufton')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/Namozi_organish_Erkaklar_5_mahal/140',caption='Xufton Namozi Erkaklar uchun',reply_markup=erkaklar)  

#ayollar

@dp.message(F.text=='bomdod')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/4',caption='Bomdod Namozi Ayollar uchun',reply_markup=ayollar)  
 
@dp.message(F.text=='peshin')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/7',caption='Peshin Namozi Ayollar uchun',reply_markup=ayollar)  

@dp.message(F.text=='asr')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/8',caption='Asr Namozi Ayollar uchun',reply_markup=ayollar)  

@dp.message(F.text=='shom')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/9',caption='Shom Namozi Ayollar uchun',reply_markup=ayollar)  

@dp.message(F.text=='xufton')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/10',caption='Xufton Namozi Ayollar uchun',reply_markup=ayollar)  

@dp.message(F.text=='ortga🔙')
async def back(message:Message):
  await message.answer('asasiy menyu',reply_markup=menyu) 

#isllar
@dp.message(F.text=='Allohnig 99 Ismi')
async def ism(message:Message):
  await message.answer('Alloh\nar-Rahmon\nar-Rahiym\nal-Malik\nal-Quddus\nas-Salom\nal-Mo‘min\nal-Muhaymin\nal-Aziz\nal-Jabbor\nal-Mutakabbir\nal-Xoliq\nal-Bori’\nal-Musavvir\nal-G‘affor\nal-Qahhor\nal-Vahhob\nar-Razzoq\nal-Fattoh\nal-Aliym\nal-Qobiz\nal-Bosit\nal-Xofiz\nar-Rofe’\nal-Mu’izz\nal-Muzill\nas-Samiy’\nal-Basiyr\nal-Hakam\nal-Adl\nal-Latiyf\nal-Xabiyr\nal-Haliym\nal-Aziym\nal-G‘afur\nash-Shakur\nal-Aliy\nal-Kabiyr\nal-Hafiyz\nal-Muqiyt\nal-Hasiyb\nal-Jaliyl\nal-Kariym\nar-Raqiyb\nal-Mujiyb\nal-Vose’\nal-Hakiym\nal-Vadud\nal-Majiyd\nal-Bo’is\nash-Shahiyd\nal-Haq\nal-Vakil\nal-Qaviy\nal-Matiyn\nal-Valiy\nal-Hamiyd\nal-Muhsiy\nal-Mubdi’\nal-Mu’iyd\nal-Muhyi\nal-Mumiyt\nal-Hayy\nal-Qayyum\nal-Vojid\nal-Mojid\nal-Vohid\nas-Somad\nal-Qodir\nal-Muqtadir\nal-Muqaddim\nal-Muaxxir\nal-Avval\nal-Oxir\naz-Zohir\nal-Botin\nal-Voliy\nal-Muta’oliy\nal-Barr\nat-Tavvob\nal-Muntaqim\nal-Afuvv\nar-Rauf\nal-Molikul mulk\nZul jaloli val ikrom\nal-Muqsit\nal-Jome’\nal-G‘aniy\nal-Mug‘niy\nal-Mone’\naz-Zorr\nan-Nofe’\nan-Nur\nal-Hodiy\nal-Badiy’\nal-Boqiy\nal-Voris\nar-Rashiyd\nas-Sabur',reply_markup=menyu)

#Taxorat
@dp.message(F.text=='Taxorat Olish Tartibi🚿')
async def back(message:Message):
  await message.answer_video(video='https://t.me/xivabotuchun/122',caption='Taxorat Olish',reply_markup=menyu) 

@dp.message(F.text=='G`usl Olish Tartibi🚿')
async def namoz2(message:Message):
  await message.answer(text='Gusl qilish',reply_markup=gusl)    

@dp.message(F.text=='erkaklar🧔')
async def erkak(message:Message):
  await message.answer_video(video='https://t.me/xivabotuchun/123',caption='Erkaklar Gusl Olish',reply_markup=gusl)

@dp.message(F.text=='ayollar🧕')
async def ayol(message:Message):
  await message.answer_video(video='https://t.me/Ayollar_nomozi_oqish_uchun/3',caption='Ayllar Gusl Olish',reply_markup=gusl) 


@dp.message(F.text=='ortga⬅️')
async def back(message:Message):
  await message.answer('Namoz Oqish',reply_markup=oqish) 


#01:48
#quran
#12:10
@dp.message(F.text=='Quran Audio🫀')
async def quran(message:Message):
  await message.answer(text='Quran Audio',reply_markup=ustozlar)  

@dp.message(F.text=='Yasser Al-Dosari')
async def send_welcome(message: types.Message):

    await message.answer("Quran Audio", reply_markup=quran1)



@dp.message(F.text == 'Al-Fatiha')
async def quran_1(message: Message):
   await message.answer_audio(audio='https://t.me/xivabotuchun/3', reply_markup=quran1)


@dp.message(F.text == 'Al-Baqarah')
async def quran_2(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/4', reply_markup=quran1)

@dp.message(F.text == 'Al-Imran')
async def quran_3(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/5', reply_markup=quran1)

@dp.message(F.text == 'An-Nisa')
async def quran_4(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/6', reply_markup=quran1)

@dp.message(F.text == 'Al-Maidah')
async def quran_5(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/7', reply_markup=quran1)

@dp.message(F.text == "Al-An'am")
async def quran_6(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/8', reply_markup=quran1)

@dp.message(F.text == 'Al-Araf')
async def quran_7(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/9', reply_markup=quran1)

@dp.message(F.text == 'Al-Anfal')
async def quran_8(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/10', reply_markup=quran1)

@dp.message(F.text == 'At-Tawbah')
async def quran_9(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/11', reply_markup=quran1)

@dp.message(F.text == 'Yunus')
async def quran_10(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/12', reply_markup=quran1)

@dp.message(F.text == 'Hud')
async def quran_11(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/13', reply_markup=quran1)

@dp.message(F.text == 'Yusuf')
async def quran_12(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/14', reply_markup=quran1)

@dp.message(F.text == "Ar-Ra'd")
async def quran_13(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/15', reply_markup=quran1)

@dp.message(F.text == 'Ibrahim')
async def quran_14(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/16', reply_markup=quran1)

@dp.message(F.text == 'Al-Hijr')
async def quran_15(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/17', reply_markup=quran1)

@dp.message(F.text == 'An-Nahl')
async def quran_16(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/18', reply_markup=quran1)

@dp.message(F.text == 'Al-Isra')
async def quran_17(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/19', reply_markup=quran1)

@dp.message(F.text == 'Al-Kahf')
async def quran_18(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/20', reply_markup=quran1)

@dp.message(F.text == 'Maryam')
async def quran_19(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/21', reply_markup=quran1)

@dp.message(F.text == 'Ta-Ha')
async def quran_20(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/22', reply_markup=quran1)

@dp.message(F.text == 'Al-Anbiya')
async def quran_21(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/23', reply_markup=quran1)

@dp.message(F.text == 'Al-Hajj')
async def quran_22(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/24', reply_markup=quran1)

@dp.message(F.text == 'Al-Muminun')
async def quran_23(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/25', reply_markup=quran1)

@dp.message(F.text == 'An-Nur')
async def quran_24(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/26', reply_markup=quran1)

@dp.message(F.text == 'Al-Furqan')
async def quran_25(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/27', reply_markup=quran1)

@dp.message(F.text == 'Ash-Shuara')
async def quran_26(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/28', reply_markup=quran1)

@dp.message(F.text == 'An-Naml')
async def quran_27(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/29', reply_markup=quran1)

@dp.message(F.text == 'Al-Qasas')
async def quran_28(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/30', reply_markup=quran1)

@dp.message(F.text == 'Al-Ankabut')
async def quran_29(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/31', reply_markup=quran1)

@dp.message(F.text == 'Ar-Rum')
async def quran_30(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/32', reply_markup=quran1)

@dp.message(F.text == 'Luqman')
async def quran_31(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/33', reply_markup=quran1)

@dp.message(F.text == 'As-Sajda')
async def quran_32(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/34', reply_markup=quran1)

@dp.message(F.text == 'Al-Ahzab')
async def quran_33(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/35', reply_markup=quran1)

@dp.message(F.text == 'Saba')
async def quran_34(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/36', reply_markup=quran1)

@dp.message(F.text == 'Fatir')
async def quran_35(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/37', reply_markup=quran1)

@dp.message(F.text == 'Ya-Sin')
async def quran_36(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/38', reply_markup=quran1)

@dp.message(F.text == 'As-Saffat')
async def quran_37(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/39', reply_markup=quran1)

@dp.message(F.text == 'Sad')
async def quran_38(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/40', reply_markup=quran1)

@dp.message(F.text == 'Az-Zumar')
async def quran_39(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/41', reply_markup=quran1)

@dp.message(F.text == 'Ghafir')
async def quran_40(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/42', reply_markup=quran1)

@dp.message(F.text == 'Fussilat')
async def quran_41(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/43', reply_markup=quran1)


@dp.message(F.text == 'Ash-Shura')
async def quran_42(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/44', reply_markup=quran1)

@dp.message(F.text == 'Az-Zukhruf')
async def quran_43(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/45', reply_markup=quran1)

@dp.message(F.text == 'Ad-Dukhan')
async def quran_44(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/46', reply_markup=quran1)

@dp.message(F.text == 'Al-Jathiya')
async def quran_45(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/47', reply_markup=quran1)

@dp.message(F.text == 'Al-Ahqaf')
async def quran_46(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/48', reply_markup=quran1)

@dp.message(F.text == 'Muhammad')
async def quran_47(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/49', reply_markup=quran1)

@dp.message(F.text == 'Al-Fath')
async def quran_48(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/50', reply_markup=quran1)

#keldi

@dp.message(F.text == 'Al-Hujurat')
async def quran_49(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/51', reply_markup=quran1)

@dp.message(F.text == 'Qaf')
async def quran_50(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/52', reply_markup=quran1)

@dp.message(F.text == 'Adh-Dhariyat')
async def quran_51(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/53', reply_markup=quran1)

@dp.message(F.text == 'At-Tur')
async def quran_52(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/54', reply_markup=quran1)

@dp.message(F.text == 'An-Najm')
async def quran_53(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/55', reply_markup=quran1)

@dp.message(F.text == 'Al-Qamar')
async def quran_54(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/56', reply_markup=quran1)

@dp.message(F.text == 'Ar-Rahman')
async def quran_55(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/57', reply_markup=quran1)

@dp.message(F.text == 'Al-Waqia')
async def quran_56(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/58', reply_markup=quran1)

@dp.message(F.text == 'Al-Hadid')
async def quran_57(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/59', reply_markup=quran1)

@dp.message(F.text == 'Al-Mujadila')
async def quran_58(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/60', reply_markup=quran1)

@dp.message(F.text == 'Al-Hashr')
async def quran_59(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/61', reply_markup=quran1)

@dp.message(F.text=='Al-Mumtahina')
async def quran_60(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/62', reply_markup=quran1)

@dp.message(F.text=='Al-Saff')
async def quran_61(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/63', reply_markup=quran1)

@dp.message(F.text=='Al-Jumua')
async def quran_62(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/64', reply_markup=quran1)

@dp.message(F.text=='Al-Munafiqun')
async def quran_63(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/65', reply_markup=quran1)


@dp.message(F.text=='At-Taghabun')
async def quran_64(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/66', reply_markup=quran1)

@dp.message(F.text=='Al-Talaq')
async def quran_65(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/67', reply_markup=quran1)


@dp.message(F.text=='At-Tahrim')
async def quran_65(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/68', reply_markup=quran1)

@dp.message(F.text=='Al-Mulk')
async def quran_67(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/69', reply_markup=quran1)

@dp.message(F.text=='Al-Qalam')
async def quran_68(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/70', reply_markup=quran1)

@dp.message(F.text=='Al-Haaqqa')
async def quran_69(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/71', reply_markup=quran1)

@dp.message(F.text=='Al-Ma’arij')
async def quran_70(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/72', reply_markup=quran1)

@dp.message(F.text=='Nuh')
async def quran_71(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/73', reply_markup=quran1)

@dp.message(F.text=='Al-Jinn')
async def quran_72(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/74', reply_markup=quran1)

@dp.message(F.text=='Al-Muzzammil')
async def quran_73(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/75', reply_markup=quran1)

@dp.message(F.text=='Al-Muddathir')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/76', reply_markup=quran1)

@dp.message(F.text=='Al-Qiyama')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/77', reply_markup=quran1)

@dp.message(F.text=='Al-Insan')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/78', reply_markup=quran1)   

@dp.message(F.text=='Al-Mursalat')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/79', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Naba')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/80', reply_markup=quran1)   

@dp.message(F.text=='Al-Naziat')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/81', reply_markup=quran1)   
     
@dp.message(F.text=='Abasa')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/82', reply_markup=quran1)   

@dp.message(F.text=='At-Takwir')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/83', reply_markup=quran1)   

@dp.message(F.text=='Al-Infitar')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/84', reply_markup=quran1)   

@dp.message(F.text=='Al-Mutaffifn')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/85', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Inshiqaq')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/86', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Buruj')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/87', reply_markup=quran1)   
     
@dp.message(F.text=='At-Tariq')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/88', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Ala')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/89', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Ghashiyah')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/90', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Fajr')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/91', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Balad')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/92', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Shams')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/93', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Layl')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/94', reply_markup=quran1)   
     
@dp.message(F.text=='Ad-Duha')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/95', reply_markup=quran1)   
     
@dp.message(F.text=='Ash-Sharh')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/96', reply_markup=quran1)   
     
@dp.message(F.text=='At-Tin')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/97', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Alaq')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/98', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Qadr')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/99', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Bayyina')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/100', reply_markup=quran1)   
     
@dp.message(F.text=='Az-Zalzala')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/101', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Adiyat')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/102', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Qaria')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/103', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Takathur')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/104', reply_markup=quran1)   

@dp.message(F.text=='Al-Asr')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/105', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Humaza')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/106', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Fil')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/107', reply_markup=quran1)   
     
@dp.message(F.text=='Quraish')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/108', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Maun')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/109', reply_markup=quran1)   

@dp.message(F.text=='Al-Kawthar')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/110', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Kafirun')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/111', reply_markup=quran1)   
     
@dp.message(F.text=='An-Nasr')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/112', reply_markup=quran1)   
     
@dp.message(F.text=='Al-Masad')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/113', reply_markup=quran1)   
     

@dp.message(F.text=='Al-Ikhlas')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/114', reply_markup=quran1)   
     

@dp.message(F.text=='Al-Falaq')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/115', reply_markup=quran1)   
     
@dp.message(F.text=='An-Nas')
async def quran_74(message: Message):
    await message.answer_audio(audio='https://t.me/xivabotuchun/116', reply_markup=quran1)   
     



@dp.message(F.text=='ortga<-')
async def back(message:Message):
  await message.answer('Asossiy menyu',reply_markup=menyu) 

@dp.message(F.text=='Ortga<-')
async def back(message:Message):
  await message.answer('Asossiy menyu',reply_markup=menyu)


@dp.message(F.text=='Ortga:')
async def back(message:Message):
  await message.answer('Asossiy menyu',reply_markup=menyu)  


@dp.message(F.text=="ORTGA <-")
async def back(message:Message):
  await message.answer('Asossiy menyu',reply_markup=menyu)  
#15:45


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Tugadi")