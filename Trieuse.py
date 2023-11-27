
from Etudiant import Etudiant


class Trieuse:
    class NomOrdre:
        def compare(self, x, y):
            return x.getNom().lower() < y.getNom().lower()

    class SectionOrdre:
        def compare(self, x, y):
            return x.getSection() < y.getSection()

    Par_nom = NomOrdre()
    Par_section = SectionOrdre()


def main():
    e = Etudiant("1897453", "John", 3)
    e.AjouterNote("INF2010", "Structures de données et algorithmes", 4)
    e.AjouterNote("LOG2810", "Structures discrètes", 5)
    e.AjouterNote("INF2610", "Noyau d'un système d'exploitation", 3)
    print(e.NoteMoyenne())

    john = Etudiant("1797453", "John", 2)
    Caroline = Etudiant("1897053", "Caroline", 1)
    Antoine = Etudiant("1297453", "Antoine", 2)
    Karl = Etudiant("1797433", "Karl", 1)
    Ahmed = Etudiant("1897453", "Ahmed", 2)
    Sam = Etudiant("1977411", "Sam", 3)

    etudiants = [john, Caroline, Karl, Ahmed, Sam]

    # Tri par nom
    print("Par le nom")
    print("----------")
    etudiants_par_nom = sorted(etudiants, key=lambda x: x.getNom())
    for etudiant in etudiants_par_nom:
        print(etudiant.toString())

    print("----------")

    # Tri par section
    print("Par section")
    print("----------")
    etudiants_par_section = sorted(etudiants, key=lambda x: x.getSection())
    for etudiant in etudiants_par_section:
        print(etudiant.toString())

    print("----------")

    carlos = Etudiant("1698853", "Carlos", 3)
    Ines = Etudiant("1897456", "Ines", 2)

    print("carlos == Ines:        " + str(carlos == Ines))
    print("carlos.equals(Ines):   " + str(carlos.equals(Ines)))


if __name__ == '__main__':
    main()
