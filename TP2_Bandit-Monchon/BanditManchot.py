from Game import BanditManchot

jeu = BanditManchot(balance=100)

print("start")

# Boucle de jeu
while jeu.get_balance() > 0:
    input("Appuyez sur Entrée pour faire tourner la machine...")
    jeu.spin()

print("Votre solde est épuisé. Fin du jeu.")