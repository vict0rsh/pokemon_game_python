import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPressione a tecla <ENTER> para continuar...")