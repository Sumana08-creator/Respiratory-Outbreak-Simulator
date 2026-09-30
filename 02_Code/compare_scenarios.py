import csv
from pathlib import Path
import matplotlib.pyplot as plt

baseline_file = Path("..") / "04_Results" / "baseline_sir_results.csv"
vaccination_file = Path("..") / "04_Results" / "vaccination_sir_results.csv"

def read_results(filename):
    with filename.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

baseline = read_results(baseline_file)
vaccination = read_results(vaccination_file)

baseline_days = [int(row["day"]) for row in baseline]
baseline_infectious = [float(row["infectious"]) for row in baseline]

vaccination_days = [int(row["day"]) for row in vaccination]
vaccination_infectious = [float(row["infectious"]) for row in vaccination]

plt.figure(figsize=(10, 6))

plt.plot(
    baseline_days,
    baseline_infectious,
    label="Baseline – No Intervention"
)

plt.plot(
    vaccination_days,
    vaccination_infectious,
    label="Vaccination – 40% Coverage"
)

plt.xlabel("Day")
plt.ylabel("Number of infectious people")
plt.title("Baseline vs Vaccination – SIR Model")
plt.legend()

output_file = Path("..") / "04_Results" / "baseline_vs_vaccination.png"

plt.savefig(output_file, dpi=300, bbox_inches="tight")
plt.close()

print("Comparison graph saved to:", output_file.resolve())