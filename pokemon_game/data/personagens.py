from data.pokemon import *


#lista de nomes randomicos para npcs
NOMES = ["Eduarda Linda", "Gustavo", "Gary", "Joãozin da quebrada", "Juan gordo", "Caldas drogado", "Missy", "Leo, o cachorro", "Nasus, o dog", "Singed", "Sharky", "Caitlyn", "Briar", "Jotaro", "Louise pituca", "Koko", "Dragonis", "Nick, o renegado"]



class Personagem:
    def __init__(self, nome = None, pokemons = [], money = 300):
        # nome randomico
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        
        self.pokemons = pokemons
        self.money = money
            
    def __str__(self):
        return self.nome
    
    def mostrar_pokemons(self): #mostra os pokemons que um personagem tem
        if self.pokemons:
            print("\nPokemons de {}:".format(self))
            for pokemon in self.pokemons:
                print(pokemon, "| Tipo : {}".format(pokemon.tipo))
        else: 
            print("{} não tem nenhum pokemon ainda.".format(self))

       
class Player(Personagem):
    tipo = "Player"
    
    def capturar(self, pokemon): #função capturar pokemon
        self.pokemons.append(pokemon)
        print("\n{} capturou {}!".format(self, pokemon))
        
    
    def batalha_selva(self, pokinimigo):
        print("\nUm Pokémon {} selvagem apareceu!".format(pokinimigo))
        result = self.pokemons[0].batalha(pokinimigo)
        if result == "vta":
            print ("\n{} venceu a batalha contra {} selvagem!".format(self, pokinimigo))
            self.ganhar_money(self.rngmoney(pokinimigo))
            pause(), limpar_tela()
        elif result == "vti":
            print ("\n{} selvagem venceu a batalha contra {}!".format(pokinimigo, self))
            pause(), limpar_tela()
            

    def ganhar_money(self, qmoney):
        self.money += qmoney
        print("\nVocê ganhou $ {}!".format(qmoney))
        self.mostrar_money()
        
    def mostrar_money(self):
        print("{} possui um total de $ {}.".format(self, self.money))
        
    def rngmoney(self, pokinimigo): # rng para ganhar dinheiro em lutas, deve ser usado como arg na func ganhar_money
        money = int(pokinimigo.xp * random.uniform(0.06, 0.08))
        return  money
        
        
class Inimigo(Personagem):
    tipo = "Inimigo"

    def __init__(self, nome = None, pokemons=[]):
        
        #pokemons randomicos
        if not pokemons:
            for rand in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))
        
        super().__init__(nome=nome, pokemons=pokemons)

    


# in1 = Inimigo()


# in1.mostrar_pokemons()

# PlayerOne.capturar(pokemon_selvagem)

# PlayerOne.mostrar_pokemons()


        