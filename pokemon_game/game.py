from data.pokemon import *
from data.personagens import *
from data.functions.osfunctions import *  
 
def iniciogame():
    limpar_tela()
    print("Você é um adolescente apaixonado pelo mundo Pokémon, mas sua mãe nunca te deixou explorar o universo Pokémon, ela diz que é muito perigoso para uma criança.")
    print("\nPorém, hoje é seu aniversário de 15 anos e ela permitiu que você visitasse o laboratório de pesquisa do Professor Bird, um renomado mestre Pokémon da sua cidade: Pallet Town, na região de Kanto")
    pause(), limpar_tela()
    print("?: Olá pequeno aventureiro! ")
    print("\n?: Eu sou o Professor Bird, um mestre Pokémon!")
    pause(), limpar_tela()
    print("Prof. Bird: Vejo que está interessado no universo Pokémon, eles são realmente incríveis!")
    print("\nProf. Bird: Neste mundo existem pokémons de todos os tipos: de fogo, água, planta, elétricos e muitos outros!")
    print("\nProf. Bird: Cada pokémon tem sua peculiaridade e características únicas!")
    pause(), limpar_tela()
    print("Prof. Bird: Qual é o seu nome, jovem aventureiro?")
    nomeplayer = input("\nDigite seu nome: ")
    playerone = Player(nomeplayer)
    limpar_tela()
    print("Prof. Bird: {}! Este é um belo nome para um jovem como você!".format(playerone))
    print("\nUm barulho muito alto e estranho interrompe a conversa: BRIAAAAAAAAAAAARRRRR!")
    pause(), limpar_tela()
    print("Prof. Bird: NOSSA! este deve ser dos grandes!")
    print("\nProf. Bird: {}, desculpe interromper a nossa conversa mas terei que averiguar este barulho!".format(playerone))
    print("Prof. Bird: Ele veio da floresta aqui acima!")
    print("\nBarulho misterioso: BRIAAAAAAAAARRRAAARRRRR!")
    pause(), limpar_tela()
    print("O professor vai às pressas para o local onde está vindo o barulho...")
    print("\nVocê, dominado pela curiosidade e também pela sua paixão pokémon, segue o professor até a floresta.")
    pause(),limpar_tela()
    print("Chegando na floresta, você se depara com um pokémon descontrolado atacando o professor com seus dentes e garras!")
    print("\nRattata: BRIIIAR! BRIAT! BRIAAAAAARRRRRRR!")
    print("\nProf. Bird: Ei! Você aí! Por favor me ajude!")
    print("Prof. Bird: Na minha bolsa! Tem pokébolas! Rápido! SOCORRO!!!")
    pause(),limpar_tela()
    return playerone
       
def escolher_inicial(player):
    print("{}! Prof. Bird está com problemas!\n \nLibere um pokémon da bolsa dele e salve-o! :".format(player))
    print("\n----------|----------|----------|----------")
    print("\nPokémon: Charmander | Tipo: Fogo")
    print("\nPokémon: Squirtle | Tipo: Água")
    print("\nPokémon: Bulbassauro | Tipo : Planta")
    print("\n----------|----------|----------|----------")
    while True:    
        resinicial = input("\nQual pokémon você escolhe? : ")
        
        if resinicial == "Charmander" or resinicial == "charmander":
            playerone.capturar(Charmanderinic)
            break
        elif resinicial == "Squirtle" or resinicial == "squirtle":
            playerone.capturar(Squirtleinic)
            break
        elif resinicial == "Bulbassauro" or resinicial == "bulbassauro":
            playerone.capturar(Bulbassauroinic)
            break
        else:
            print("\n<<<<<<<< [ERRO] Por favor, digite o nome do pokémon corretamente!")
    pause(), limpar_tela()
    playerone.batalha_selva(Rattatainic)

gary = Inimigo("gary")
gary.mostrar_pokemons()
pause()
playerone = iniciogame()
escolher_inicial(playerone)

         