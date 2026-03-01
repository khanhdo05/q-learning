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

        self.total_rewards = np.zeros((num_simulations, E))  # total rewards for each episode in each simulation
        self.total_durations = np.zeros((num_simulations, E))  # total durations (number of steps) for each episode in each simulation

    def _run_simulation(self, agent: QLearningAgent):
        """
        Run a single simulation of E episodes, where the agent interacts with the environment and learns from it.

        At each step, the agent:
            1. Chooses an action.
            2. Moves to the next state based on that action.
            3. Updates the Q-value for the state-action pair using the Bellman formula.
            4. Ends the episode if it reaches a terminal state, otherwise continues to the next step.

        Returns two arrays of length E:
            - episode_rewards: total reward obtained in each episode
            - episode_durations: total number of steps taken in each episode
        """
        # for each ep, track total reward and duration (number of steps)
        episode_rewards   = np.zeros(self.E)
        episode_durations = np.zeros(self.E)

        # global clock to count total iterations within a simulation
        T = 1  

        for i in range(self.E):
            P = 1  # episode clock to count iterations within the current episode

            # make sure to reset env for independent episodes, but not the agent's Q-values
            state = self.env.reset()
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

            episode_rewards[i] = total_reward
            episode_durations[i] = steps
        
        return episode_rewards, episode_durations

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
            
            rwds, durs = self._run_simulation(agent)
            self.total_rewards[i] = rwds
            self.total_durations[i] = durs
        
        # average rewards and durations across simulations
        # save as attributes for data visualization
        self.avg_rewards = np.mean(self.total_rewards, axis=0)
        self.avg_durations = np.mean(self.total_durations, axis=0)
        