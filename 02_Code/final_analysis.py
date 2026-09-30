import csv
from pathlib import Path
import matplotlib.pyplot as plt


RESULTS_FOLDER = Path("..") / "04_Results"


def read_results(filename):
    file_path = RESULTS_FOLDER / filename

    with file_path.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


scenarios = {
    "Baseline": {
        "file": "baseline_sir_results.csv",
        "initially_protected": 0
    },
    "Vaccination": {
        "file": "vaccination_sir_results.csv",
        "initially_protected": 1600
    },
    "Transmission Reduction": {
        "file": "transmission_reduction_sir_results.csv",
        "initially_protected": 0
    },
    "Combined Intervention": {
        "file": "combined_intervention_sir_results.csv",
        "initially_protected": 1600
    }
}


summary = []


for scenario_name, scenario_info in scenarios.items():

    data = read_results(scenario_info["file"])

    days = [int(row["day"]) for row in data]
    infectious = [float(row["infectious"]) for row in data]
    susceptible = [float(row["susceptible"]) for row in data]
    recovered = [float(row["recovered"]) for row in data]

    peak_infectious = max(infectious)
    peak_index = infectious.index(peak_infectious)
    peak_day = days[peak_index]

    final_susceptible = susceptible[-1]
    final_infectious = infectious[-1]

    # For vaccination scenarios, remove the 1,600
    # initially protected people from the recovered/removed
    # compartment before estimating cumulative infections.
    cumulative_infections = recovered[-1] - scenario_info["initially_protected"]

    summary.append({
        "scenario": scenario_name,
        "peak_infectious": round(peak_infectious, 3),
        "peak_day": peak_day,
        "final_susceptible": round(final_susceptible, 3),
        "final_infectious": round(final_infectious, 3),
        "cumulative_simulated_infections": round(cumulative_infections, 3)
    })


# Save summary table
summary_file = RESULTS_FOLDER / "scenario_summary.csv"

with summary_file.open("w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "scenario",
        "peak_infectious",
        "peak_day",
        "final_susceptible",
        "final_infectious",
        "cumulative_simulated_infections"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(summary)


# Print summary to PowerShell
print("\nFINAL SCENARIO COMPARISON")
print("=" * 70)

for row in summary:
    print(
        f"{row['scenario']}: "
        f"Peak = {row['peak_infectious']}, "
        f"Peak day = {row['peak_day']}, "
        f"Cumulative simulated infections = "
        f"{row['cumulative_simulated_infections']}"
    )


# Create four-scenario epidemic curve
plt.figure(figsize=(10, 6))

for scenario_name, scenario_info in scenarios.items():

    data = read_results(scenario_info["file"])

    days = [int(row["day"]) for row in data]
    infectious = [float(row["infectious"]) for row in data]

    plt.plot(days, infectious, label=scenario_name)


plt.xlabel("Day")
plt.ylabel("Number of infectious people")
plt.title("Comparison of Public Health Intervention Scenarios")
plt.legend()

comparison_graph = (
    RESULTS_FOLDER / "all_scenarios_epidemic_curves.png"
)

plt.savefig(comparison_graph, dpi=300, bbox_inches="tight")
plt.close()


# Create peak comparison bar chart
scenario_names = [row["scenario"] for row in summary]
peak_values = [row["peak_infectious"] for row in summary]

plt.figure(figsize=(10, 6))
plt.bar(scenario_names, peak_values)

plt.ylabel("Peak infectious population")
plt.title("Peak Infectious Population by Scenario")
plt.xticks(rotation=20, ha="right")

peak_graph = RESULTS_FOLDER / "peak_comparison.png"

plt.savefig(peak_graph, dpi=300, bbox_inches="tight")
plt.close()


print("\nFiles created:")
print(summary_file.resolve())
print(comparison_graph.resolve())
print(peak_graph.resolve())