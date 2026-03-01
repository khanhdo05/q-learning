import numpy as np
from environment import GridWorld

class QLearningAgent:
    """
    A Q-learning agent that learns to navigate the environment.

    q-table is initialized to zeros and has dimensions (num_states, num_actions) by the method reset().
        - rows represent states
        - columns represent actions
        - each entry is a q-value for the state-action pair
    
    gamme: discount factor - how much future awards are valued
    alpha: learning rate - how much new info overrides old info
    epsilon: exploration rate - probability of taking a random action
    """
    def __init__(self, env: GridWorld, gamma: str | float, alpha: str | float, epsilon: float, random_seed):
        self.env = env
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.random_seed = random_seed

        self.reset()
    
    def reset(self):
        self.q_table = np.zeros((self.env.num_states, 4))  # 4 actions: up, down, left, right

    def _resolve_para(self, para, T, P):
        """
        Turn a paramter into a concrete float.
        It can already by a float or the string '1/T' or '1/P'
        """
        if isinstance(para, float) or isinstance(para, int):
            return float(para)
        
        if para == '1/T':
            return 1.0 / T
        
        if para == '1/P':
            return 1.0 / P
        
        raise ValueError(f"Invalid parameter: {para}")
    
    def choose_action(self, state):
        """
        The agent selects an action using the epsilon-greedy policy:
            - With probability epsilon, it chooses a random action (exploration).
            - With probability 1 - epsilon, it chooses the action with the highest Q-value.
        """
        if np.random.rand() < self.epsilon:
            # explore
            return np.random.randint(4)  
        
        # else exploit
        return np.argmax(self.q_table[state])
    
    def learn(self, state, action, reward, next_state):
        pass
        