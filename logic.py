from random import randint
import requests
from datetime import timedelta, datetime


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1025)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(100,200)
        self.manna = randint(30,70)
        self.last_feed_time = datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data =  response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return 'Pikachu' 


    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f'''Имя твоего покеомона: {self.name}
hp: {self.hp}
manna: {self.manna}'''
    
    def attack(self, enemy):
        if enemy.hp > self.manna:
            enemy.hp -= self.manna
            return f'Сражение @{self.pokemon_trainer} c @{enemy.pokemon_trainer}'
        else:
            enemy.hp = 0
            return f'Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}'
        
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
        

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(10,1000)
        self.power += super_power
        result = super().attack(enemy)
        self.power -=   super_power
        return result + f'\
    Боец применил супер-атаку силой:{super_power}'


class Wizard(Pokemon):
    pass
    

p = Pokemon('Tuskul')
print(p.info())