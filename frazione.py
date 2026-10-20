class Frazione:
    def __init__(numeratore,denominatore):
        self.numeratore=numeratore
        if denominatore == 0 :
            print ("il denominatore non puo essere 0")
        
    def calcolatore(self):
        risultato=numeratore/danominatore
        return risultato
    def stampa(self):
        print(f"{numeratore}/{denominatore}")
    def semplifica(self):
        risultato=numeratore % 2 and denominatore % 2
        return risultato 
    def moltiplica(self,f):
        pass
        
        
f1 = Frazione(4,6)
f2 = Frazione(5,7)
print(f1.calcolatore())
print(f1.stampa())
print(f1.semplifica())
print(f1.moltiplica(f2))