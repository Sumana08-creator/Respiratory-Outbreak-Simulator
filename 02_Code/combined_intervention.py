import csv
from pathlib import Path
import matplotlib.pyplot as plt

susceptible = 3390
infectious = 10
recovered = 1600

total_population = susceptible + infectious + recovered

beta = 0.30
gamma = 0.20

results = []

for day in range(1, 181):

    if day >= 30:
        effective_beta = beta * 0.50
    else:
        effective_beta = beta

    new_infections = effective_beta * susceptible * infectious / total_population
    recoveries = gamma * infectious

    susceptible = susceptible - new_infections
    infectious = infectious + new_infections - recoveries
    recovered = recovered + recoveries

    results.append({
        "day": day,
        "susceptible": susceptible,
        "infectious": infectious,
        "recovered": recovered
    })

    print("Day:", day)
    print("Susceptible:", round(susceptible, 3))
    print("Infectious:", round(infectious, 3))
    print("Recovered:", round(recovered, 3))
    print()

print("Number of days saved:", len(results))

# Save results
output_file = Path("..") / "04_Results" / "combined_intervention_sir_results.csv"
with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["day", "susceptible", "infectious", "recovered"]
    )
    writer.writeheader()
    writer.writerows(results)

print("Results saved to:", output_file.resolve())

# Prepare data for graph
days = [row["day"] for row in results]
infectious_values = [row["infectious"] for row in results]

# Create graph
plt.figure(figsize=(10, 6))
plt.plot(days, infectious_values)

plt.xlabel("Day")
plt.ylabel("Number of infectious people")
plt.title("Combined Intervention Scenario – SIR Model")
# Save graph
output_graph = Path("..") / "04_Results" / "combined_intervention_epidemic_curve.png"
plt.savefig(output_graph, dpi=300, bbox_inches="tight")
plt.close()

print("Graph saved to:", output_graph.resolve())

# Find peak
peak_infectious = max(infectious_values)
peak_index = infectious_values.index(peak_infectious)
peak_day = days[peak_index]

print("Peak infectious population:", round(peak_infectious, 3))
print("Day of epidemic peak:", peak_day)