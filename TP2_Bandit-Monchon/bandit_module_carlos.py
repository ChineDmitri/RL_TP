import random
import matplotlib.pyplot as plt
import math

class Bandit:
    def __init__(self):
        self.avg = random.normalvariate(0, 1)

    def play(self):
        return random.normalvariate(self.avg, 1)

# =============================================================================
# Exercice 1
# =============================================================================

# # 3 instances de Bandit
# bandits = [Bandit() for _ in range(3)]

# # Jouer 1000 fois
# results = [ [bandit.play() for _ in range(1000)] for bandit in bandits ]

# plt.figure(figsize=(15, 5))

# # Tracer les histogrammes pour chaque bandit
# for i, result in enumerate(results):
#     plt.subplot(1, 3, i + 1)
#     plt.hist(result, bins=50, density=True, alpha=0.6)
#     plt.title(f'Bandit {i + 1}')
#     plt.xlabel('Valeur')
#     plt.ylabel('Fréquence')

# plt.tight_layout()  # Ajuster les sous-graphiques pour éviter le chevauchement
# plt.show()

# =============================================================================
# Exercice 2
# =============================================================================

class Ban10:
    def __init__(self):
        self.bandits = [Bandit() for _ in range(10)]
        self.bigger_avg_bandit = self.max_avg_index()

    def max_avg_index(self):
        max_avg = float('-inf')
        max_index = -1
        for i, bandit in enumerate(self.bandits):
            if bandit.avg > max_avg:
                max_avg = bandit.avg
                max_index = i
        return max_index
    
    def play(self, arms):
        if 0 <= arms < len(self.bandits):
            return self.bandits[arms].play()
        else:
            raise ValueError("Le numéro de bras doit être entre 0 et 9")
    
# =============================================================================
# Exercice 3
# =============================================================================
class GreedyPlayer():
    def __init__(self, n, eps):
        self.action_values = [0] * n
        self.eval_count = [0] * n
        self.eps = eps

    def get_action(self):
        rand_value = random.random()

        explore = rand_value < self.eps

        if explore:
            return self._random_action()
        else:
            return self._greedy_action()

    def _greedy_action(self):
        max_value = max(self.action_values)

        # Trouver l'index de la valeur maximale dans la liste
        actions = [i for i, value in enumerate(self.action_values) if value == max_value]
        # Choisie une action aléatoire si plusieures actions ont la même valeur ou choisi la seule action disponible
        return random.choice(actions)
    
    def _random_action(self):
        return random.randint(0, len(self.action_values) - 1)

    def reward(self, action, reward):
        self.eval_count[action] += 1

        # Mise à jour de la moyenne
        self.action_values[action] += (reward - self.action_values[action]) / self.eval_count[action]



# =============================================================================
# "Heritage de GreedyPlayer"
class OptimistGreedyPlayer(GreedyPlayer):
    def __init__(self, num_actions, epsilon):
        super().__init__(num_actions, epsilon)
        self.Q = [5] * num_actions

# =============================================================================
# Exercice 3
# =============================================================================
class UCBGreedyPlayer():
    def __init__(self, n, eps, c):
        self.action_values = [0] * n
        self.eval_count = [0] * n
        self.eps = eps
        self.c = c
        self.t = 0

    def get_action(self):
        rand_value = random.random()

        explore = rand_value < self.eps

        if explore:
            return self._random_action()
        else:
            return self._greedy_action()

    def _greedy_action(self):
        ucb_values = []
        for i in range(len(self.action_values)):
            if self.eval_count[i] == 0:
                ucb_values.append(float('inf'))
            else:
                # Calculer la valeur UCB
                bonus = self.c * math.sqrt(math.log(self.t + 1) / self.eval_count[i])
                ucb_values.append(self.action_values[i] + bonus)
        
        # Sélectionner l'action avec la plus grande valeur UCB
        max_value = max(ucb_values)
        best_actions = [i for i, value in enumerate(ucb_values) if value == max_value]
        
        return random.choice(best_actions)

            
    def _random_action(self):
        return random.randint(0, len(self.action_values) - 1)

    def reward(self, action, reward):
        self.eval_count[action] += 1

        # Mise à jour de la moyenne
        self.action_values[action] += (reward - self.action_values[action]) / self.eval_count[action]

# Nombre d'instances
num_players = 2000
num_iterations = 1000

# Initialiser les joueurs
epsilon = 0.1
c = 2  # Paramètre de confiance pour UCB
greedy_players = [GreedyPlayer(10, epsilon) for _ in range(num_players)]
ucb_players = [UCBGreedyPlayer(10, 0, c) for _ in range(num_players)]
ban10 = Ban10()

# Stocker les récompenses et pourcentage d'optimalité
greedy_rewards = []
ucb_rewards = []
optimality_greedy = []
optimality_ucb = []

for t in range(num_iterations):
    greedy_reward_sum = 0
    ucb_reward_sum = 0
    greedy_optimal_count = 0
    ucb_optimal_count = 0
    
    for player in greedy_players:
        action = player.get_action()
        reward = ban10.play(action)
        player.reward(action, reward)
        greedy_reward_sum += reward
        # Vérifier si l'action est optimale
        if action == ban10.bigger_avg_bandit:
            greedy_optimal_count += 1
            
    for player in ucb_players:
        action = player.get_action()
        reward = ban10.play(action)
        player.reward(action, reward)
        ucb_reward_sum += reward
        # Vérifier si l'action est optimale
        if action == ban10.bigger_avg_bandit:
            ucb_optimal_count += 1

    # Stocker les résultats
    greedy_rewards.append(greedy_reward_sum / num_players)
    ucb_rewards.append(ucb_reward_sum / num_players)
    optimality_greedy.append(greedy_optimal_count / num_players)
    optimality_ucb.append(ucb_optimal_count / num_players)

# Tracer les courbes
plt.figure(figsize=(12, 6))

# Courbes des moyennes des récompenses
plt.subplot(2, 1, 1)
plt.plot(greedy_rewards, label='GreedyPlayer (ε=0.1)', color='blue')
plt.plot(ucb_rewards, label='UCBGreedyPlayer', color='orange')
plt.title('Moyenne des récompenses')
plt.xlabel('Itérations')
plt.ylabel('Récompense moyenne')
plt.legend()

# Courbes du pourcentage d'optimalité
plt.subplot(2, 1, 2)
plt.plot(optimality_greedy, label='GreedyPlayer (ε=0.1)', color='blue')
plt.plot(optimality_ucb, label='UCBGreedyPlayer', color='orange')
plt.title('Pourcentage d\'optimalité')
plt.xlabel('Itérations')
plt.ylabel('Pourcentage optimal')
plt.legend()

plt.tight_layout()
plt.show()