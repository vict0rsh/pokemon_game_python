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
    
    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de {}:".format(self))
            for pokemon in self.pokemons:
                print(pokemon)
        else: 
            print("{} não tem nenhum pokemon ainda.".format(self))
       
class Player(Personagem):
    tipo = "Player"
    
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("{} capturou {}!".format(self, pokemon))
        
    
    
class Inimigo(Personagem):
    tipo = "Inimigo"
    
    
PlayerOne = Player("Victor", pokemons=[meu_pokemon])

PlayerOne.capturar(pokemon_selvagem)

PlayerOne.mostrar_pokemons()


        