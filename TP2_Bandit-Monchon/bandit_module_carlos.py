import random
import matplotlib.pyplot as plt

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
