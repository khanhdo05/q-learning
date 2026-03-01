import numpy as np
from constants import NUM_SIMS, E
from environment import GridWorld
from agent import QLearningAgent

class TestBed:
    """
    A test bed for evaluating the performance of the Q-learning agent.
    """
    def __init__(self, exp_id: int, gamma, alpha, epsilon, num_simulations=NUM_SIMS, E=E, seed=31):
        self.exp_id = exp_id
        self.gamma = gamma
        self.alpha = alpha
        self.epsilon = epsilon
        self.num_simulations = num_simulations
        self.E = E  # Number of episodes per simulation
        self.seed = seed

        self.env = GridWorld()

    def _run_simulation(self, agent: QLearningAgent):
        """
        Run a single simulation of E episodes, where the agent interacts with the environment and learns from it.

        At each step, the agent:
            1. Chooses an action.
            2. Moves to the next state based on that action.
            3. Updates the Q-value for the state-action pair using the Bellman formula.
            4. Ends the episode if it reaches a terminal state, otherwise continues to the next step.
        """
        T = 1  # global clock to count total iterations within a simulation

        for _ in range(self.E):
            P = 1  # episode clock to count iterations within the current episode

            # make sure to reset env for independent episodes, but not the agent's Q-values
            total_reward = 0
            steps = 0

            while not self.env.is_terminal(state):
                action = agent.choose_action(state, T, P)
                next_state, reward = self.env.step(state, action)
                agent.learn(state, action, reward, next_state, T, P)

                state = next_state
                total_reward += reward
                steps += 1
                T += 1
                P += 1

    def run_experiment(self):
        """
        A loop that runs `num_simulations` simulations, where each simulation consists of 
        running `run_simulation()`, then resetting the environment and agent for the next simulation.
        """
        for i in range(self.num_simulations):
            # independent random seed for each simulation to ensure variability
            rng = np.random.default_rng(self.seed + i)

            # initialize environment and agent for this simulation
            agent = QLearningAgent(
                num_states=self.env.num_states,
                num_actions=self.env.num_actions,
                gamma=self.gamma,
                alpha=self.alpha,
                epsilon=self.epsilon,
                random_seed=rng
            )
            
            self._run_simulation(agent)