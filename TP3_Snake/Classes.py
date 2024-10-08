import random


class ShortSnake:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        self.snake_pos = [grid_size // 2, grid_size // 2]
        # init direction à droite
        self.snake_dir = [0, 1]  
        self.fruit_pos = self._get_random_pos()
        self.score = 0

    def _get_random_pos(self):
        return [random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)]

    def move(self, direction=None):
        if direction is not None:
            self.snake_dir = direction
        new_head = [(self.snake_pos[0] + self.snake_dir[0]) % self.grid_size,
                    (self.snake_pos[1] + self.snake_dir[1]) % self.grid_size]
        if new_head == self.fruit_pos:
            self.score += 10
            self.fruit_pos = self._get_random_pos()
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
                    grid_str += 'S '
                elif [i, j] == self.fruit_pos:
                    grid_str += 'F '
                else:
                    grid_str += '  '
            grid_str += '\n'
        grid_str += f'Score: {self.score}\n'
        return grid_str
