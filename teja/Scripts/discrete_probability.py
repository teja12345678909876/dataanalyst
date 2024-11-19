import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

class DiscreteDistribution:
    def __init__(self):
        # Example: Rolling a die (uniform distribution)
        self.die_outcomes = {1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
        
        # Example: Binomial distribution (coin flips)
        self.coin_prob = 0.5  # probability of heads
        
        # Example: Custom discrete distribution
        self.custom_dist = {
            'A': 0.4,
            'B': 0.3,
            'C': 0.2,
            'D': 0.1
        }

    def expected_value(self, distribution):
        """Calculate expected value of a discrete distribution"""
        return sum(x * p for x, p in distribution.items())

    def variance(self, distribution):
        """Calculate variance of a discrete distribution"""
        exp_val = self.expected_value(distribution)
        return sum((x - exp_val)**2 * p for x, p in distribution.items())

    def simulate_die_rolls(self, num_rolls=1000):
        """Simulate rolling a die multiple times"""
        outcomes = random.choices(
            list(self.die_outcomes.keys()),
            weights=list(self.die_outcomes.values()),
            k=num_rolls
        )
        return Counter(outcomes)

    def binomial_probability(self, n, k):
        """Calculate probability of k successes in n trials (binomial)"""
        from math import comb
        p = self.coin_prob
        return comb(n, k) * (p**k) * ((1-p)**(n-k))

    def plot_distribution(self, data, title):
        """Plot a discrete distribution"""
        plt.figure(figsize=(10, 6))
        if isinstance(data, Counter):
            # Normalize the counts to get probabilities
            total = sum(data.values())
            probabilities = {k: v/total for k, v in data.items()}
            plt.bar(probabilities.keys(), probabilities.values())
        else:
            plt.bar(data.keys(), data.values())
        plt.title(title)
        plt.xlabel('Outcome')
        plt.ylabel('Probability')
        plt.show()

def main():
    dp = DiscreteDistribution()

    # 1. Analyze die rolls
    print("Die Rolling Analysis:")
    print(f"Expected Value: {dp.expected_value(dp.die_outcomes):.2f}")
    print(f"Variance: {dp.variance(dp.die_outcomes):.2f}")
    
    # Simulate die rolls and plot
    simulated_rolls = dp.simulate_die_rolls(1000)
    dp.plot_distribution(simulated_rolls, "Simulated Die Rolls Distribution")

    # 2. Binomial Distribution Example (coin flips)
    print("\nBinomial Distribution (10 coin flips):")
    n = 10  # number of trials
    for k in range(n + 1):
        prob = dp.binomial_probability(n, k)
        print(f"P(X = {k}) = {prob:.4f}")

    # Plot binomial distribution
    binomial_dist = {k: dp.binomial_probability(n, k) for k in range(n + 1)}
    dp.plot_distribution(binomial_dist, f"Binomial Distribution (n={n}, p={dp.coin_prob})")

    # 3. Custom Distribution Analysis
    print("\nCustom Distribution Analysis:")
    print(f"Expected Value cannot be calculated (non-numeric outcomes)")
    print("Probabilities:")
    for outcome, prob in dp.custom_dist.items():
        print(f"P({outcome}) = {prob:.2f}")
    
    dp.plot_distribution(dp.custom_dist, "Custom Discrete Distribution")

if __name__ == "__main__":
    main() 