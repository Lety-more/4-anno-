"""nome_1="Tommaso"
cognome_1="STRA"
eta_1=25


nome_2="Luigi"
cognome_2="Rossi"
eta_2=28


print("1 persona")
print(eta_1)
print("2 persona")
print(eta_2)

"""

#uso degli oggetti
class Persona:
    def __init__(self,nome,cognome,eta,lavoro):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.lavoro = lavoro
    def stampaEta(self):
        print(self.eta)
    def stampalavoro(self):
        print(self.lavoro)
    def eta_minorenne(self,eta):
        if self>18:
            print("maggiorenne")
        else:
            print("minorenne")
prima_persona= Persona("Tommaso", "Stra", 25, "meccanico")
seconda_presona= Persona("Luigi", "Rossi", 28, "ingengiere")
prima_persona.stampaEta()
seconda_presona.stampaEta()
prima_persona.stampalavoro()
seconda_presona.stampalavoro()
prima_persona.eta_minorenne()
seconda_presona.eta_minorenne()