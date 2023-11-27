from Sac import Sac
from File import File
from Pile import Pile

# Tester la classe Sac
sac = Sac()
sac.ajouter(1)
sac.ajouter(2)
sac.ajouter(3)

print("Contenu du sac :")
for item in sac.iterer():
    print(item)

# Tester la classe File
file = File()
file.enfiler("A")
file.enfiler("B")
file.enfiler("C")

print("Contenu de la file :")
for item in file.iterer():
    print(item)

# Tester la classe Pile
pile = Pile()

pile.empiler("X")
pile.empiler("Y")
pile.empiler("Z")

print("Contenu de la pile :")
for item in pile.iterer():
    print(item)
