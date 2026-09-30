import csv
from pathlib import Path
import matplotlib.pyplot as plt


results_folder = Path("..") / "04_Results"


def read_csv(filename):
    file_path = results_folder / filename

    with file_path.open(
        "r",
        newline="",
        encoding="utf-8"
    ) as file:
        return list(csv.DictReader(file))


# Read SIR results
sir_data = read_csv("baseline_sir_results.csv")

sir_days = [
    int(row["day"])
    for row in sir_data
]

sir_infectious = [
    float(row["infectious"])
    for row in sir_data
]


# Read SEIR results
seir_data = read_csv("seir_results.csv")

seir_days = [
    int(row["day"])
    for row in seir_data
]

seir_infectious = [
    float(row["infectious"])
    for row in seir_data
]


# Find peaks
sir_peak = max(sir_infectious)
sir_peak_day = sir_days[sir_infectious.index(sir_peak)]

seir_peak = max(seir_infectious)
seir_peak_day = seir_days[seir_infectious.index(seir_peak)]


# Print comparison
print("\nSIR vs SEIR COMPARISON")
print("=" * 60)

print(
    "SIR  | Peak:",
    round(sir_peak, 3),
    "| Peak day:",
    sir_peak_day
)

print(
    "SEIR | Peak:",
    round(seir_peak, 3),
    "| Peak day:",
    seir_peak_day
)


# Calculate percentage difference in peak
peak_difference = (
    (sir_peak - seir_peak)
    / sir_peak
) * 100

print(
    "Difference in peak:",
    round(peak_difference, 2),
    "%"
)


# Create comparison graph
plt.figure(figsize=(10, 6))

plt.plot(
    sir_days,
    sir_infectious,
    label="SIR"
)

plt.plot(
    seir_days,
    seir_infectious,
    label="SEIR"
)

plt.xlabel("Day")
plt.ylabel("Number of infectious people")
plt.title("SIR vs SEIR Model Comparison")
plt.legend()

output_graph = (
    results_folder
    / "sir_vs_seir_comparison.png"
)

plt.savefig(
    output_graph,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print("\nGraph saved to:")
print(output_graph.resolve())