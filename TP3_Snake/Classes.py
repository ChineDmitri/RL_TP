import random


import random

class ShortSnake:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.reset()

    def reset(self):
        self.grid = [
            [' ' for _ in range(self.grid_size)]
            for _ in range(self.grid_size)
        ]
        self.snake_pos = [self.grid_size // 2, self.grid_size // 2]
        self.snake_dir = [0, 1]  # init direction à droite ->
        self.fruit_pos = self._get_random_fruit_pos()
        self.score = 0
        self.steps_without_fruit = 0
        self.max_steps_without_fruit = self.grid_size * 2  # Limite de pas sans manger de fruit
        return self.get_state()

    def _get_random_fruit_pos(self):
        return [random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)]

    def move(self, direction=None):
        if direction is not None:
            self.snake_dir = direction
        new_head = [
            (self.snake_pos[0] + self.snake_dir[0]) % self.grid_size,
            (self.snake_pos[1] + self.snake_dir[1]) % self.grid_size
        ]
        if new_head == self.fruit_pos:
            self.score += 10
            self.fruit_pos = self._get_random_fruit_pos()
            self.steps_without_fruit = 0
        else:
            self.steps_without_fruit += 1

        self.snake_pos = new_head

    def step(self, action):
        actions = {
            'up': [-1, 0],
            'down': [1, 0],
            'left': [0, -1],
            'right': [0, 1]
        }
        if action in actions:
            self.move(actions[action])

        state = self.get_state()
        reward = self.get_reward()
        done = self.is_game_over()

        return state, reward, done

    def get_reward(self):
        if self.snake_pos == self.fruit_pos:
            return 10  # Récompense pour avoir mangé le fruit
        elif self.is_game_over():
            return -10  # Pénalité pour fin de jeu
        else:
            return -1  # Petite pénalité pour encourager à trouver le fruit rapidement

    def is_game_over(self):
        # Le jeu est terminé si le serpent sort de la grille ou s'il n'a pas mangé de fruit depuis trop longtemps
        return (self.snake_pos[0] < 0 or self.snake_pos[0] >= self.grid_size or
                self.snake_pos[1] < 0 or self.snake_pos[1] >= self.grid_size or
                self.steps_without_fruit >= self.max_steps_without_fruit)

    def get_state(self):
        return (tuple(self.snake_pos), tuple(self.fruit_pos))

    def __str__(self):
        grid_str = ''
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if [i, j] == self.snake_pos:
                    grid_str += '🐍 '
                elif [i, j] == self.fruit_pos:
                    grid_str += '🍏 '
                else:
                    grid_str += ' . '
            grid_str += '\n'
        grid_str += f'Score: {self.score}, Steps without fruit: {self.steps_without_fruit}\n'
        return grid_str
    

# class ShortSnake:
#     def __init__(self, grid_size):
#         self.grid_size = grid_size
#         self.grid = [
#             [' ' for _ in range(grid_size)]
#             for _ in range(grid_size)
#         ]
#         self.snake_pos = [grid_size // 2, grid_size // 2]
#         # init direction à droite ->
#         self.snake_dir = [0, 1]
#         self.fruit_pos = self._get_random_fruit_pos()
#         self.score = 0

#     def _get_random_fruit_pos(self):
#         return [random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)]

#     def move(self, direction=None):
#         if direction is not None:
#             self.snake_dir = direction
#         new_head = [
#             (self.snake_pos[0] + self.snake_dir[0]) % self.grid_size,
#             (self.snake_pos[1] + self.snake_dir[1]) % self.grid_size
#         ]
#         if new_head == self.fruit_pos:
#             self.score += 10
#             self.fruit_pos = self._get_random_fruit_pos()
#         elif (new_head[0] < 0
#               or new_head[0] >= self.grid_size
#               or new_head[1] < 0
#               or new_head[1] >= self.grid_size):
#             self.score -= 10

#         self.snake_pos = new_head

#     def __str__(self):
#         grid_str = ''
#         for i in range(self.grid_size):
#             for j in range(self.grid_size):
#                 if [i, j] == self.snake_pos:
#                     grid_str += '🐍 '
#                 elif [i, j] == self.fruit_pos:
#                     grid_str += '🍏 '
#                 else:
#                     grid_str += ' . '
#             grid_str += '\n'
#         grid_str += f'Score: {self.score}\n'
#         return grid_str

#     def get_reward(self):
#         if self.snake_pos == self.fruit_pos:
#             return 10  # Récompense pour avoir mangé le fruit
#         elif (self.snake_pos[0] < 0 or self.snake_pos[0] >= self.grid_size or
#               self.snake_pos[1] < 0 or self.snake_pos[1] >= self.grid_size):
#             return -10  # Pénalité pour collision ou sortie
#         else:
#             return 0  # Aucune récompense si rien de spécial ne se passe

#     def step(self, action):
#         actions = {
#             'up': [-1, 0],
#             'down': [1, 0],
#             'left': [0, -1],
#             'right': [0, 1]
#         }
#         if action in actions:
#             self.move(actions[action])

