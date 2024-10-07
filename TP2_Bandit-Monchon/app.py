from bandit_module_carlos import Ban10, GreedyPlayer, OptimistGreedyPlayer
import matplotlib.pyplot as plt

ban10 = Ban10()
greedy_player = GreedyPlayer(10, 0.1)
optimist_greedy_player = OptimistGreedyPlayer(10, 0.1)
# rewards = []
rewards_greedy = []
rewards_optimist = []
optimal_actions_greedy = []
optimal_actions_optimist = []

for i in range(1000):
    # Get actions
    action_greedy = greedy_player.get_action()
    action_optimist = optimist_greedy_player.get_action()
    
    # Play actions on the bandit
    reward_greedy = ban10.play(action_greedy)
    reward_optimist = ban10.play(action_optimist)

    # Update rewards lists
    rewards_greedy.append(reward_greedy)
    rewards_optimist.append(reward_optimist)
    
    # Inform players of rewards
    greedy_player.reward(action_greedy, reward_greedy)
    optimist_greedy_player.reward(action_optimist, reward_optimist)

    # Check if actions are optimal
    optimal_action_greedy = action_greedy == ban10.max_avg_index()
    optimal_action_optimist = action_optimist == ban10.max_avg_index()

    optimal_actions_greedy.append(optimal_action_greedy)
    optimal_actions_optimist.append(optimal_action_optimist)

    print(f"Iteration {i+1}:")
    print(f"  Action greedy choisie : {action_greedy}")
    print(f"  Action optimist choisie : {action_optimist}")
    print(f"  Récompense obtenue par greedy : {reward_greedy}")
    print(f"  Récompense obtenue par optimist : {reward_optimist}")
    # print(f"  Choix optimal : {'Oui' if optimal_action_greedy else 'Non'}")
    print("------------------------------------------------")

# Tracer l'évolution des récompenses
# CARLOS
# plt.figure(figsize=(12, 6))
# plt.plot(rewards, label='Récompense')
# plt.xlabel('Itération')
# plt.ylabel('Récompense')
# plt.title('Évolution de la Récompense au Cours des Itérations')
# plt.legend()
# plt.grid(True)
# plt.show()

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(rewards_greedy, label='GreedyPlayer')
plt.plot(rewards_optimist, label='OptimistGreedyPlayer')
plt.xlabel('Iteration')
plt.ylabel('Reward')
plt.title('Average Rewards')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(optimal_actions_greedy, label='GreedyPlayer')
plt.plot(optimal_actions_optimist, label='OptimistGreedyPlayer')
plt.xlabel('Iteration')
plt.ylabel('Optimal Action (%)')
plt.title('Optimal Action Percentages')
plt.legend()
plt.grid(True)
plt.show()
