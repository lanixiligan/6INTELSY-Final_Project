import numpy as np
import matplotlib.pyplot as plt
import os

class BottleRLAgent:
    def __init__(self):
        self.threshold = 0.5
        self.history = []

    def compute_reward(self, y_true, y_prob):
        # Penalty: Missed defect is much worse than false alarm
        y_pred = 1 if y_prob >= self.threshold else 0
        if y_true == 1 and y_pred == 0: return -10
        if y_true == 0 and y_pred == 1: return -2
        return 1

    def run_simulation(self):
        os.makedirs("experiments/results", exist_ok=True)
        rewards = [self.compute_reward(np.random.randint(0,2), np.random.random()) for _ in range(50)]
        plt.plot(np.cumsum(rewards))
        plt.title("RL Agent: Decision Threshold Learning")
        plt.savefig("experiments/results/rl_curve.png")

if __name__ == "__main__":
    BottleRLAgent().run_simulation()