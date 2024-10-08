import random
import time

from Classes import ShortSnake


# États (x snake,y snake,x fruit,y fruit)
# x snake,y snake -> sont les coordonnées du serpent.
# x fruit,y fruit -> sont les coordonnées du fruit (pomme).
# Boucle principale pour exécuter le jeu avec MDP
def main():
    mdp_snake = ShortSnake(5)  # Grille de taille 5x5

    # Actions possibles
    actions = ['up', 'down', 'left', 'right']

    while True:
        print(mdp_snake)
        # Choisir une action aléatoire ou manuelle
        action = random.choice(actions)  # Action aléatoire
        state, reward, done = mdp_snake.step(action)  # Appliquer l'action et obtenir le nouvel état

        print(f'Action: {action}, Reward: {reward}, State: {state}\n')
        time.sleep(0.1)  # Pause de 0.5 secondes entre chaque tour
        if done:
            print("Game Over!")
            break

if __name__ == "__main__":
    main()