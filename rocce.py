#definizione classe padre
class Rocce:
    def __init__(self,composizione_minerale,ciclo,stato):
        self.composizione_minerale=composizione_minerale
        self.ciclo=ciclo
        self.stato=stato
        
# definizione classe figlie
class Magmetica(Rocce):
    def __init__(self,composizione_minerale,ciclo,stato):
        super().__init__(self,composizione_minerale,ciclo,stato)
    def rafredamento(self):
        print("la roccia e in fase di rafredamento")

class Sedimentaria(Rocce):
    def __init__(self,composizione_minerale,ciclo,stato):
        super().__init__(self,composizione_minerale,ciclo,stato)
    
        
class Metamorfica(Rocce):
    def __init__(self,composizione_minerale,ciclo,stato):
        super().__init__(self,composizione_minerale,ciclo,stato)

#istanzioare la classe padre
rocciagenrica=Rocce("CA","ciclo A","FONDAMENTALE")
#istanzioare la classe figlia
rocciamagmatica=Rocce("CA","ciclo A","FONDAMENTALE")
rocciamagmatica.rafredamento()
