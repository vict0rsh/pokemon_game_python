from pokemon import *

class Personagem:
    def __init__(self, nome = None, pokemons = []):
        if nome:
            self.nome = nome
        else:
            self.nome = "Anônimo"
        self.pokemons = pokemons
        
    def __str__(self):
        return self.nome
    
class Player(Personagem):
    tipo = "Player"
    
    
class Inimigo(Personagem):
    tipo = "Inimigo"
    
    
PlayerOne = Player("Victor", (meu_pokemon, pokemon_amigo))

print(PlayerOne)
for pokemon in PlayerOne.pokemons:
    print(pokemon)          