import math
class Frazione:
    def __init__(self,numeratore,denominatore):
        self.numeratore=numeratore
        if denominatore == 0:
            raise ValueError("denominatore non puo essere 0")
        self.__denominatore = denominatore
            
    def calcolatore(self):
        risultato = self.numeratore / self.__denominatore
        return risultato
        
    def stampa(self):
        print(f"stampa: {self.numeratore}/{self.__denominatore}")
            
    def semplifica(self):
        risultato = math.gcd(self.numeratore,self.__denominatore)
        nuovo_numeratore = self.numeratore //risultato
        nuovo_denominatore = self.__denominatore//risultato
        return (f"sempilificato: {nuovo_numeratore}/{nuovo_denominatore}")
        
    def moltiplica(self,altra_frazione):
        ris_num=self.numeratore* altra_frazione.numeratore
        ris_den=self.__denominatore* altra_frazione.__denominatore
        return (f"moltiplicazione: {ris_num}/{ris_den}")
        
    
        
f1 = Frazione(4,6)
f2 = Frazione(5,7)
print(f1.calcolatore())
f1.stampa()
print(f1.semplifica())
print(f1.moltiplica(f2))