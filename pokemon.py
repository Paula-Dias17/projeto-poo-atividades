import random

class Pet:
    nome = str
    poder = float
    vida = int
    estamina = int

    def __init__(self, nome, poder, vida, estamina = 25):
        self.nome = nome
        self.poder = poder
        self.vida = vida
        self.estamina = estamina

    def status(self):
        return str(f"Nome: {self.nome}\nEstamina: {self.estamina}\nVida: {self.vida}")

    def ataque_normal(self):
        print(f"{self.nome} bateu em seu oponente")
        self.estamina -= 5

    def ataque_elementar(self, tipo, alvo):
        if tipo == "Fogo" and alvo == "Planta":
            bonus= 10
            return bonus
        
        self.estamina -= 10

    def ataque_defesa(self):
        self.estamina -= 15

    def atacar(self, ataque):
        if ataque==1:
            self.ataque_normal()

        elif ataque==2:
            self.ataque_elementar()

        elif ataque==3:
            self.ataque_defesa()

    def fugir(self):
        pass

    def capturar(self):
        pass
    
    def esta_vivo(self):
        if self.vida == 0:
            return False
        else:
            return True
        

class Pet_fogo(Pet):
    tipo= "Fogo"

    def bonus_elementar(self, alvo):
        self.ataque_elementar(self.tipo, alvo)
    
class Pet_planta(Pet):
    tipo= "Planta"

    def bonus_elementar(self, alvo):
        self.ataque_elementar(self.tipo, alvo)


pokemon1=Pet_fogo("Charizard", 30, 100)
pokemon2=Pet_planta("bulbasaur", 40, 90)


def batalha(atacante, defensor):
    escolha=input("Você entrou em uma batalha! O que gostaria de fazer?\n   1.Digite: 'Atacar'  2.Digite: 'Fugir'   3.Digite'Capturar'\n")

    while True:
        escolha= input("Seu pokemon ainda está em batalha! O que gostaria de fazer?\n   1.Digite: 'Atacar'  2.Digite: 'Fugir'   3.Digite'Capturar'\n")
        if escolha == 'Atacar':
            ataque=int(input("Escolha seu ataque:\n     1.'ataque_normal'  2.'ataque_elementar'   3.'ataque_defesa'\n"))
            atacante.atacar(ataque)
            atacante


def menu():
    pokemon=int(input("Seja bem-vindo! Escolha seu pokemon para começar sua jornada!\n   1.Fogo  2.Planta\n"))
    if pokemon == 1:
        atacante= pokemon1
    
    elif pokemon == 2:
        atacante= pokemon2

    while True:
        opcao=int(input("Olá treinador pokemon! Escolha oque deseja fazer nessa jornada!\n    1.Trocar pokemon    2.Batalhar      5.Sair\n"))

        if opcao==1:
            pokemon=int(input("Escolha seu pokemon!\n   1.Fogo  2.Planta\n"))
            if pokemon == 1:
                atacante= pokemon1
            
            elif pokemon == 2:
                atacante= pokemon2
            
        elif opcao== 2:
            batalha(atacante)

        elif opcao==5:
            break

menu()


# nome = str
# estamina = int
# poder = float
# vida = int

