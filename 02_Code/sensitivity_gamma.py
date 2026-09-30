import csv
from pathlib import Path
import matplotlib.pyplot as plt


# Recovery/removal values we want to test
gamma_values = [0.15, 0.20, 0.25]

beta = 0.30

results = []


# Run the model once for each gamma value
for gamma in gamma_values:

    # Reset the starting population
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

    # Find peak
    infectious_values = [
        row["infectious"] for row in daily_results
    ]

    peak_infectious = max(infectious_values)
    peak_index = infectious_values.index(peak_infectious)
    peak_day = daily_results[peak_index]["day"]

    # Calculate approximate infectious period
    infectious_period = 1 / gamma

    # Calculate R0 for this scenario
    r0 = beta / gamma

    results.append({
        "gamma": gamma,
        "infectious_period_days": infectious_period,
        "r0": r0,
        "peak_infectious": peak_infectious,
        "peak_day": peak_day,
        "cumulative_infections": recovered
    })


# Print results
print("\nGAMMA SENSITIVITY ANALYSIS")
print("=" * 75)

for result in results:

    print(
        "Gamma:",
        result["gamma"],
        "| Infectious period:",
        round(result["infectious_period_days"], 2),
        "days",
        "| R0:",
        round(result["r0"], 2),
        "| Peak:",
        round(result["peak_infectious"], 3),
        "| Peak day:",
        result["peak_day"],
        "| Cumulative infections:",
        round(result["cumulative_infections"], 3)
    )


# Save CSV
output_file = (
    Path("..")
    / "04_Results"
    / "sensitivity_gamma_results.csv"
)

with output_file.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "gamma",
            "infectious_period_days",
            "r0",
            "peak_infectious",
            "peak_day",
            "cumulative_infections"
        ]
    )

    writer.writeheader()
    writer.writerows(results)


# Create sensitivity graph
gamma_values_for_graph = [
    result["gamma"] for result in results
]

peak_values_for_graph = [
    result["peak_infectious"] for result in results
]

plt.figure(figsize=(8, 5))

plt.plot(
    gamma_values_for_graph,
    peak_values_for_graph,
    marker="o"
)

plt.xlabel("Recovery/removal parameter γ")
plt.ylabel("Peak infectious population")
plt.title("Sensitivity of Epidemic Peak to γ")

output_graph = (
    Path("..")
    / "04_Results"
    / "sensitivity_gamma_peak.png"
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