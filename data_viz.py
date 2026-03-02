import matplotlib.pyplot as plt
import numpy as np

class DataTracker:
    """
    Generates the two required line plots per experiment:
      1. Average Reinforcement per Episode
      2. Average Episode Duration per Episode
    Both include a horizontal line marking the theoretical optimum.
    """
    # To S=15: 12->13->14->15 (3 steps, rewards = -1 -1 +1 = -1)
    # To S=0: 12->8->4->0 (3 steps, rewards = -1 -1 +1 = -1)
    OPTIMAL_REWARD   = -1   # sum of rewards on shortest path
    OPTIMAL_DURATION =  3   # minimum steps to reach terminal

    def __init__(self, exp_id, avg_rewards, avg_durations):
        self.exp_id = exp_id
        self.avg_rewards = avg_rewards 
        self.avg_durations = avg_durations 

        # episodes are just 1 to E, where E is the number of episodes per simulation
        self.episodes = np.arange(1, len(avg_rewards) + 1)
        
    def plot_results(self, save=True):
        # create a figure with 2 subplots side by side
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        fig.suptitle(f"Experiment {self.exp_id}", fontsize=14, fontweight='bold')

        # plot 1: average reinforcement per episode
        ax = axes[0]  # first subplot

        # x-axis: episode number, y-axis: average reinforcement (reward)
        ax.plot(self.episodes, self.avg_rewards, color='steelblue',
                linewidth=1.2, label='Avg Reinforcement')
        
        ax.axhline(y=self.OPTIMAL_REWARD, color='red', linestyle='--',
                   linewidth=1.5, label=f'Optimal = {self.OPTIMAL_REWARD}')
        ax.set_xlabel('Episode Number')
        ax.set_ylabel('Average Reinforcement')
        ax.set_title('Average Reinforcement per Episode')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # plot 2: average episode duration per episode
        ax = axes[1]  # second subplot

        # x-axis: episode number, y-axis: average episode duration (number of steps)
        ax.plot(self.episodes, self.avg_durations, color='darkorange',
                linewidth=1.2, label='Avg Duration')
        
        ax.axhline(y=self.OPTIMAL_DURATION, color='red', linestyle='--',
                   linewidth=1.5, label=f'Optimal = {self.OPTIMAL_DURATION} steps')
        ax.set_xlabel('Episode Number')
        ax.set_ylabel('Average Episode Duration (steps)')
        ax.set_title('Average Episode Duration per Episode')
        ax.legend()
        ax.grid(True, alpha=0.3)

        plt.tight_layout()

        if save:
            fname = f"exp_{self.exp_id}_results.png"
            plt.savefig(fname, dpi=150)
            print(f"Saved {fname}")
        plt.show()