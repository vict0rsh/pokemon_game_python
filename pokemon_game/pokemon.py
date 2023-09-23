import random


class Pokemon:    
    tipo = "Normal"
        
    def __init__(self, especie, level = None, nome = None): #inicio do objeto pokemon
        self.especie = especie
        self.tipo = self.tipok()
        # level randomico
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
        # nome = especie caso vazio    
        if nome:
            self.nome = nome
        else:
            self.nome = especie            
    
    def tipok(self):
        return "Normal"
        
    def __str__(self):
        return "{} ({})".format(self.especie, self.level) #print mostra especie do pokemon e level
    
    def atacar(self, inimigo):
        print("{} atacou {}".format(self, inimigo))
        
class PokemonEletrico(Pokemon):
    def tipok(self):
        return "Elétrico"
        
class PokemonFogo(Pokemon):
    def tipok(self):
        return "Fogo"
    
class PokemonAgua(Pokemon):
    def tipok(self):
        return "Água"

class PokemonPlanta(Pokemon):
    def tipok(self):
        return "Planta"
               
# class PokemonLutador(Pokemon):
#     tipo = "Lutador"

# class PokemonVeneno(Pokemon):
#     tipo = "Veneno"
    
# class PokemonTerra(Pokemon):
#     tipo = "Terra"
    
# class PokemonPedra(Pokemon):
#     tipo = "Pedra"
    
# class PokemonInseto(Pokemon):
#     tipo = "Inseto"
    
# class PokemonGelo(Pokemon):
#     tipo = "Gelo"
    
# class PokemonPsiquico(Pokemon):
#     tipo = "Psíquico"

                                          
POKEMONS =[
    PokemonFogo("Flareon"),
    PokemonFogo("Charmander"),
    PokemonFogo("Arcanine"),
    PokemonAgua("Tentacool"),
    PokemonAgua("Squirtle"),
    PokemonAgua("Magikarp"),
    PokemonEletrico("Raichu"),
    PokemonEletrico("Rayquaza"),
    PokemonEletrico("Voltorb"),
    PokemonPlanta("Bulbassauro"),
    PokemonPlanta("Oddish"),
    PokemonPlanta("Bellsprout"),
    Pokemon("Ratata"),
    Pokemon("Meowth"),
    Pokemon("Chansey")
    ]

Charmanderinic = PokemonFogo("Charmander", level = 5)
Squirtleinic = PokemonAgua("Squirtle", level = 5)
Bulbassauroinic = PokemonPlanta("Bulbassauro", level = 5)