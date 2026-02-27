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
        """
        Calculate the next state based on the current state and action.
        If the next state is out of bounds, return the current state.
        """
        r, c = divmod(state, self.size)
        dr, dc = self.actions[action]
        new_r, new_c = r + dr, c + dc

        # if go off the grid, stay in the same state
        if self.states.is_out_of_bounds(new_r, new_c):
            return state
        
        return new_r * self.size + new_c

    def reward(self, state):
        """
        R = 1 if state is terminal, R=-1 otherwise
        """
        if state == self.terminal_states:
            return 1
        return -1