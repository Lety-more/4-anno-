class Atomo:
    def __init__(self,simbolo,numero_atomico,massa):
        #simbolo,numero_atomico,massa sono artibutti publici 
        self.simbolo = simbolo
        if numero_atomico<0:
            raise ValueError("il numero atomico deve essere sempre positivo")
        else:
            self.numero_atomico=numero_atomico
        self.massa = massa
        #orbitale e un atributo privato
        self.__orbitale = "2p"
        
    def is_stabile(self):
        A = round(self.massa)
        neutroni = A - self.numero_atomico
        rapporto = neutroni / self.numero_atomico
        if 0.9<=rapporto<=1.6:
            print ("e stabile il")
        else:
            print ("non e stabile")
    def print_orbitale(self):
        print(idrogeno.__orbitale)

 
    def new_massa(self):
        dato=input("inserisci la nuova massa: ")
        self.massa= float(dato)
        print(f"nuova massa: {self.massa}")
        
        
    def new_orbitale(self):
        dato2=input("inserisci la nuova orbitale: ")
        self.orbile= dato2
        print(f"nuova massa: {self.orbile}")
    
    def gas_nobile(self):
        numeri_gas = [2, 10, 18, 36, 54, 86, 118]
        for numero in numeri_gas:
            if numero == self.numero_atomico:
                return True
        #if self.numero_atomico in numeri_gas:
         #   return True
        # o
        #if self.numero_atomico == 2 or numero_ .......:
        #    return True
         
        
idrogeno = Atomo("H",1,1.008)
idrogeno.is_stabile()
#per accedere al esterno a un elemneto publico basta la sintassi della riga sicessiva
print(idrogeno.simbolo)
#per ccedere daal esteno ad un atruburo privato devo utilizare un metodo 
print(idrogeno.print_orbitale())
#idrogeno.new_massa()
#idrogeno.new_orbitale()
idrogeno.gas_nobile() # manca una parte 
try:
    ferro = Atomo("Fe",26,55.845)
except ValueError:
    print("il numero atomico deve essere sempre positivo")


