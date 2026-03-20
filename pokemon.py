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
        return str(f"\n     Nome: {self.nome}\n     Estamina: {self.estamina}\n     Vida: {self.vida}")

    def ataque_normal(self, alvo):
        print(f"\n{self.nome} bateu em {alvo.nome}")
        self.estamina -= 5
        alvo.vida-= 5
        print(f"\nO status do oponente é: {alvo.status()}")
        print(f"Seu status é: {self.status()}")

    def ataque_elementar(self, alvo):
        bonus=0
        if self.tipo == "Fogo" and alvo.tipo == "Planta":
            bonus= 10
        
        elif self.tipo == "Planta" and alvo.tipo =="Agua":
            bonus=10

        elif self.tipo=="Planta" and alvo.tipo == "Fogo":
            bonus=-10

        else:
            bonus=0

        alvo.vida -= 20 + bonus
        self.estamina -= 10

    def ataque_defesa(self, alvo):
        self.estamina -= 15

    def atacar(self, ataque, alvo):
        if ataque==1:
            self.ataque_normal(alvo)

        elif ataque==2:
            self.ataque_elementar(alvo)

        elif ataque==3:
            self.ataque_defesa(alvo)

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

class Pet_agua(Pet):
    tipo= "Agua"

    def bonus_elementar(self, alvo):
        self.ataque_elementar(self.tipo, alvo)


pokemon1=Pet_fogo("Charizard", 30, 100)
pokemon2=Pet_planta("Bulbasaur", 40, 90)
pokemon3= Pet_agua("num sei", 35, 100)

pokemons = [pokemon1, pokemon2, pokemon3]


def batalha(atacante):
    while True:
        defensor = random.choice(pokemons)
        if defensor != atacante:
            break
    
    print("\nVocê entrou em uma batalha!")
    
    while atacante.esta_vivo() and defensor.esta_vivo():
        
        print(f"\nO status do oponente é: {defensor.status()}")
        print(f"O seu status é: {atacante.status()}")


        escolha= int(input("\nO que gostaria de fazer?\n   1.'Atacar'  2.'Fugir'   3.'Capturar'\n"))

        if escolha == 1:
            ataque=int(input("\nEscolha seu ataque:\n     1.'ataque_normal'  2.'ataque_elementar'   3.'ataque_defesa'\n"))
            atacante.atacar(ataque, defensor)


def menu():
    pokemon=int(input("Seja bem-vindo! Escolha seu pokemon para começar sua jornada!\n   1.Fogo  2.Planta\n"))
    if pokemon == 1:
        atacante= pokemon1
    
    elif pokemon == 2:
        atacante= pokemon2

    while True:
        opcao=int(input("\nOlá treinador pokemon! Escolha oque deseja fazer nessa jornada!\n    1.Trocar pokemon    2.Batalhar      5.Sair\n"))

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

