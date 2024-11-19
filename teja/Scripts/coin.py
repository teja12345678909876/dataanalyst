import random

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def simulate_sequence(target_length, target_outcome='Heads'):
    # Simulate getting a specific sequence of outcomes
    return all(flip_coin() == target_outcome for _ in range(target_length))

def calculate_probability(sequence_length, num_trials=1000, target_outcome='Heads'):
    # Run multiple trials and calculate probability
    successful_trials = sum(simulate_sequence(sequence_length, target_outcome) 
                          for _ in range(num_trials))
    return successful_trials / num_trials

def main():
    # Test different sequence lengths
    for length in [1, 2, 3, 4, 5]:
        empirical_prob = calculate_probability(length)
        theoretical_prob = (1/2)**length
        
        print(f"\nFor {length} {('Head' if length==1 else 'Heads')} in a row:")
        print(f"Empirical probability: {empirical_prob:.4f}")
        print(f"Theoretical probability: {theoretical_prob:.4f}")

if __name__ == "__main__":
    print("Coin Flip Probability Simulator")
    print("------------------------------")
    main()