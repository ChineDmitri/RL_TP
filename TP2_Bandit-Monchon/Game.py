import random

class BanditManchot:
    def __init__(self, balance):
        self.balance = balance
        self.reels = ['🍒', '🍋', '🍊', '🍉', '⭐', '💎']

    def spin(self):
        if self.balance <= 0:
          print("Solde insuffisant. Vous ne pouvez pas jouer.")
          return

        # Déduire le coût du tour (par exemple, 10 unités)
        self.balance -= 10
        print(f"Vous avez parié 10 unités. Solde restant: {self.balance}")

        # Faire tourner les 3 rouleaux
        result = [random.choice(self.reels) for _ in range(3)]

        # Afficher les résultats
        print(f"Résultat du tirage: {result[0]} | {result[1]} | {result[2]}")

        # Calculer les gains
        self.calculate_win(result)

    def calculate_win(self, result):
        if result[0] == result[1] == result[2]:
            if result[0] == '💎':
                winnings = 100  # Jackpot
            elif result[0] == '⭐':
                winnings = 50  # Second grand prix
            else:
                winnings = 20  # Prix ordinaire
            print(f"Vous avez gagné {winnings} unités!")
            self.balance += winnings
        else:
            print("Désolé, vous n'avez pas gagné cette fois.")

    def get_balance(self):
        return self.balance