import csv
from pathlib import Path
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# Read immunity-by-year results
# ---------------------------------------------------------

input_file = (
    Path("..")
    / "04_Results"
    / "immunity_by_year.csv"
)

years = []
protected_percentages = []

with input_file.open(
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:
        years.append(int(row["sample_year"]))
        protected_percentages.append(
            float(row["protected_percentage"])
        )


# ---------------------------------------------------------
# Create immunity-over-time plot
# ---------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    years,
    protected_percentages,
    marker="o"
)

plt.xlabel("Sampling year")

plt.ylabel("Synthetic records classified as protected (%)")
plt.title(
    "Synthetic Enterovirus Immunity Over Time"
)

plt.ylim(0, 100)

plt.grid(True, alpha=0.3)

output_file = (
    Path("..")
    / "04_Results"
    / "immunity_over_time.png"
)

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Plot saved to:")
print(output_file.resolve())