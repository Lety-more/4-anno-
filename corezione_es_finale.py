class Esperimento:
    def __init__(self, titolo, operatore):
        self.titolo = titolo
        self.operatore = operatore
        self.sostanze = []
        
    def aggiungi_sostanza(self, sostanza):
        self.sostanze.append(sostanza)
        
class Sostanza:
    def __init__(self, nome):
        self.nome = nome
    def stampa_nome(self):
        print(self.nome)
        
#creo un oggetto della classe sostanza 
ferro=Sostanza("Ferro")
#creo un oggentto della classe esperimento 
exp = Esperimento("Preparazione soluzione","Letizia")
#aggiungo la sostanza al esoerimento
exp.aggiungi_sostanza(ferro)
# copia foto
exp.sostanze[0].stampa_nome()
# aggiungo una seconda sostanza al espermento
oro=Sostanza("oro")
exp.aggiungi_sostanza(oro)
exp.sostanze[1].stampa_nome()
print(exp.sostanze)

