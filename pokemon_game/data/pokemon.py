import random
from data.functions.osfunctions import * 

LEVELS = {}

def importarlevxp():
    with open("./data/levels/levels.csv", "r") as levelxp:
        linhas = levelxp.readlines()
        for linha in linhas:
            if linha == linhas[0]:
                pass
            else:
                lv, xp = linha.strip().split(";")
                LEVELS [int(lv)] = {
                    "LV" : int(lv),
                    "XP" : int(xp)
                }

importarlevxp()

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
            
        self.xp = self.leveltoxp(self.level) #transforma o level em xp
         
        # nome = especie caso vazio    
        if nome:
            self.nome = nome
        else:
            self.nome = especie
            
            self.atk = int(self.level * 1.4)
            self.vida = int(8 + self.level * 2.5)            
    
    def leveltoxp(self, level):
        return LEVELS[level]["XP"]
    
    def xptolevel(self, xp):
        if xp < LEVELS[(self.level + 1)]["XP"]:
            diff = (LEVELS[(self.level + 1)]["XP"] - self.xp) 
            print("\nFaltam {} pontos de experiência para {} subir de nível.".format(diff, self))
        else:
            for level in LEVELS:
                if xp < LEVELS[level]["XP"]: 
                    self.level = (LEVELS[level]["LV"] - 1)
                    print("\nParabéns! {} evoluiu para o nível {}!".format(self, self.level))
                    break
                else:
                    pass
            
    def tipok(self):
        return "Normal"
        
    def __str__(self):
        return "{} ({})".format(self.especie, self.level) #print mostra especie do pokemon e level
    
    def atacar(self, inimigo):
        self.msgatk(inimigo)
        dano = self.rngatk()
        inimigo.vida = inimigo.vida - dano 
        print("\n{} perdeu {} pontos de vida.".format(inimigo, dano))
        print("\nPontos de vida atuais de {}: {} ".format(inimigo, inimigo.vida))
        if inimigo.vida <= 0:
            return "Win" #retorna para func batalha
        
    def rngatk(self):
        rng = random.random()
        if rng >= 0.96: #critico
            print("\nFoi um golpe crítico!!!")
            return int(self.atk * 2)
        elif rng >= 0.70: #forte
            print("\nFoi um ataque forte!")
            return int(self.atk * 1.4)
        elif rng >= 0.30: #normal
            print("\nFoi um ataque normal.")
            return self.atk
        elif rng  >= 0.04: #fraco
            print("\nFoi um ataque fraco.")
            return int(self.atk * 0.6)
        else: #erro critico
            print("\nFoi um ERRO crítico!")
            return int(self.atk * 0.2)
        
                
    def msgatk(self, inimigo):
        print(self.textosatk(inimigo))
    
    def winxp(self, pokinimigo):
        maisxp = 0
        # xp equacao
        if pokinimigo.level < 10:
            maisxp = int(50 + pokinimigo.xp * 0.1)  
        elif pokinimigo.level < 20:
            maisxp = int(200 + pokinimigo.xp * 0.04) 
        elif pokinimigo.level < 30:
            maisxp = int(400 + pokinimigo.xp * 0.02)             
        elif pokinimigo.level < 40:
            maisxp = int(800 + pokinimigo.xp * 0.01) 
        elif pokinimigo.level < 50:
            maisxp = int(1200 + pokinimigo.xp * 0.005)
        elif pokinimigo.level < 60:
            maisxp = int(1800 + pokinimigo.xp * 0.0025)
        elif pokinimigo.level < 70:
            maisxp = int(2400 + pokinimigo.xp * 0.00125)
        elif pokinimigo.level < 80:
            maisxp = int(900 + pokinimigo.xp * 0.00075)
        elif pokinimigo.level < 90:
            maisxp = int(3300 + pokinimigo.xp * 0.000375)
        elif pokinimigo.level <= 100:
            maisxp = int(3800 + pokinimigo.xp * 0.0001875)
        else: 
            print("ERRO NO XP.")
        
        maisxp = int(maisxp * random.uniform(0.99, 1.01))  
        self.xp += maisxp
        print("\n{} ganhou {} pontos de experiência.".format(self, maisxp))
        self.xptolevel(self.xp)
           
    def batalha(self, pokinimigo):
        vta = None
        vti = None
        ESCOLHAS =["atk"]
        
        while vta != "Win" and vti != "Win":
            print("\n----------|----------|----------|----------") #vez do player
            print("\nÉ a vez de {}!".format(self))
            print("\nVida atual de {}: {}".format(self, self.vida))
            print("Vida atual de {} inimigo: {}".format(pokinimigo, pokinimigo.vida))
            print("\n1 - Atacar {}".format(pokinimigo))
            print("2 - Trocar de pokemon")
            print("3 - Lançar Pokébola")
            print("4 - Fugir")
            print("\n----------|----------|----------|----------")
            while True:
                resb = input("\nSelecione a ação desejada: ")
                if resb == '1':
                    limpar_tela()
                    print("\n----------|----------|----------|----------\n")
                    vta = self.atacar(pokinimigo)
                    print("\n----------|----------|----------|----------")
                    break
                elif resb == '2':
                    #todo
                    print("\nOpção ainda indisponível")
                elif resb == '3':
                    #todo
                    print("\nOpção  ainda indisponível")
                elif resb == '4':
                    #todo
                    print("\nOpção  ainda indisponível")
                else:
                    print("\n<<<<<<<<[ERRO] Opção inválida")
            pause(), limpar_tela()
            if vta == "Win":
                print("\n{} desmaiou!".format(pokinimigo))
                self.winxp(pokinimigo)
                return "vta"
            print("\n----------|----------|----------|----------")
            print("\nÉ a vez de {}!".format(pokinimigo)) # vez do bot
            escolha = random.choice(ESCOLHAS)
            if escolha == "atk":
                print("\n{} escolheu atacar!".format(pokinimigo))
                vti = pokinimigo.atacar(self)
                print("\n----------|----------|----------|----------")
                pause(), limpar_tela()
            if vti == "Win":
                return "vti"
            
            
    def textosatk(self, inimigo):
        
        textos = ["{} desferiu golpes rápidos consecutivos em {}!".format(self, inimigo),
                  "Com velocidade impressionante, {} atacou {} ferozmente!".format(self, inimigo),
                  "{} canalizou sua força interior e desferiu um golpe esmagador em {}!".format(self, inimigo),
                  "Com uma força esmagadora, {} golpeou {}!".format(self, inimigo),
                  "Com destreza notável, {} investiu contra {}!".format(self, inimigo)]
        
        return random.choice(textos)        
            


                    
