import numpy as np
from environment import Environment

class QLearningAgent:
    """
    A Q-learning agent that learns to navigate the environment.
    """
    def __init__(self, env: Environment, alpha=0.1, gamma=0.9):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma

        self.reset()
    
    def reset(self):
        self.q_table = np.zeros((self.env.num_states, 4))  # 4 actions: up, down, left, right

    def choose_action(self, state):
        return np.argmax(self.q_table[state])
    
    def learn(self, state, action, reward, next_state):
        pass