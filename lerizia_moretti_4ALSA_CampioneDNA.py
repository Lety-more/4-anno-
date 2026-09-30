class CampioneDNA:
    """questa classe serve a gestire un campione di DNA nel laboratorio"""
    laboratorio = "LabGen-BioApp"
    def __init__(self, codice_campione, sequenza, geni_mappati, mutazioni_rilevate):
        """inizilizza l'oggetto"""
        self.__codice_campione = codice_campione
        self.__sequenza = sequenza.upper()
        self.__geni_mappati = geni_mappati
        self.__mutazioni_rilevate = mutazioni_rilevate
    def aggiungi_gene(self, nome_gene):
        """aggiunge un gene alla lista solo se non ce"""
        if nome_gene not in self.__geni_mappati:
            self.__geni_mappati.append(nome_gene)
            print("gene aggiunto!")
        else:
            print("questo gene ce gia, non lo aggiungo.")
    def registra_mutazione(self, posizione, tipo_mutazione):
        """salva una mutazione nel dizionario usando la posizzione come chiave"""
        self.__mutazioni_rilevate[posizione] = tipo_mutazione
        print("mutazione registrata")
    def calcola_percentuale_gc(self):
        """conta le G e le C e fa la percentuall sul totale della sequenza"""
        lunghezza = len(self.__sequenza)
        if lunghezza == 0:
            return 0
        else:
            quanteG = self.__sequenza.count("G")
            quanteC = self.__sequenza.count("C")
            totaleGc = quanteG + quanteC
            risultato = (totaleGc / lunghezza) * 100
            return risultato
    def stampa_report(self):
        """stampa a schermo tutti i dati del campione"""
        print("Codice:", self.__codice_campione)
        print("Laboratorio:", self.laboratorio)
        if len(self.__sequenza) > 20:
            pezzoSequenza = self.__sequenza[:20]
            print("Sequenza:", pezzoSequenza + "...")
        else:
            print("sequenza:", self.__sequenza)
        print("geni identificati:", self.__geni_mappati)
        print("mutazioni trovate:", self.__mutazioni_rilevate)
primoCampione = CampioneDNA("DNA-4029", "atcggctagctagctagctagctagcta", ["geneA"], {45: "sostituzione"})
primoCampione.stampa_report()
primoCampione.aggiungi_gene("ampR")
primoCampione.aggiungi_gene("geneA")
primoCampione.registra_mutazione(120, "delezione")
percentualeGc = primoCampione.calcola_percentuale_gc()
print("la percentuale di GC e:", percentualeGc, "%")
primoCampione.stampa_report()
