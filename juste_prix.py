from random import randint

x = randint(1, 100)
vie = 10

while vie > 0:
    print(f"Il te reste {vie} vies")
    rep = int(input("Quel est ton nombre ? "))
    if rep == x:
        print("Bravo, tu as réussi le jeu !")
        break
    elif rep > x:
        statut = "grand"
    else:
        statut = "petit"
    print(f"ton nombre est trop {statut}")
    vie -= 1
else:
    print("Tu as perdu.")
