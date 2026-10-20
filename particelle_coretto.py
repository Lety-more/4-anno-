class Particelle:
    def __init__(nome, massa, carica, spin):
        self.nome=nome
        self.massa=massa
        self.carica=carica
        self.spin=spin
   
    def energia_riposo(self):
        c=3*10**9
        return c
    def info(self):
        info= self.nome+ " " +str(self.massa)+" "+ str(self.arica) + " "
        return (info)
    
    def stabile(self):
        stabile=["elettrone","protone","neutrone"]
        if self.nome in stabile:
            return True
        else:
            return False

class Carica:
    def __init__(self,nome,massa,carica,spin,tipo_carica):
        super().__init__(nome,massa,carica,spin,tipo_carica):
            self.tipo_carica=tipo_carica
    def calcola_forza(self,particella,distanza):
        k=3*10**7
        forza=((self.carica*paricella.carica)/distanza**2)*k
        return forza


#istanza della classe che genera l'oggetto partiella generica
particellaGenerica= Particelle( "elettrone" ,12 , 8.0, 5.5)
e1=particellaGenerica.energia_riposo()
print(e1)
i=particellaGenerica.info()
print(i)
stabile=particellaGenerica.stablile()
print(stabile)

particallaCarica("protone", 15,0.9,0.5;"positiva")
f = particallaCarica.calcola_forza(particellaGenerica,78)
print (f)