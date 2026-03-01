# main.py
from constants import NUM_SIMS, E
from experiment import TestBed
from data_viz import DataTracker

# Experiment configurations
# alpha and epsilon can be a float OR the string '1/T' / '1/P'
EXPERIMENTS = [
    # exp_id,  gamma, alpha,  epsilon
    (1,        0.9,   0.1,    0.25),
    (2,        0.9,   '1/T',  '1/T'),
    (3,        0.9,   0.1,    '1/T'),
    (4,        0.9,   '1/T',  0.1),
    (5,        0.9,   0.1,    0.1),
    (6,        0.9,   '1/P',  0.1),
]

# Run each experiment and generate the required plots
for exp_id, gamma, alpha, epsilon in EXPERIMENTS:
    testbed = TestBed(
        exp_id           = exp_id,
        gamma            = gamma,
        alpha            = alpha,
        epsilon          = epsilon,
        num_simulations  = NUM_SIMS,
        E                = E,
        seed             = 31  # just a favorite number for reproducibility :P
    )

    testbed.run_experiment()

    tracker = DataTracker(
        exp_id        = exp_id,
        avg_rewards   = testbed.avg_rewards,
        avg_durations = testbed.avg_durations
    )

    tracker.plot_results(save=True)
