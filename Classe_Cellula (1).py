class Organello:
    def __init__(self, nome, efficienza, energia_base):
        self.nome = nome
        self.efficienza = efficienza

        if energia_base <= 0:
            raise ValueError("L'energia base deve essere positiva.")

        if not 0 <= efficienza <= 1:
            raise ValueError("L'efficienza deve essere tra 0 e 1.")

        self.__energia_base = energia_base

    def calcola_energia(self):
        return self.__energia_base * self.efficienza
    
    def info(self):
        print(f"Nome organello: {self.nome}")
        print(f"Efficienza: {self.efficienza}")
        print(f"Energia prodotta: {self.calcola_energia()}")


class Cellula:
    def __init__(self, nome, intatto, membrana, forma, dimensione):
        self.nome = nome
        self.intatto = intatto
        self.forma = forma

        if not isinstance(membrana, bool):
            raise ValueError("La membrana deve essere True o False.")

        self.__membrana = membrana

        if dimensione <= 0:
            raise ValueError("La dimensione deve essere positiva.")

        self.dimensione = dimensione
        self.organello=[]
        """
        if len organelli>0:
            self.organelli=organelli
        else:
            raise ValueError
        self.__energia_totale = 0
        """
    def numero_organelli(self):
        return len(self.__organelli)

    def tipo_nutrizione(self):
        return "Non specificato"

    def aggiungi_organello(self, organello):
        if not isinstance(organello, Organello):
            raise ValueError("Devi inserire un oggetto Organello.")

        self.__organello.append(organello)

    def calcola_energia_totale(self):
        self.__energia_totale = 0

        for organello in self.__organelli:
            self.__energia_totale += organello.calcola_energia()

        return self.__energia_totale
    
    def info(self):
        print(f"Nome cellula: {self.nome}")
        print(f"Intatta: {self.intatto}")
        print(f"Forma: {self.forma}")
        print(f"Dimensione: {self.dimensione}")
        print(f"Numero organelli: {self.numero_organelli()}")
        print(f"Tipo di nutrizione: {self.tipo_nutrizione()}")
        print(f"Energia totale: {self.calcola_energia_totale()}")


class CellulaAnimale(Cellula):
    def __init__(self, nome, intatto, membrana, forma,
                 dimensione, centrioli):
        super().__init__(nome, intatto, membrana, forma, dimensione)

        if not isinstance(centrioli, bool):
            raise ValueError("I centrioli devono essere True o False.")

        self.centrioli = centrioli

    def tipo_nutrizione(self):
        return "Eterotrofa"
    
    def info(self):
        super().info()
        print(self.centrioli)


class CellulaVegetale(Cellula):
    def __init__(self, nome, intatto, membrana, forma,
                 dimensione, spessore_parte):
        super().__init__(nome, intatto, membrana, forma, dimensione)

        if spessore_parte <= 0:
            raise ValueError(
                "Lo spessore della parete deve essere positivo.")

        self.spessore_parte = spessore_parte

    def tipo_nutrizione(self):
        return "Autotrofa"
    
    def info(self):
        super().info()
        print(self.spessore_parte)
        
mitocondrio_animale = Organello("Mitocondrio", 0.8, 100)
ribosoma_animale = Organello("Ribosoma", 0.5, 20)
mitocondrio_vegetale = Organello("Mitocondrio", 0.8, 100)
cloroplasto = Organello("Cloroplasto", 0.9, 150)
ribosoma_vegetale = Organello("Ribosoma", 0.5, 20)
animale = CellulaAnimale("Cellula animale",True,True,"Irregolare",20,True)
vegetale = CellulaVegetale("Cellula vegetale",True,True,"Regolare",56,3.7)
animale.aggiungi_organello(mitocondrio_animale)
animale.aggiungi_organello(ribosoma_animale)
vegetale.aggiungi_organello(mitocondrio_vegetale)
vegetale.aggiungi_organello(cloroplasto)
vegetale.aggiungi_organello(ribosoma_vegetale)
print(animale.nome)
print(animale.tipo_nutrizione())
print(animale.numero_organelli())
print(animale.calcola_energia_totale())
print(animale.centrioli)
print(vegetale.nome)
print(vegetale.tipo_nutrizione())
print(vegetale.numero_organelli())
print(vegetale.calcola_energia_totale())
print(vegetale.spessore_parte)
try:
    organello_errato = Organello("Mitocondrio", 0.8, -10)
except ValueError as errore:
    print(errore)
print(animale.info())
print(vegetale.info())


"""
lista_organelli=[]
mitocondri=Organello("Mitocondrio",0.95,190)
lista_organelli.append(mitocondrio)
cellulagenrica=Cellula(True,lista_organelli,True,"cerchio",2,"AK67","vegano")
print(cellulagenrica.numeroorganelli())

"""