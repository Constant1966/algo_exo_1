"""
Auteurs
1.Jeff FORTUNE
2.Lorvenson CONSTANT

Date:  octobre 2023
"""


class Etudiant:
    N = 10
    Matr = ""
    nom = ''
    prenom = ''
    email = ''
    section = ''
    n_des_notes = 0

    def __init__(self, Matr, nom, section):
        self.Matr = Matr
        self.nom = nom

        self.section = section
        self.n_des_notes = 0
        self.notes = []

    def AjouterNote(self, sigle, titre, note):
        if self.n_des_notes < self.N:
            self.notes.append((sigle, titre, note))
            self.n_des_notes += 1
        else:
            print("Le nombre maximum de notes est atteint.")

    def NoteMoyenne(self):
        if self.n_des_notes == 0:
            return 0.0
        total = sum(note for _, _, note in self.notes)
        # total = sum(self.notes)
        return total / self.n_des_notes

    def getMatr(self):
        return self.Matr

    def setMatr(self, Matr):
        self.Matr = Matr

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getPrenom(self):
        return self.prenom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def getSection(self):
        return self.section

    def toString(self):
        return f"Matricule : {self.Matr}, Nom : {self.nom}, Prénom : {self.prenom}, Section : {self.section}"

    def equals(self, etudiant_x):
        return self.Matr == etudiant_x.Matr
