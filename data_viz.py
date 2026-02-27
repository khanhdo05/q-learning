class DataTracker:
    """
    Generates the two required line plots per experiment:
      1. Average Reinforcement per Episode
      2. Average Episode Duration per Episode
    Both include a horizontal line marking the theoretical optimum.
    """
    def __init__(self, exp_id, avg_rewards, avg_durations):
        self.exp_id = exp_id
        self.avg_rewards = avg_rewards  # List of average rewards per episode
        self.avg_durations = avg_durations  # List of average episode durations per episode
        
    def plot_results(self, save=True):
        # Plot 1: Average Reinforcement by Episode number
        # Plot 2: Average Episode Duration by Episode number
        pass