import csv
from pathlib import Path
import matplotlib.pyplot as plt


results_folder = Path("..") / "04_Results"


def read_results(filename):
    file_path = results_folder / filename

    with file_path.open(
        "r",
        newline="",
        encoding="utf-8"
    ) as file:
        return list(csv.DictReader(file))


scenarios = [
    {
        "model": "SIR",
        "scenario": "Baseline",
        "file": "baseline_sir_results.csv"
    },
    {
        "model": "SIR",
        "scenario": "Transmission Reduction",
        "file": "transmission_reduction_sir_results.csv"
    },
    {
        "model": "SEIR",
        "scenario": "Baseline",
        "file": "seir_results.csv"
    },
    {
        "model": "SEIR",
        "scenario": "Transmission Reduction",
        "file": "seir_transmission_reduction_results.csv"
    }
]


summary = []


# -----------------------------------------
# Read all four model outputs
# -----------------------------------------

for item in scenarios:

    data = read_results(item["file"])

    days = [
        int(row["day"])
        for row in data
    ]

    infectious = [
        float(row["infectious"])
        for row in data
    ]

    peak_infectious = max(infectious)

    peak_index = infectious.index(
        peak_infectious
    )

    peak_day = days[peak_index]

    summary.append({
        "model": item["model"],
        "scenario": item["scenario"],
        "peak_infectious": peak_infectious,
        "peak_day": peak_day
    })


# -----------------------------------------
# Calculate intervention peak reductions
# -----------------------------------------

sir_baseline = next(
    row["peak_infectious"]
    for row in summary
    if row["model"] == "SIR"
    and row["scenario"] == "Baseline"
)

sir_intervention = next(
    row["peak_infectious"]
    for row in summary
    if row["model"] == "SIR"
    and row["scenario"] == "Transmission Reduction"
)

seir_baseline = next(
    row["peak_infectious"]
    for row in summary
    if row["model"] == "SEIR"
    and row["scenario"] == "Baseline"
)

seir_intervention = next(
    row["peak_infectious"]
    for row in summary
    if row["model"] == "SEIR"
    and row["scenario"] == "Transmission Reduction"
)


sir_reduction = (
    (sir_baseline - sir_intervention)
    / sir_baseline
) * 100

seir_reduction = (
    (seir_baseline - seir_intervention)
    / seir_baseline
) * 100


# -----------------------------------------
# Add reduction values to summary
# -----------------------------------------

for row in summary:

    row["peak_reduction_vs_model_baseline"] = ""

    if (
        row["model"] == "SIR"
        and row["scenario"] == "Transmission Reduction"
    ):
        row["peak_reduction_vs_model_baseline"] = sir_reduction

    elif (
        row["model"] == "SEIR"
        and row["scenario"] == "Transmission Reduction"
    ):
        row["peak_reduction_vs_model_baseline"] = seir_reduction


# -----------------------------------------
# Save comparison table
# -----------------------------------------

summary_file = (
    results_folder
    / "final_model_comparison.csv"
)

with summary_file.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "model",
            "scenario",
            "peak_infectious",
            "peak_day",
            "peak_reduction_vs_model_baseline"
        ]
    )

    writer.writeheader()

    for row in summary:

        writer.writerow({
            "model": row["model"],
            "scenario": row["scenario"],
            "peak_infectious":
                round(row["peak_infectious"], 3),
            "peak_day":
                row["peak_day"],
            "peak_reduction_vs_model_baseline":
                (
                    round(
                        row["peak_reduction_vs_model_baseline"],
                        2
                    )
                    if row[
                        "peak_reduction_vs_model_baseline"
                    ] != ""
                    else ""
                )
        })


# -----------------------------------------
# Print final results
# -----------------------------------------

print("\nFINAL SIR vs SEIR COMPARISON")
print("=" * 70)

for row in summary:

    print(
        row["model"],
        "|",
        row["scenario"],
        "| Peak:",
        round(row["peak_infectious"], 3),
        "| Peak day:",
        row["peak_day"]
    )

print()
print(
    "SIR transmission-reduction peak reduction:",
    round(sir_reduction, 2),
    "%"
)

print(
    "SEIR transmission-reduction peak reduction:",
    round(seir_reduction, 2),
    "%"
)


# -----------------------------------------
# Create final comparison graph
# -----------------------------------------

plt.figure(figsize=(10, 6))


for item in scenarios:

    data = read_results(item["file"])

    days = [
        int(row["day"])
        for row in data
    ]

    infectious = [
        float(row["infectious"])
        for row in data
    ]

    label = (
        item["model"]
        + " – "
        + item["scenario"]
    )

    plt.plot(
        days,
        infectious,
        label=label
    )


plt.xlabel("Day")
plt.ylabel("Number of infectious people")
plt.title("SIR vs SEIR: Baseline and Transmission Reduction")
plt.legend()


output_graph = (
    results_folder
    / "final_sir_seir_intervention_comparison.png"
)

plt.savefig(
    output_graph,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


print()
print("Comparison table saved to:")
print(summary_file.resolve())

print()
print("Final graph saved to:")
print(output_graph.resolve())