from grid import Grid

class GridWorld:
    def __init__(self, size = 4):
        self.size = size
        self.states = Grid(size, size, 0)
        self.initial_state = 12
        self.terminal_states = 0
        self.actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def reset(self):
        self.states = Grid(self.size, self.size, 0)
        return self.initial_state
    
    def step(self, state, action):
        pass

    def apply_action(self, state, action):
        pass

    def reward(self, state):
        if state == self.terminal_states:
            return 1
        return 0