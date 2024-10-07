from bandit_module_carlos import Ban10, GreedyPlayer
import matplotlib.pyplot as plt

ban10 = Ban10()
greedy_player = GreedyPlayer(10, 0.1)
rewards = []

for i in range(1000):
    # Get action
    action = greedy_player.get_action()
    
    # Action sur le ban
    reward = ban10.play(action)

    # Tableau avec les récompenses
    rewards.append(reward)
    
    # Informer le joueur de la récompense
    greedy_player.reward(action, reward)

    # Vérification si action optimale
    optimal_action = action == ban10.max_avg_index()

    print(f"Iteration {i+1}:")
    print(f"  Action choisie : {action}")
    print(f"  Récompense obtenue : {reward}")
    print(f"  Choix optimal : {'Oui' if optimal_action else 'Non'}")
    print("------------------------------------------------")

# Tracer l'évolution des récompenses
plt.figure(figsize=(12, 6))
plt.plot(rewards, label='Récompense')
plt.xlabel('Itération')
plt.ylabel('Récompense')
plt.title('Évolution de la Récompense au Cours des Itérations')
plt.legend()
plt.grid(True)
plt.show()