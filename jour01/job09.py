class Produit():
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT + (self.prixHT * self.TVA/100)

    def afficher(self):
        return (f"Nom: {self.nom}, Prix HT: {self.prixHT}, TVA: {self.TVA}, Prix total: {self.CalculerPrixTTC()}")

chaudmarron = Produit("Marron chauds", 40000, 20)
print(chaudmarron.afficher())