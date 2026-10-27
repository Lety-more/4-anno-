class ScuolaFilosofica:
    def __init__(self,nome,fondatore,epoca,filosofi):
        self.nome = nome
        self.fondatore = fondatore
        self.epoca = epoca
        self.filosofi = filosofi
    def descrivi(self):
        print (f"nome scuola: {self.nome}, fondatore: {self.fondatore}, epoca: {self.filosofi} ")
        
scuolagenerale=ScuolaFilosofica("corpo","anima","spirito santo","dio")
scuolagenerale.descrivi()