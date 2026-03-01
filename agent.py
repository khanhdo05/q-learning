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
    def __init__(self, env: GridWorld, gamma: str | float, alpha: str | float, epsilon: float):
        self.env = env
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon

        self.reset()
    
    def reset(self):
        self.q_table = np.zeros((self.env.num_states, 4))  # 4 actions: up, down, left, right

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
        """
        At each step, the agent:
            1. Chooses an action.
            2. Moves to the next state based on that action.
            3. Updates the Q-value for the state-action pair using the Bellman formula.
            4. Ends the episode if it reaches a terminal state, otherwise continues to the next step.
        """
        