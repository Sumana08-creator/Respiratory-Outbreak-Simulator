import csv
from pathlib import Path
import matplotlib.pyplot as plt


# Values we want to test
beta_values = [0.25, 0.30, 0.35]

gamma = 0.20

results = []


# Run the model once for each beta value
for beta in beta_values:

    # Reset the starting population for each experiment
    susceptible = 4990
    infectious = 10
    recovered = 0

    total_population = susceptible + infectious + recovered

    daily_results = []

    # Simulate 180 days
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
            "susceptible": susceptible,
            "infectious": infectious,
            "recovered": recovered
        })

    # Find the peak
    infectious_values = [
        row["infectious"] for row in daily_results
    ]

    peak_infectious = max(infectious_values)

    peak_index = infectious_values.index(peak_infectious)

    peak_day = daily_results[peak_index]["day"]

    cumulative_infections = recovered

    results.append({
        "beta": beta,
        "peak_infectious": peak_infectious,
        "peak_day": peak_day,
        "cumulative_infections": cumulative_infections
    })


# Print the results
print("\nBETA SENSITIVITY ANALYSIS")
print("=" * 60)

for result in results:

    print(
        "Beta:",
        result["beta"],
        "| Peak:",
        round(result["peak_infectious"], 3),
        "| Peak day:",
        result["peak_day"],
        "| Cumulative infections:",
        round(result["cumulative_infections"], 3)
    )


# Save results as CSV
output_file = (
    Path("..")
    / "04_Results"
    / "sensitivity_beta_results.csv"
)

with output_file.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "beta",
            "peak_infectious",
            "peak_day",
            "cumulative_infections"
        ]
    )

    writer.writeheader()
    writer.writerows(results)


# Create a graph of beta vs peak infections
beta_values_for_graph = [
    result["beta"] for result in results
]

peak_values_for_graph = [
    result["peak_infectious"] for result in results
]

plt.figure(figsize=(8, 5))

plt.plot(
    beta_values_for_graph,
    peak_values_for_graph,
    marker="o"
)

plt.xlabel("Transmission parameter β")
plt.ylabel("Peak infectious population")
plt.title("Sensitivity of Epidemic Peak to β")

output_graph = (
    Path("..")
    / "04_Results"
    / "sensitivity_beta_peak.png"
)

plt.savefig(
    output_graph,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nResults saved to:")
print(output_file.resolve())

print("\nGraph saved to:")
print(output_graph.resolve())