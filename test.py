import CadreDiplome
import Livre
import Article
import Vetement

article = Article()


def CalculePrix(articles):
    prix = 0
    for i in articles:
        print(f'{articles},{article} , {article.getPrix(1)}, {article.getArticleType()}')
        prix += article.getPrix(1)
    print(f'LE PRIX TOTALE =   {prix}')


if __name__ == '__main__':
    livre = Livre("23400199911", "Initiation à la théorie des probabilités", 33.95, "pdf")
    cadreDiplome = CadreDiplome("02045", "Cadre pour diplôme BAC", 139, "Classique")
    vetement = Vetement("4549632", "T-shirt Bleu Caraibes (large) Homme Polytechnique", 16.99, 54)

    articles = [livre, cadreDiplome, vetement]

    CalculePrix(articles)
