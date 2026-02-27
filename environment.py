import enum

class Action(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class GridWorld:
    """
    The environment is:
        - A 4x4 grid (16 states) indexed 0-15:
            0  1  2  3
            4  5  6  7
            8  9  10 11
            12 13 14 15
        - State 0 and 15 are terminal states with reward R = 1
        - All other states have reward R = -1
        - State 12 is the initial state
    """
    def __init__(self, size = 4):
        self.size = size
        self.num_states = size * size  # square grid
        self.initial_state = 12
        self.terminal_states = {0, 15}

    def _row_col(self, state: int):
        """
        Convert flat state index → (row, col).
        """
        return divmod(state, self.size)
    
    def is_terminal(self, state: int):
        """
        Check if a state is terminal.
        """
        return state in self.terminal_states
    
    def reset(self):
        """
        Resets the environment to the initial state.
        """
        return self.initial_state
    
    def step(self, state: int, action: Action):
        """
        Calculate the next state based on the current state and action.
        If the next state is out of bounds, return the current state.

        Returns next_state, reward
        """
        if self.is_terminal(state):
            return state, 0

        # calculate next state
        r, c = self._row_col(state)
        if action == Action.UP:
            r -= 1
        elif action == Action.DOWN:
            r += 1
        elif action == Action.LEFT:
            c -= 1
        elif action == Action.RIGHT:
            c += 1
        else:
            raise ValueError("Invalid action")

        # stay in place if out of grid
        if not (0 <= r < self.size and 0 <= c < self.size):
            next_state = state 
        else:
            next_state = self._state(r, c)

        return next_state, self.reward(next_state)

    def reward(self, state: int):
        """
        Returns the reward for a given state.
        1 if state is terminal, -1 otherwise
        """
        if self.is_terminal(state):
            return 1
        return -1