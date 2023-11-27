from Article import Article


class CadreDiplome(Article):
    def __init__(self, NumProduit, nom, prix, categorie):
        super().__init__(NumProduit, nom, prix)
        self.categorie = categorie

    def __init__(self, NumProduit, nom, prix, couleur, categorie):
        super().__init__(NumProduit, nom, prix)
        self.couleur = couleur
        self.categorie = categorie

    def getArticleType(self):
        return "CadreDiplome"

    def getCategorie(self):
        return self.categorie

    def setCategorie(self, categorie):
        self.categorie = categorie

