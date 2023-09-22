class Pokemon:
    
    def __init__(self, especie, level = 1, nome = None):
        self.especie = especie
        self.level = level
        if nome:
            self.nome = nome
        else:
            self.nome = especie            
        
    def __str__(self):
        return "{} ({})".format(self.especie, self.level)
    
    def atacar(self, inimigo):
        print("{} atacou {}".format(self, inimigo))
        
class PokemonEletrico(Pokemon):
    tipo = 'Elétrico'        

class PokemonFogo(Pokemon):
    tipo = "Fogo" 
    
class PokemonAgua(Pokemon):
    tipo = "Água"

class PokemonPlanta(Pokemon):
    tipo = "Planta"
    
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
                                          
meu_pokemon = PokemonFogo("Charmander")

pokemon_amigo = PokemonAgua("Squirtle", "20")

pokemon_selvagem = PokemonEletrico("Pikachu", "15")
