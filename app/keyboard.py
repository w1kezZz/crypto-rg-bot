from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

wallet = InlineKeyboardButton(text='👛 Кошелёк', callback_data='wallet')
subscriber = InlineKeyboardButton(text='🍑 Подписки', callback_data='subs')
p2p = InlineKeyboardButton(text='💠 P2P', callback_data='p2p')
birza = InlineKeyboardButton(text='🐬 Биржа', callback_data='birza')
checks = InlineKeyboardButton(text='🦋 Чеки', callback_data='checks')
score = InlineKeyboardButton(text='📥 Счета', callback_data='score')
cryptopay = InlineKeyboardButton(text='🏝 Crypto Pay', callback_data='cryptopay')
contest = InlineKeyboardButton(text='🥇 Конкурсы', callback_data='contest')
settings = InlineKeyboardButton(text='⚙️ Настройки', callback_data='settings')
mainmenu = InlineKeyboardMarkup(row_width=2).add(wallet, subscriber).add(p2p, birza).add(checks, score).add(cryptopay, contest).add(settings)

addbal = InlineKeyboardButton(text='Пополнить', callback_data='addbal')
vivod = InlineKeyboardButton(text='Вывести', callback_data='vivod')
adressbook = InlineKeyboardButton(text='Адресная книга', callback_data='adressbook')
commisia = InlineKeyboardButton(text='Комиссии и лимиты', callback_data='commisia')
nazad = InlineKeyboardButton(text='< Назад', callback_data='nazad')
walletmarkup = InlineKeyboardMarkup(row_width=2).add(addbal, vivod).add(adressbook).add(commisia).add(nazad)

addbal1 = InlineKeyboardButton(text='Tether - USDT (TRC20, ERC20, BEP20)', callback_data='addbal1')
addbal2 = InlineKeyboardButton(text='Toncoin - TON (TON)', callback_data='addbal2')
addbal3 = InlineKeyboardButton(text='Bitcoin - BTC ( BTC)', callback_data='addbal3')
addbal4 = InlineKeyboardButton(text='Litecoin - LTC (LTC)', callback_data='addbal4')
addbal5 = InlineKeyboardButton(text='Ethereum - ETH (ERC20)', callback_data='addbal5')
addbal6 = InlineKeyboardButton(text='Binance Coin - BNB (BEP20)', callback_data='addbal6')
addbal7 = InlineKeyboardButton(text='TRON - TRX (TRC20)', callback_data='addbal7')
addbal8 = InlineKeyboardButton(text='USD Coin - USDC (ERC20, BEP20)', callback_data='addbal8')
nazadwall = InlineKeyboardButton(text='< Назад в Кошелёк', callback_data='nazadwall')
addbalwallet = InlineKeyboardMarkup(row_width=1).add(addbal1, addbal2, addbal3, addbal4, addbal5, addbal6, addbal7, addbal8, nazadwall)

selladdbal1 = InlineKeyboardButton(text='Tether - USDT (TRC20, ERC20, BEP20)', callback_data='selladdbal1')
selladdbal2 = InlineKeyboardButton(text='Toncoin - TON (TON)', callback_data='selladdbal2')
selladdbal3 = InlineKeyboardButton(text='Bitcoin - BTC (BTC)', callback_data='selladdbal3')
selladdbal4 = InlineKeyboardButton(text='Litecoin - LTC (LTC)', callback_data='selladdbal4')
selladdbal5 = InlineKeyboardButton(text='Ethereum - ETH (ERC20)', callback_data='selladdbal5')
selladdbal6 = InlineKeyboardButton(text='Binance Coin - BNB (BEP20)', callback_data='selladdbal6')
selladdbal7 = InlineKeyboardButton(text='TRON - TRX (TRC20)', callback_data='selladdbal7')
selladdbal8 = InlineKeyboardButton(text='USD Coin - USDC (ERC20, BEP20)', callback_data='selladdbal8')
sellnazadwall = InlineKeyboardButton(text='< Назад в Кошелёк', callback_data='wallet')
selladdbalwallet = InlineKeyboardMarkup(row_width=1).add(selladdbal1, selladdbal2, selladdbal3, selladdbal4, selladdbal5, selladdbal6, selladdbal7, selladdbal8, sellnazadwall)

tron = InlineKeyboardButton(text='TRON (TRC20)', callback_data='notmoney')
eth = InlineKeyboardButton(text='Ethereum (ERC20)', callback_data='notmoneyeth')
bnb = InlineKeyboardButton(text='BNB Smart Chain (BEP20)', callback_data='notmoneybnb')
edit = InlineKeyboardButton(text='< Изменить монету', callback_data='vivodback')
selltether = InlineKeyboardMarkup(row_width=1).add(tron, eth, bnb, edit)

ton = InlineKeyboardButton(text='The Open Network (TON)', callback_data='notmoneyton')
edit = InlineKeyboardButton(text='< Изменить монету', callback_data='vivodback')
sellton = InlineKeyboardMarkup(row_width=1).add(ton, edit)