class PokemonEletrico(Pokemon):
    def tipok(self):
        return "Elétrico"
    
    def textosatk(self, inimigo):
        
        textos = ["{} lançou uma rajada elétrica em {}!".format(self, inimigo),
                  "{} soltou uma explosão de energia elétrica em {} que se espalhou pelo campo de batalha, deixando todos eletrizados!".format(self, inimigo),
                  "Uma onda elétrica se espalhou pelo chão, causando tremor enquanto {} lançava sua eletricidade contra {}!".format(self, inimigo),
                  "{} foi cercado por um campo de força elétrica, lançado por {}, e acabou se machucando!".format(inimigo, self),
                  "Com força surpreendente, {} invocou os poderes do trovão e relâmpagos atingiram {}!".format(self, inimigo)]
        
        return random.choice(textos)
               
class PokemonFogo(Pokemon):
    def tipok(self):
        return "Fogo"
    
    def textosatk(self, inimigo):
        
        textos = ["{} cuspiu uma bola de fogo que atingiu {}, deixando ele tostado!".format(self, inimigo),
                  "Com poder incrível, {} invocou um inferno de fogo, cercando {} em chamas!".format(self, inimigo),
                  "{} invocou um furacão de chamas na direção de {}!".format(self, inimigo),
                  "{} deesferiu um chute flamejante em {}!".format(inimigo, self),
                  "Surpreendentemente, {} invocou uma erupção vulcânica no campo de batalha e atingiu {}!".format(self, inimigo)]
        
        return random.choice(textos)
    
class PokemonAgua(Pokemon):
    def tipok(self):
        return "Água"
    
    def textosatk(self, inimigo):
        
        textos = ["{} lançou um jato de bolhas mortal em {}!".format(self, inimigo),
                  "{} invocou um redemoinho aquático nos pés de {}!".format(self, inimigo),
                  "Com poder surpreendente, {} criou um tsunami de água, fazendo ondas gigantes atingirem {}!".format(self, inimigo),
                  "{} se camuflou nas águas rasas de um lago, esperando o momento certo para lançar um ataque surpresa em {}!".format(self, inimigo),
                  "{} disparou uma poderosa bomba hidráulica que inundou o campo de batalha, deixando {} submerso em água!".format(self, inimigo)]
        
        return random.choice(textos)

class PokemonPlanta(Pokemon):
    def tipok(self):
        return "Planta"
    
    def textosatk(self, inimigo):
        
        textos = ["{}  fez um vendaval de folhas, criando um furacão verde que pegou {} desprevenido!".format(self, inimigo),
                  "{} invocou uma chuva de plantas carnívoras em {}!".format(self, inimigo),
                  "{} lançou raízes que envolveram {}, apertando-o com uma força esmagadora crescente!".format(self, inimigo),
                  "{} lançou um conjunto de folhas lâmina, afiadas como navalhas, que cortaram {} implacavelmente!".format(self, inimigo),
                  "{{ lançou um poderoso raio solar, criando um raio de energia concentrada que devastou {} e também o campo de batalha!".format(self, inimigo)]
        
        return random.choice(textos)
               
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
    Pokemon("Rattata"),
    Pokemon("Meowth"),
    Pokemon("Chansey")
    ]


Charmanderinic = PokemonFogo("Charmander", level = 5)
Squirtleinic = PokemonAgua("Squirtle", level = 5)
Bulbassauroinic = PokemonPlanta("Bulbassauro", level = 5)
Pikachui = PokemonEletrico("Pikachu", level = 5)
Rattatainic = Pokemon("Rattata", level = 3)



