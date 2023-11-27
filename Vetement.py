from Article import Article


class Vetement(Article):
    def __init__(self, NumProduit, nom, taille):
        super().__init__(NumProduit, nom)
        self.taille = taille

    def __init__(self, NumProduit, nom, prix, taille):
        super().__init__(NumProduit, nom, prix)
        self.taille = taille

    def getArticleType(self):
        return "Vetement"

    def getTaille(self):
        return self.taille

    def setTaille(self, taille):
        self.taille = taille