#         state = (self.snake_pos, self.fruit_pos)
#         reward = self.get_reward()
#         done = reward == -10

#         return state, reward, done

#     def save_state(self):
#         return (tuple(self.snake_pos), tuple(self.fruit_pos), tuple(self.snake_dir), self.score)

#     def get_state(self):
#         return (tuple(self.snake_pos), tuple(self.fruit_pos))

#     def restore_state(self, state):
#         self.snake_pos, self.fruit_pos, self.snake_dir, self.score = map(list, state[:3]) + [state[3]]

#     def reset(self):
#         self.grid = [
#             [' ' for _ in range(self.grid_size)]
#             for _ in range(self.grid_size)
#         ]
#         self.snake_pos = [self.grid_size // 2, self.grid_size // 2]
#         self.snake_dir = [0, 1]  # init direction à droite ->
#         self.fruit_pos = self._get_random_fruit_pos()
#         self.score = 0
#         return self.get_state()  # Retourne l'état initial


################################################################
################################################################
################################################################


# class GreedyPlayer:
#     def __init__(self, actions, eps=0.1, alpha=0.1, gamma=0.9):
#         """
#         actions: liste des actions possibles (ex: ['up', 'down', 'left', 'right'])
#         eps: taux d'exploration
#         alpha: taux d'apprentissage
#         gamma: facteur de réduction pour les récompenses futures
#         """
#         self.actions = actions
#         self.eps = eps
#         self.alpha = alpha
#         self.gamma = gamma
#         self.q_values = {}  # Table Q pour stocker les valeurs d'état-action

#     def get_action(self, state):
#         """
#         Choisir une action basée sur l'état actuel
#         """
#         if random.random() < self.eps:
#             return self._random_action()
#         else:
#             return self._greedy_action(state)

#     def _greedy_action(self, state):
#         """
#         Choisir l'action avec la meilleure valeur Q pour l'état donné
#         """
#         if state not in self.q_values:
#             return self._random_action()
        
#         q_values = self.q_values[state]
#         max_q = max(q_values.values())
#         best_actions = [action for action, value in q_values.items() if value == max_q]
#         return random.choice(best_actions)

#     def _random_action(self):
#         """
#         Choisir une action aléatoire
#         """
#         return random.choice(self.actions)

#     def update(self, state, action, reward, next_state):
#         """
#         Mettre à jour la valeur Q pour un couple état-action
#         """
#         if state not in self.q_values:
#             self.q_values[state] = {a: 0 for a in self.actions}
        
#         if next_state not in self.q_values:
#             self.q_values[next_state] = {a: 0 for a in self.actions}
        
#         current_q = self.q_values[state][action]
#         max_next_q = max(self.q_values[next_state].values())
        
#         new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
#         self.q_values[state][action] = new_q

class GreedyPlayer:
    def __init__(self, snake_game, eps=0.1, alpha=0.1, gamma=0.5):
        """
        snake_game: instance de ShortSnake
        eps: taux d'exploration
        alpha: taux d'apprentissage
        gamma: facteur d'actualisation
        """
        self.snake_game = snake_game
        self.actions = ['up', 'down', 'left', 'right']
        self.eps = eps
        self.alpha = alpha
        self.gamma = gamma
        self.q_values = {}  # Table Q pour stocker les valeurs d'état-action

    def get_action(self, state):
        """
        Choisir une action basée sur l'état actuel
        """
        if random.random() < self.eps:
            return self._random_action()
        else:
            return self._greedy_action(state)

    def _greedy_action(self, state):
        """
        Choisir l'action avec la meilleure valeur Q pour l'état donné
        """
        state_key = self._get_state_key(state)
        if state_key not in self.q_values:
            return self._random_action()
        
        q_values = self.q_values[state_key]
        max_q = max(q_values.values())
        best_actions = [action for action, value in q_values.items() if value == max_q]
        return random.choice(best_actions)

    def _random_action(self):
        """
        Choisir une action aléatoire
        """
        return random.choice(self.actions)

    def update(self, state, action, reward, next_state):
        """
        Mettre à jour la valeur Q pour un couple état-action selon la formule du Q-Learning
        """
        state_key = self._get_state_key(state)
        next_state_key = self._get_state_key(next_state)

        if state_key not in self.q_values:
            self.q_values[state_key] = {a: 0 for a in self.actions}
        
        if next_state_key not in self.q_values:
            self.q_values[next_state_key] = {a: 0 for a in self.actions}
        
        current_q = self.q_values[state_key][action]
        max_next_q = max(self.q_values[next_state_key].values())
        
        new_q = current_q + self.alpha * (reward + self.gamma * max_next_q - current_q)
        self.q_values[state_key][action] = new_q

    def _get_state_key(self, state):
        """
        Convertir l'état en une clé hashable pour la table Q
        """
        return (tuple(state[0]), tuple(state[1]))
