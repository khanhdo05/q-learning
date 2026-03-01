import numpy as np
from environment import Environment

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
    def __init__(self, env: Environment, gamma, alpha, epsilon):
        self.env = env
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon

        self.reset()
    
    def reset(self):
        self.q_table = np.zeros((self.env.num_states, 4))  # 4 actions: up, down, left, right

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(4)  # Explore: choose a random action
        return np.argmax(self.q_table[state])  # Exploit: choose the best action
    
    def learn(self, state, action, reward, next_state):
        """
        At each step, the agent:
            1. Chooses an action.
            2. Moves to the next state based on that action.
            3. Updates the Q-value for the state-action pair using the Bellman formula.
            4. Ends the episode if it reaches a terminal state, otherwise continues to the next step.
        """
        action = self.choose_action(state)
        reward = self.env.step(action)
        next_state = self.env.get_state()
        self.q_table[state, action] += self.alpha * (reward + self.gamma * np.max(self.q_table[next_state]) - self.q_table[state, action])
        state = next_state