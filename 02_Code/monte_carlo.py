import random
import csv
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

# Number of simulations
number_of_simulations = 1000

# Makes the random sampling reproducible
random.seed(42)

results = []


for simulation in range(1, number_of_simulations + 1):

    # Randomly sample beta and gamma
    beta = random.uniform(0.25, 0.35)
    gamma = random.uniform(0.15, 0.25)

    # Starting population
    susceptible = 4990
    infectious = 10
    recovered = 0

    total_population = susceptible + infectious + recovered

    # Store daily results for this simulation
    daily_results = []

    # Run SIR model for 180 days
    for day in range(1, 181):

        new_infections = (
            beta * susceptible * infectious / total_population
        )

        recoveries = gamma * infectious

        susceptible = susceptible - new_infections
        infectious = infectious + new_infections - recoveries
        recovered = recovered + recoveries

        daily_results.append({
            "day": day,
            "infectious": infectious
        })

    # Find epidemic peak
    infectious_values = [
        row["infectious"] for row in daily_results
    ]

    peak_infectious = max(infectious_values)

    peak_index = infectious_values.index(peak_infectious)

    peak_day = daily_results[peak_index]["day"]

    # Calculate R0
    r0 = beta / gamma

    results.append({
        "simulation": simulation,
        "beta": beta,
        "gamma": gamma,
        "r0": r0,
        "peak_infectious": peak_infectious,
        "peak_day": peak_day,
        "cumulative_infections": recovered
    })


# Save all simulation results to CSV
output_file = (
    Path("..")
    / "04_Results"
    / "monte_carlo_results.csv"
)

with output_file.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "simulation",
            "beta",
            "gamma",
            "r0",
            "peak_infectious",
            "peak_day",
            "cumulative_infections"
        ]
    )

    writer.writeheader()
    writer.writerows(results)


# Calculate simple summary statistics
peak_values = [
    result["peak_infectious"]
    for result in results
]

minimum_peak = min(peak_values)
median_peak = np.percentile(peak_values, 50)
fifth_percentile = np.percentile(peak_values, 5)
ninety_fifth_percentile = np.percentile(peak_values, 95)
maximum_peak = max(peak_values)

print("\nMONTE CARLO SIMULATION")
print("=" * 60)

print("Number of simulations:", number_of_simulations)

print("Minimum peak:", round(minimum_peak, 3))
print("5th percentile:", round(fifth_percentile, 3))
print("Median peak:", round(median_peak, 3))
print("95th percentile:", round(ninety_fifth_percentile, 3))
print("Maximum peak:", round(maximum_peak, 3))


# Create histogram
plt.figure(figsize=(10, 6))

plt.hist(
    peak_values,
    bins=30
)

plt.xlabel("Simulated peak infectious population")
plt.ylabel("Number of simulations")
plt.title("Monte Carlo Distribution of Simulated Epidemic Peaks")

histogram_file = (
    Path("..")
    / "04_Results"
    / "monte_carlo_peak_distribution.png"
)

plt.savefig(
    histogram_file,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nHistogram saved to:")
print(histogram_file.resolve())
print("\nResults saved to:")
print(output_file.resolve())