btc = InlineKeyboardButton(text='Bitcoin (BTC)', callback_data='notmoneybtc')
sellbtc = InlineKeyboardMarkup(row_width=1).add(btc, edit)

litecoin = InlineKeyboardButton(text='Litecoin (LTC)', callback_data='notmoneyltc')
sellltc = InlineKeyboardMarkup(row_width=1).add(litecoin, edit)

eth2 = InlineKeyboardButton(text='Ethereum (ERC20)', callback_data='notmoneyeth')
selleth = InlineKeyboardMarkup(row_width=1).add(eth2, edit)

bnbcoin = InlineKeyboardButton(text='BNB Smart Chain (BEP20)', callback_data='notmoneybnb2')
sellbnb = InlineKeyboardMarkup(row_width=1).add(bnbcoin, edit)

troncoin = InlineKeyboardButton(text='TRON (TRC20)', callback_data='notmoneytron')
selltron = InlineKeyboardMarkup(row_width=1).add(troncoin, edit)

eth3 = InlineKeyboardButton(text='Ethereum (ERC20)', callback_data='ethcoin')
bnbcoin2 = InlineKeyboardButton(text='BNB Smart Chain (BEP20)', callback_data='bnbcoin')
sellusdc = InlineKeyboardMarkup(row_width=1).add(eth3, bnbcoin2, edit)

comisia1 = InlineKeyboardButton(text='Tether - USDT (TRC20, ERC20, BEP20)', callback_data='comisia1')
comisia2 = InlineKeyboardButton(text='Toncoin - TON (TON)', callback_data='comisia2')
comisia3 = InlineKeyboardButton(text='Bitcoin - BTC ( BTC)', callback_data='comisia3')
comisia4 = InlineKeyboardButton(text='Litecoin - LTC (LTC)', callback_data='comisia4')
comisia5 = InlineKeyboardButton(text='Ethereum - ETH (ERC20)', callback_data='comisia5')
comisia6 = InlineKeyboardButton(text='Binance Coin - BNB (BEP20)', callback_data='comisia6')
comisia7 = InlineKeyboardButton(text='TRON - TRX (TRC20)', callback_data='comisia7')
comisia8 = InlineKeyboardButton(text='USD Coin - USDC (ERC20, BEP20)', callback_data='comisia8')
sellnazadwall = InlineKeyboardButton(text='< Назад в Кошелёк', callback_data='wallet')
comisiamarkup = InlineKeyboardMarkup(row_width=1).add(comisia1, comisia2, comisia3, comisia4, comisia5, comisia6, comisia7, comisia8, sellnazadwall)

troncom = InlineKeyboardButton(text='TRON (TRC20)', callback_data='troncom')
ethcom = InlineKeyboardButton(text='Ethereum (ERC20)', callback_data='ethcom')
bnbcom = InlineKeyboardButton(text='BNB Smart Chain (BEP20)', callback_data='bnbcom')
editcom = InlineKeyboardButton(text='< Изменить монету', callback_data='commisia')
nazadcom = InlineKeyboardButton(text='< Назад', callback_data='comisia1')
nazadcom2 = InlineKeyboardButton(text='< Назад', callback_data='commisia')
tethermark = InlineKeyboardMarkup(row_width=1).add(troncom, ethcom, bnbcom, editcom)

nazadcomark = InlineKeyboardMarkup(row_width=1).add(nazadcom)

nazadcommark = InlineKeyboardMarkup(row_width=1).add(nazadcom2)

ethereums = InlineKeyboardButton(text='Ethereum (ERC20)', callback_data='ethereums')
bnbsmartch = InlineKeyboardButton(text='BNB Smart Chain (BEP20)', callback_data='bnbsmartch')
nazadcom3 = InlineKeyboardButton(text='< Назад', callback_data='comisia8')
nextcommark = InlineKeyboardMarkup(row_width=1).add(ethereums, bnbsmartch, nazadcom2)

nazadnextmark = InlineKeyboardMarkup(row_width=1).add(nazadcom3)

buytron = InlineKeyboardButton(text='TRON (TRC20)', callback_data='buytron')
buyeth = InlineKeyboardButton(text='Ethereum (ERC20)', callback_data='buyeth')
buybnb = InlineKeyboardButton(text='BNB Smart Chain (BEP20)', callback_data='buybnb')
buyback = InlineKeyboardButton(text='< Изменить монету', callback_data='editmonet')
buyback2 = InlineKeyboardButton(text='< Изменить монету', callback_data='editmonet2')
buymark = InlineKeyboardMarkup(row_width=1).add(buytron, buyeth, buybnb, buyback)

buyback3 = InlineKeyboardButton(text='< Назад в Кошелёк', callback_data='wallet')
backmark = InlineKeyboardMarkup(row_width=1).add(buyback3)

buyethereums = InlineKeyboardButton(text='Ethereum (ERC20)', callback_data='buyethereums')
buybnbsmartch = InlineKeyboardButton(text='BNB Smart Chain (BEP20)', callback_data='buybnbsmartch')
buynextcommark = InlineKeyboardMarkup(row_width=1).add(buyethereums, buybnbsmartch, buyback)