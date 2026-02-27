from constants import NUM_SIMS, E
from agent import QLearningAgent
from environment import GridWorld

class TestBed:
    def __init__(self, exp_id: int, agent: QLearningAgent, env: GridWorld, num_simulations=NUM_SIMS, E=E):
        self.exp_id = exp_id
        self.agent = agent
        self.env = env
        self.num_simulations = num_simulations
        self.E = E  # The consistent number of episodes sufficient for convergence

    def _run_simulation(self):
        """
        Executes E episodes in sequence without restarting Q-values.
        """
        pass

    def run_experiment(self):
        """
        A loop that runs `num_simulations` simulations, where each simulation consists of 
        running `run_simulation()`, then resetting the environment and agent for the next simulation.
        """
        for _ in range(self.num_simulations):
            self._run_simulation()
            self.env.reset()
            self.agent.reset()