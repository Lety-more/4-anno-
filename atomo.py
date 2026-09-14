class Atomo:
    def __init__(self,simbolo,numero_atomico,massa):
        self.simbolo = simbolo
        if numero_atomico<0:
            raise ValueError("il numero atomico deve essere sempre positivo")
        else:
            self.numero_atomico=numero_atomico
        self.massa = massa
    def is_stabile(self):
        A = round(self.massa)
        neutroni = A - self.numero_atomico
        rapporto = neutroni / self.numero_atomico
        if 0.9<=rapporto<=1.6:
            print ("e stabile")
        else:
            print ("non e stabile")
idrogeno = Atomo("H",1,1.008)
try:
    ferro = Atomo("Fe",26,55.845)
except ValueError:
    print("il numero atomico deve essere sempre positivo")