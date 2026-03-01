import enum

class Action(enum.Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

NUM_SIMS = 10000
E = 500
GRID_SIZE = 4
NUM_STATES = GRID_SIZE * GRID_SIZE
INITIAL_STATE = 12
TERMINAL_STATES = {0, 15}