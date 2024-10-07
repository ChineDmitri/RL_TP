from bandit_module_carlos import Ban10, GreedyPlayer, OptimistGreedyPlayer
import matplotlib.pyplot as plt

# ban10 = Ban10()
# greedy_player = GreedyPlayer(10, 0.1)
# rewards = []

# # EXERCICE 4 QUESTION 1
# for i in range(1000):
#     # Get action
#     action = greedy_player.get_action()
    
#     # Action sur le ban
#     reward = ban10.play(action)

#     # Tableau avec les récompenses
#     rewards.append(reward)
    
#     # Informer le joueur de la récompense
#     greedy_player.reward(action, reward)

#     # Vérification si action optimale
#     optimal_action = action == ban10.max_avg_index()

#     print(f"Iteration {i+1}:")
#     print(f"  Action choisie : {action}")
#     print(f"  Récompense obtenue : {reward}")
#     print(f"  Choix optimal : {'Oui' if optimal_action else 'Non'}")
#     print("------------------------------------------------")

# # Tracer l'évolution des récompenses
# plt.figure(figsize=(12, 6))
# plt.plot(rewards, label='Récompense')
# plt.xlabel('Itération')
# plt.ylabel('Récompense')
# plt.title('Évolution de la Récompense au Cours des Itérations')
# plt.legend()
# plt.grid(True)
# plt.show()


# EXERCICE 4 QUESTION 2 à 4
# ban10 = Ban10()
# greedy_player = GreedyPlayer(10, 0.1)
# rewards = []
# optimal_action = []

# players = 2000
# actions = 10
# eps = 0.1
# iterations = 1000

# ban10_list = [Ban10() for _ in range(players)]
# greedy_players = [GreedyPlayer(actions, eps) for _ in range(players)]

# for iteration in range(iterations):
#     iteration_reward = []
#     optimal_action_count = 0

#     for i in range(players):
#         action = greedy_players[i].get_action()
#         reward = ban10_list[i].play(action)
#         greedy_players[i].reward(action, reward)
#         iteration_reward.append(reward)
    
#     if action == ban10_list[i].bigger_avg_bandit:
#             optimal_action_count += 1
    
#     # Calculer la récompense moyenne pour cette itération
#     avg_reward = sum(iteration_reward) / players
#     rewards.append(avg_reward)

#     # Calculer le pourcentage de choix optimal pour cette itération
#     optimal_percentage = (optimal_action_count / players) * 100
#     optimal_action.append(optimal_percentage)

#     print(f"Iteration {iteration+1}: Récompense moyenne : {avg_reward}")

# # Tracer l'évolution des récompenses moyennes
# plt.figure(figsize=(12, 6))
# plt.subplot(2, 1, 1)
# plt.plot(rewards, label='Récompense moyenne')
# plt.xlabel('Itération')
# plt.ylabel('Récompense moyenne')
# plt.title('Évolution de la Récompense Moyenne sur 2000 GreedyPlayers')
# plt.legend()
# plt.grid(True)

# # Tracer l'évolution du pourcentage de choix optimal
# plt.subplot(2, 1, 2)
# plt.plot(optimal_action, label='Pourcentage de choix optimal', color='orange')
# plt.xlabel('Itération')
# plt.ylabel('Pourcentage de choix optimal (%)')
# plt.title('Évolution du Pourcentage de Choix Optimal sur 2000 GreedyPlayers')
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()

# EXERCICE 4 QUESTION 5
ban10 = Ban10()
greedy_player = GreedyPlayer(10, 0.1)
rewards = []
optimal_action = []

players = 2000
actions = 10
eps_values = [0, 0.01, 0.1]
iterations = 1000

def play_greedy_players(eps):
    ban10_list = [Ban10() for _ in range(players)]
    greedy_players = [GreedyPlayer(actions, eps) for _ in range(players)]

    rewards = []
    optimal_action = []

    for iteration in range(iterations):
        iteration_reward = []
        optimal_action_count = 0

        for i in range(players):
            action = greedy_players[i].get_action()
            reward = ban10_list[i].play(action)
            greedy_players[i].reward(action, reward)
            iteration_reward.append(reward)
    
        if action == ban10_list[i].bigger_avg_bandit:
                optimal_action_count += 1
    
        # Calculer la récompense moyenne pour cette itération
        avg_reward = sum(iteration_reward) / players
        rewards.append(avg_reward)

        # Calculer le pourcentage de choix optimal pour cette itération
        optimal_percentage = (optimal_action_count / players) * 100
        optimal_action.append(optimal_percentage)

        print(f"Iteration {iteration+1}: Récompense moyenne : {avg_reward}")
    
    return rewards, optimal_action

# Stocker les résultats pour chaque epsilon
results = {eps: play_greedy_players(eps) for eps in eps_values}

plt.figure(figsize=(12, 8))

# Sous-graphique 1 : Récompenses moyennes
plt.subplot(2, 1, 1)
for eps in eps_values:
    plt.plot(results[eps][0], label=f'eps = {eps}')
plt.xlabel('Itération')
plt.ylabel('Récompense moyenne')
plt.title('Évolution des Récompenses Moyennes pour différentes valeurs de eps')
plt.legend()
plt.grid(True)

# Sous-graphique 2 : Pourcentage de choix optimal
plt.subplot(2, 1, 2)
for eps in eps_values:
    plt.plot(results[eps][1], label=f'eps = {eps}')
plt.xlabel('Itération')
plt.ylabel('Pourcentage de choix optimal (%)')
plt.title('Évolution du Pourcentage de Choix Optimal pour différentes valeurs de eps')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()