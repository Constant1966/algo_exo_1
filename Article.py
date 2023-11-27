
class Article:
    def __init__(self, num_produit, nom, prix_net=0):
        self.__num_produit = num_produit
        self.__nom = nom
        self._prix_net = prix_net

    def get_num_produit(self):
        return self.__num_produit

    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    def get_prix_net(self):
        return self._prix_net

    def set_prix_net(self, prix_net):
        self._prix_net = prix_net

    def get_VAT(self):
        # Supposons que la TVA est de 20%
        return 0.20

    def get_prix(self, count):

        return self._prix_net * count

    def get_article_type(self):

        return "Article"

    def toString(self):

        return f"Numéro de produit : {self.__num_produit}, Nom : {self.__nom}, Prix net : {self._prix_net:.2f} €"

