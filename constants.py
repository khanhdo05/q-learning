import enum

class Action(enum.Enum):
    0 = 0  # UP
    1 = 1  # DOWN
    2 = 2  # LEFT
    3 = 3  # RIGHT

NUM_SIMS = 10000
E = 500
GRID_SIZE = 4
NUM_STATES = GRID_SIZE * GRID_SIZE
INITIAL_STATE = 12
TERMINAL_STATES = {0, 15}