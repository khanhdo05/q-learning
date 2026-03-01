import numpy as np
from constants import Action

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
    def __init__(self, num_states: int, num_actions: int, gamma: float, alpha: str | float, epsilon: str | float, random_seed: np.random.Generator):
        self.num_states = num_states
        self.num_actions = num_actions
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.rng = random_seed

        self.reset()
    
    def reset(self):
        self.q_table = np.zeros((self.num_states, self.num_actions))

    def _resolve_para(self, para: float | str, T: int, P: int) -> float:
        """
        Turn a paramter (alpha and epsilon) into a concrete float.
        It can already by a float or the string '1/T' or '1/P'
        """
        if isinstance(para, float) or isinstance(para, int):
            return float(para)
        
        if para == '1/T':
            return 1.0 / T
        
        if para == '1/P':
            return 1.0 / P
        
        raise ValueError(f"Invalid parameter: {para}")
    
    def choose_action(self, state: int, T: int, P: int) -> int:
        """
        The agent selects an action using the epsilon-greedy policy:
            - With probability epsilon, it chooses a random action (exploration).
            - With probability 1 - epsilon, it chooses the action with the highest Q-value.
        """
        epsilon = self._resolve_para(self.epsilon, T, P)
        if self.rng.random() < epsilon:
            # explore: choose a random action
            return self.rng.integers(0, len(Action))  
        
        # else exploit: choose the action with the highest Q-value
        return np.argmax(self.q_table[state])
    
    def learn(self, state: int, action: int, reward: float, next_state: int, T: int, P: int):
        """
        Bellman equation for Q-learning:
        Q(state, action) = Q(state, action) + alpha * (reward + gamma * max(Q(next_state)) - Q(state, action))
        """
        alpha = self._resolve_para(self.alpha, T, P)