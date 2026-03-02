import enum

Action = {
    0: 'UP',
    1: 'DOWN',
    2: 'LEFT',
    3: 'RIGHT'
}

NUM_SIMS = 10000
E = 80
GRID_SIZE = 4
NUM_STATES = GRID_SIZE * GRID_SIZE
INITIAL_STATE = 12
TERMINAL_STATES = {0, 15}