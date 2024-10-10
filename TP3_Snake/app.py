import random
import time

from Classes import ShortSnake, GreedyPlayer


# États (x snake,y snake,x fruit,y fruit)
# x snake,y snake -> sont les coordonnées du serpent.
# x fruit,y fruit -> sont les coordonnées du fruit (pomme).
# Boucle principale pour exécuter le jeu avec MDP
def main():
    grid_size = 5
    snake_game = ShortSnake(grid_size)
    player = GreedyPlayer(snake_game)
    
    num_episodes = 10000
    for episode in range(num_episodes):
        state = snake_game.reset()
        total_reward = 0
        done = False
        
        while not done:
            action = player.get_action(state)
            next_state, reward, done = snake_game.step(action)
            
            player.update(state, action, reward, next_state)
            
            state = next_state
            total_reward += reward

        if episode % 1000 == 0:
            print(f"Episode {episode}, Total Reward: {total_reward}, Score: {snake_game.score}")
    
    # Test the trained agent
    print("\nTesting the trained agent:")
    state = snake_game.reset()
    total_reward = 0
    done = False
    steps = 0
    while not done:
        action = player.get_action(state)
        state, reward, done = snake_game.step(action)
        total_reward += reward
        steps += 1
        if steps % 5 == 0:  # Afficher l'état du jeu toutes les 5 étapes pour ne pas surcharger la sortie
            print(snake_game)
            print(f"Step: {steps}, Action: {action}, Reward: {reward}")
    
    print(f"Game Over! Steps: {steps}, Final Score: {snake_game.score}, Total Reward: {total_reward}")

if __name__ == "__main__":
    main()