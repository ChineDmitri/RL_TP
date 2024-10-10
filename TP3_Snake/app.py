import random
import time

from Classes import ShortSnake, GreedyPlayer


# États (x snake,y snake,x fruit,y fruit)
# x snake,y snake -> sont les coordonnées du serpent.
# x fruit,y fruit -> sont les coordonnées du fruit (pomme).
# Boucle principale pour exécuter le jeu avec MDP
def main():
    actions = ['up', 'down', 'left', 'right']
    player = GreedyPlayer(actions)
    snake_game = ShortSnake(5)  # Supposons que cette classe existe et fonctionne comme prévu
    
    num_episodes = 1000
    for episode in range(num_episodes):
        state = snake_game.reset()
        total_reward = 0
        done = False
        
        while not done:
            action = player.get_action(tuple(state))
            next_state, reward, done = snake_game.step(action)
            
            player.update(tuple(state), action, reward, tuple(next_state))
            
            state = next_state
            total_reward += reward
        
        if episode % 100 == 0:
            print(f"Episode {episode}, Total Reward: {total_reward}")

if __name__ == "__main__":
    main()
