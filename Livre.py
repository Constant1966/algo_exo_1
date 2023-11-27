from Article import Article


class Livre(Article):
    def __init__(self, NumProduit, nom, prix, format):
        super().__init__(NumProduit, nom, prix)
        self.format = format

    def getArticleType(self):

        return "Livre"

    def getFormat(self):
        return self.format

    def setFormat(self, format):
        self.format = format
