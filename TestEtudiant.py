# package
# POO;
#
# import java.util.Arrays;
# // import java.util.Comparator;
#
# public
#
#
# class TestEtudiant {
#
# public static void main(String[] args) {
#
#
from POO.Etudiant import Etudiant

if __name__ == '__main__':
    e = Etudiant("1897453", "John", 3)

    e.AjouterNote("INF2010", "Structures de données et algorithmes", 4)
    e.AjouterNote("LOG2810", "Structures discrètes", 5)
    e.AjouterNote("INF2610", "Noyau d'un système d'exploitation", 3)
    print(f'\n {e.NoteMoyenne()}')

    john = Etudiant("1797453", "john", 2)
    Caroline = Etudiant("1897053", "Caroline", 1)
    Antoine = Etudiant("1297453", "Antoine", 2)
    Karl = Etudiant("1797433", "Karl", 1)
    Ahmed = Etudiant("1897453", "Ahmed", 2)
    Sam = Etudiant("1977411", "Sam", 3)
    #
    etudiants = [john, Caroline, Karl, Ahmed, Sam]

    #  Completer le pseudo-code pour trie les etudiants par nom -section
    print(' Par le nom  \n ')
    print("-----------\n")
    # Completer
    print("-----------\n")
    #
    #
    #
    #
    print(" Par section \n")
    print("-----------\n")
    # // Completer
    print("-----------\n")

    carlos =  Etudiant("1698853", "carlos", 3)
    Ines = Etudiant("1897456", "Ines", 2)

    print(f' \n carlos == Ines:         {carlos==Ines}')
    print("carlos.equals(Ines):   " + (carlos.equals(Ines)))

