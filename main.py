# main.py
from constants import NUM_SIMS, E
from experiment import TestBed
from data_viz import DataTracker

# Experiment configurations
# alpha and exploration_rate can be a float OR the string '1/T' / '1/P'
EXPERIMENTS = [
    # exp_id,  gamma, alpha,  exploration_rate
    (1,        0.9,   0.1,    0.25),
    (2,        0.9,   '1/T',  '1/T'),
    (3,        0.9,   0.1,    '1/T'),
    (4,        0.9,   '1/T',  0.1),
    (5,        0.9,   0.1,    0.1),
    (6,        0.9,   '1/P',  0.1),
]

# ── Run ──────────────────────────────────────────────────────────────
for exp_id, gamma, alpha, exploration_rate in EXPERIMENTS:
    testbed = TestBed(
        exp_id           = exp_id,
        gamma            = gamma,
        alpha            = alpha,
        exploration_rate = exploration_rate,
        num_simulations  = NUM_SIMS,
        E                = E
    )

    testbed.run_experiment()

    tracker = DataTracker(
        exp_id        = exp_id,
        avg_rewards   = testbed.avg_rewards,
        avg_durations = testbed.avg_durations
    )
    tracker.plot_results(save=True)
