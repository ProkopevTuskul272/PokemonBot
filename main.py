import telebot 
from config import token
from logic import Pokemon


bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def attack(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        my_pokemon = Pokemon.pokemons(message.from_user.username)
        his_or_her_pokemon = Pokemon.pokemons(message.reply_to_message.from_user.username)
        result = my_pokemon.attack(his_or_her_pokemon)
        bot.send_message(message.chat.id, result)
    else:
        bot.reply_to(message, "Э, слышь, выбери противника.")

@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon_1 = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon_1.feed())
    

@bot.message_handler(commands=['info'])
def info(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
    else:
        bot.reply_to(message, 'где покемон???')


bot.infinity_polling(none_stop=True)

