import csv
from pathlib import Path
import matplotlib.pyplot as plt


# -----------------------------
# Initial population
# -----------------------------

susceptible = 4990
exposed = 0
infectious = 10
recovered = 0

total_population = (
    susceptible
    + exposed
    + infectious
    + recovered
)


# -----------------------------
# Model parameters
# -----------------------------

beta = 0.30
gamma = 0.20
sigma = 1.11


# -----------------------------
# Store daily results
# -----------------------------

results = []


# -----------------------------
# Run SEIR model for 180 days
# -----------------------------

for day in range(1, 181):

    # S → E
    new_exposed = (
        beta
        * susceptible
        * infectious
        / total_population
    )

    # E → I
    new_infectious = sigma * exposed

    # I → R
    recoveries = gamma * infectious

    # Update compartments
    susceptible = susceptible - new_exposed

    exposed = (
        exposed
        + new_exposed
        - new_infectious
    )

    infectious = (
        infectious
        + new_infectious
        - recoveries
    )

    recovered = recovered + recoveries

    # Save this day's results
    results.append({
        "day": day,
        "susceptible": susceptible,
        "exposed": exposed,
        "infectious": infectious,
        "recovered": recovered
    })


# -----------------------------
# Save results to CSV
# -----------------------------

output_file = (
    Path("..")
    / "04_Results"
    / "seir_results.csv"
)

with output_file.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "day",
            "susceptible",
            "exposed",
            "infectious",
            "recovered"
        ]
    )

    writer.writeheader()
    writer.writerows(results)


# -----------------------------
# Prepare data for graph
# -----------------------------

days = [
    row["day"]
    for row in results
]

susceptible_values = [
    row["susceptible"]
    for row in results
]

exposed_values = [
    row["exposed"]
    for row in results
]

infectious_values = [
    row["infectious"]
    for row in results
]

recovered_values = [
    row["recovered"]
    for row in results
]


# -----------------------------
# Create SEIR graph
# -----------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    days,
    susceptible_values,
    label="Susceptible"
)

plt.plot(
    days,
    exposed_values,
    label="Exposed"
)

plt.plot(
    days,
    infectious_values,
    label="Infectious"
)

plt.plot(
    days,
    recovered_values,
    label="Recovered/Removed"
)

plt.xlabel("Day")
plt.ylabel("Population")
plt.title("SEIR Respiratory Outbreak Model")

plt.legend()

output_graph = (
    Path("..")
    / "04_Results"
    / "seir_model_curve.png"
)

plt.savefig(
    output_graph,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# -----------------------------
# Find infectious peak
# -----------------------------

peak_infectious = max(
    infectious_values
)

peak_index = infectious_values.index(
    peak_infectious
)

peak_day = days[peak_index]


# -----------------------------
# Display results
# -----------------------------

print("\nSEIR SIMULATION")
print("=" * 60)

print(
    "Number of days simulated:",
    len(results)
)

print(
    "Peak infectious population:",
    round(peak_infectious, 3)
)

print(
    "Day of epidemic peak:",
    peak_day
)

print(
    "Final susceptible:",
    round(susceptible_values[-1], 3)
)

print(
    "Final exposed:",
    round(exposed_values[-1], 3)
)

print(
    "Final infectious:",
    round(infectious_values[-1], 3)
)

print(
    "Final recovered/removed:",
    round(recovered_values[-1], 3)
)

print("\nResults saved to:")
print(output_file.resolve())

print("\nGraph saved to:")
print(output_graph.resolve())