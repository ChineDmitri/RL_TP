import random
import time
import matplotlib.pyplot as plt

from Classes import ShortSnake, GreedyPlayer


# États (x snake,y snake,x fruit,y fruit)
# x snake,y snake -> sont les coordonnées du serpent.
# x fruit,y fruit -> sont les coordonnées du fruit (pomme).
# Boucle principale pour exécuter le jeu avec MDP
# def main():
#     grid_size = 5
#     snake_game = ShortSnake(grid_size)
#     player = GreedyPlayer(snake_game)
    
#     num_episodes = 10000
#     for episode in range(num_episodes):
#         state = snake_game.reset()
#         total_reward = 0
#         done = False
        
#         while not done:
#             action = player.get_action(state)
#             next_state, reward, done = snake_game.step(action)
            
#             player.update(state, action, reward, next_state)
            
#             state = next_state
#             total_reward += reward

#         if episode % 1000 == 0:
#             print(f"Episode {episode}, Total Reward: {total_reward}, Score: {snake_game.score}")
    
#     # Test the trained agent
#     print("\nTesting the trained agent:")
#     state = snake_game.reset()
#     total_reward = 0
#     done = False
#     steps = 0
#     while not done:
#         action = player.get_action(state)
#         state, reward, done = snake_game.step(action)
#         total_reward += reward
#         steps += 1
#         if steps % 5 == 0:  # Afficher l'état du jeu toutes les 5 étapes pour ne pas surcharger la sortie
#             print(snake_game)
#             print(f"Step: {steps}, Action: {action}, Reward: {reward}")
    
#     print(f"Game Over! Steps: {steps}, Final Score: {snake_game.score}, Total Reward: {total_reward}")

# if __name__ == "__main__":
#     main()

import matplotlib.pyplot as plt
import numpy as np
from Classes import ShortSnake, GreedyPlayer

def run_experiment(gamma, num_steps=1000, num_runs=10):
    rewards_per_run = []
    for _ in range(num_runs):
        snake_game = ShortSnake(grid_size=5)
        player = GreedyPlayer(snake_game, eps=0.1, alpha=0.5, gamma=gamma)

        rewards = []
        for _ in range(num_steps):
            action = player.get_action()
            _, reward, _ = snake_game.step(action)
            player.reward(action, reward)
            rewards.append(reward)
        rewards_per_run.append(rewards)
    
    avg_rewards = np.mean(rewards_per_run, axis=0)
    return avg_rewards

def main():
    gamma_values = [0, 0.1, 0.5, 0.9, 1]
    num_steps = 1000
    
    plt.figure(figsize=(12, 8))
    for gamma in gamma_values:
        avg_rewards = run_experiment(gamma, num_steps)
        plt.plot(range(num_steps), avg_rewards, label=f'γ = {gamma}')
    
    plt.xlabel("Step")
    plt.ylabel("Average Reward")
    plt.title("Reward Evolution for Different γ Values")
    plt.legend()
    plt.show()

    # Find the best gamma value
    best_gamma = max(gamma_values, key=lambda g: np.mean(run_experiment(g, num_steps)))
    print(f"The best gamma value for {num_steps} steps is: {best_gamma}")

    # Test with 10000 steps
    num_steps_long = 10000
    best_gamma_long = max(gamma_values, key=lambda g: np.mean(run_experiment(g, num_steps_long)))
    print(f"The best gamma value for {num_steps_long} steps is: {best_gamma_long}")

if __name__ == "__main__":
    main()