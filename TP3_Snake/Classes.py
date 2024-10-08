import random


class ShortSnake:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [
            [' ' for _ in range(grid_size)]
            for _ in range(grid_size)
        ]
        self.snake_pos = [grid_size // 2, grid_size // 2]
        # init direction à droite ->
        self.snake_dir = [0, 1]
        self.fruit_pos = self._get_random_fruit_pos()
        self.score = 0

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
        elif (new_head[0] < 0
              or new_head[0] >= self.grid_size
              or new_head[1] < 0
              or new_head[1] >= self.grid_size):
            self.score -= 10

        self.snake_pos = new_head

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
        grid_str += f'Score: {self.score}\n'
        return grid_str

    def get_reward(self):
        if self.snake_pos == self.fruit_pos:
            return 10  # Récompense pour avoir mangé le fruit
        elif (self.snake_pos[0] < 0 or self.snake_pos[0] >= self.grid_size or
              self.snake_pos[1] < 0 or self.snake_pos[1] >= self.grid_size):
            return -10  # Pénalité pour collision ou sortie
        else:
            return 0  # Aucune récompense si rien de spécial ne se passe

    def step(self, action):
        actions = {
            'up': [-1, 0],
            'down': [1, 0],
            'left': [0, -1],
            'right': [0, 1]
        }
        if action in actions:
            self.move(actions[action])

        state = (self.snake_pos, self.fruit_pos)
        reward = self.get_reward()
        done = reward == -10

        return state, reward, done

    def save_state(self):
        return (tuple(self.snake_pos), tuple(self.fruit_pos), tuple(self.snake_dir), self.score)

    # Nouvelle méthode pour restaurer un état sauvegardé
    def restore_state(self, state):
        self.snake_pos,
        self.fruit_pos,
        self.snake_dir,
        self.score = map(list, state)


################################################################
################################################################
################################################################


class GreedyPlayer:
    def __init__(self, actions, eps):
        """
        actions: liste des actions possibles (ex: ['up', 'down', 'left', 'right'])
        eps: taux d'exploration
        """
        self.actions = actions
        # Valeurs initiales des actions
        self.action_values = {action: 0 for action in actions}
        # Compteur d'évaluation pour chaque action
        self.eval_count = {action: 0 for action in actions}
        self.eps = eps  # Taux d'exploration

    def get_action(self):
        """
        Choisir une action soit aléatoire (exploration), soit en suivant la meilleure valeur d'action (exploitation)
        """
        rand_value = random.random()
        explore = rand_value < self.eps  # Si aléatoire est inférieur à epsilon, on explore

        if explore:
            return self._random_action()  # Choisir une action aléatoire
        else:
            # Choisir la meilleure action selon les valeurs d'actions
            return self._greedy_action()

    def _greedy_action(self):
        """
        Choisir l'action avec la meilleure valeur
        """
        max_value = max(self.action_values.values())

        # Trouver les actions ayant la valeur maximale
        best_actions = [action for action,
                        value in self.action_values.items() if value == max_value]

        # Si plusieurs actions ont la même valeur maximale, en choisir une aléatoirement
        return random.choice(best_actions)

    def _random_action(self):
        """
        Choisir une action aléatoire parmi les actions possibles
        """
        return random.choice(self.actions)

    def reward(self, action, reward):
        """
        Mettre à jour la valeur de l'action choisie avec la récompense obtenue
        action: l'action pour laquelle on reçoit la récompense
        reward: la valeur de la récompense
        """
        self.eval_count[action] += 1  # Incrémenter le nombre de fois que cette action a été choisie

        # Mise à jour de la moyenne des valeurs pour cette action
        self.action_values[action] += (reward -
                                       self.action_values[action]) / self.eval_count[action]
