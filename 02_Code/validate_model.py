import csv
from pathlib import Path


# Location of the baseline results
results_file = (
    Path("..")
    / "04_Results"
    / "baseline_sir_results.csv"
)


# Read the simulation results
with results_file.open(
    "r",
    newline="",
    encoding="utf-8"
) as file:

    data = list(csv.DictReader(file))


# Model population
total_population = 5000

# Convert values from text to numbers
for row in data:
    row["day"] = int(row["day"])
    row["susceptible"] = float(row["susceptible"])
    row["infectious"] = float(row["infectious"])
    row["recovered"] = float(row["recovered"])


# ------------------------------------------------
# CHECK 1: Initial conditions
# ------------------------------------------------

first_day = data[0]

initial_conditions_correct = (
    abs(first_day["susceptible"] - 4987.006) < 0.01
    and abs(first_day["infectious"] - 10.994) < 0.01
    and abs(first_day["recovered"] - 2.0) < 0.01
)


# ------------------------------------------------
# CHECK 2: Population conservation
# ------------------------------------------------

population_errors = []

for row in data:

    population_total = (
        row["susceptible"]
        + row["infectious"]
        + row["recovered"]
    )

    error = abs(population_total - total_population)

    population_errors.append(error)


maximum_population_error = max(population_errors)

population_conserved = maximum_population_error < 0.01


# ------------------------------------------------
# CHECK 3: No negative compartments
# ------------------------------------------------

negative_values = []

for row in data:

    if (
        row["susceptible"] < 0
        or row["infectious"] < 0
        or row["recovered"] < 0
    ):
        negative_values.append(row["day"])


no_negative_values = len(negative_values) == 0


# ------------------------------------------------
# CHECK 4: Susceptible population decreases
# ------------------------------------------------

susceptible_decreases = (
    data[-1]["susceptible"] < data[0]["susceptible"]
)


# ------------------------------------------------
# CHECK 5: Recovered population increases
# ------------------------------------------------

recovered_increases = (
    data[-1]["recovered"] > data[0]["recovered"]
)


# ------------------------------------------------
# Display results
# ------------------------------------------------

print("\nMODEL VALIDATION RESULTS")
print("=" * 60)

print(
    "Initial conditions correct:",
    initial_conditions_correct
)

print(
    "Population conserved:",
    population_conserved
)

print(
    "Maximum population error:",
    round(maximum_population_error, 10)
)

print(
    "Negative compartment values found:",
    len(negative_values)
)

print(
    "Susceptible population decreased:",
    susceptible_decreases
)

print(
    "Recovered population increased:",
    recovered_increases
)


# Overall result
all_checks_passed = (
    initial_conditions_correct
    and population_conserved
    and no_negative_values
    and susceptible_decreases
    and recovered_increases
)


print()

if all_checks_passed:
    print("OVERALL VALIDATION: PASSED")
else:
    print("OVERALL VALIDATION: CHECK FAILED")