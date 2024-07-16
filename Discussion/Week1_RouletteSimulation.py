# Write a simulation for  a simple game of chance (e.g., drawing cards, rolling one or more dice, etc.)   Run the simulation 1000 times and interpret the outcome.  Post your code here, and discuss what might be done to improve it.

# %%
import random
import matplotlib.pyplot as plt

# Set a seed for reproducibility
random.seed(1125)

# Define a function to simulate a spin of the roulette wheel
def roulette_spin():
    # American Roulette: 38 slots: numbers 1-36, a single zero, and a double zero
    return random.choice(list(range(37)) + ['00'])

def simulate_roulette(num_spins, bet_amount, bet_type):
    results = {i: 0 for i in ['00'] + list(range(37))}  # Initialize results dictionary
    winnings = 0

    for _ in range(num_spins):
        spin_result = roulette_spin()
        results[spin_result] += 1  # Increment the count for the spin result

        # Check if the bet won
        if bet_type == 'even' and isinstance(spin_result, int) and spin_result % 2 == 0 and spin_result != 0:
            winnings += bet_amount
        elif bet_type == 'odd' and isinstance(spin_result, int) and spin_result % 2 == 1:
            winnings += bet_amount
        elif bet_type == spin_result:
            winnings += bet_amount * 35  # Winning a single number bet pays 35 to 1
        else:
            winnings -= bet_amount  # Subtract bet amount if the bet is lost

    return results, winnings

# Run the simulation 1000 times
simulation_results, total_winnings = simulate_roulette(1000, 10, 'even')

# Convert keys to strings for visualization
keys_as_str = [str(key) for key in simulation_results.keys()]

# Define colors for each number
colors = ['green' if key == '0' or key == '00' else 'blue' if int(key) % 2 == 0 else 'red' for key in keys_as_str]

# Visualize the results using a bar chart
plt.bar(keys_as_str, simulation_results.values(), color=colors)
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Roulette Simulation Results')
plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
plt.show()


# Print the total winnings
print(f'Total winnings: ${total_winnings:.2f}')

# %%
