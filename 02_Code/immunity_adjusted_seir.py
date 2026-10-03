import csv
from pathlib import Path
import csv
from pathlib import Path

import matplotlib.pyplot as plt


# =========================================================
# 1. MODEL SETTINGS
# =========================================================

TOTAL_POPULATION = 5000
INITIAL_INFECTIOUS = 10
INITIAL_EXPOSED = 0

BETA = 0.30
GAMMA = 0.20
SIGMA = 1.11

SIMULATION_DAYS = 180

# We will use the latest synthetic sampling year
# as the starting immunity profile.
SELECTED_YEAR = 2025


# =========================================================
# 2. FILE PATHS
# =========================================================

input_file = (
    Path("..")
    / "04_Results"
    / "population_susceptibility_by_year_type.csv"
)

results_folder = Path("..") / "04_Results"

summary_output = (
    results_folder
    / "immunity_adjusted_seir_results.csv"
)

epidemic_curve_output = (
    results_folder
    / "immunity_adjusted_seir_curves.png"
)

peak_comparison_output = (
    results_folder
    / "immunity_adjusted_seir_peak_comparison.png"
)


# =========================================================
# 3. READ POPULATION SUSCEPTIBILITY DATA
# =========================================================

susceptibility_data = []

with input_file.open(
    "r",
    newline="",
    encoding="utf-8"
) as file:

    reader = csv.DictReader(file)

    for row in reader:

        susceptibility_data.append({
            "sample_year": int(row["sample_year"]),
            "enterovirus_type": row["enterovirus_type"],
            "mean_susceptibility": float(
                row["mean_susceptibility"]
            )
        })


print(
    "Susceptibility records loaded:",
    len(susceptibility_data)
)


# =========================================================
# 4. SEIR SIMULATION FUNCTION
# =========================================================

def simulate_seir(mean_susceptibility):
    """
    Run a deterministic SEIR simulation using the
    synthetic population susceptibility estimate.

    The synthetic susceptibility estimate determines
    the initial susceptible population.

    This is a methodological modelling exercise and
    does not represent real enterovirus epidemiology.
    """

    # -----------------------------------------------------
    # Initial susceptible population
    # -----------------------------------------------------

    susceptible = (
        TOTAL_POPULATION
        * mean_susceptibility
    )

    # We keep the initial infectious population fixed.
    infectious = INITIAL_INFECTIOUS

    exposed = INITIAL_EXPOSED

    # Everyone not initially susceptible or infectious
    # is treated as protected/removed at model start.
    removed = (
        TOTAL_POPULATION
        - susceptible
        - exposed
        - infectious
    )

    # Prevent impossible negative values
    if removed < 0:
        raise ValueError(
            "Initial population allocation is invalid."
        )

    # -----------------------------------------------------
    # Store simulation results
    # -----------------------------------------------------

    results = []

    cumulative_new_infections = 0.0

    # Store initial state
    results.append({
        "day": 0,
        "susceptible": susceptible,
        "exposed": exposed,
        "infectious": infectious,
        "removed": removed,
        "cumulative_new_infections":
            cumulative_new_infections
    })

    # -----------------------------------------------------
    # Daily SEIR simulation
    # -----------------------------------------------------

    for day in range(1, SIMULATION_DAYS + 1):

        new_exposures = (
            BETA
            * susceptible
            * infectious
            / TOTAL_POPULATION
        )

        new_infectious = (
            SIGMA
            * exposed
        )

        new_recoveries = (
            GAMMA
            * infectious
        )

        # Update compartments
        susceptible = (
            susceptible
            - new_exposures
        )

        exposed = (
            exposed
            + new_exposures
            - new_infectious
        )

        infectious = (
            infectious
            + new_infectious
            - new_recoveries
        )

        removed = (
            removed
            + new_recoveries
        )

        cumulative_new_infections += (
            new_exposures
        )

        results.append({
            "day": day,
            "susceptible": susceptible,
            "exposed": exposed,
            "infectious": infectious,
            "removed": removed,
            "cumulative_new_infections":
                cumulative_new_infections
        })

    return results


# =========================================================
# 5. RUN THE MODEL FOR EACH ENTEROVIRUS TYPE
# =========================================================

selected_records = [
    row
    for row in susceptibility_data
    if row["sample_year"] == SELECTED_YEAR
]


if not selected_records:

    raise ValueError(
        f"No susceptibility data found for "
        f"year {SELECTED_YEAR}."
    )


simulation_outputs = []


for record in selected_records:

    virus_type = record["enterovirus_type"]

    mean_susceptibility = (
        record["mean_susceptibility"]
    )

    print()
    print(
        "Running SEIR model for:",
        virus_type
    )

    print(
        "Mean synthetic susceptibility:",
        round(
            mean_susceptibility,
            4
        )
    )

    simulation = simulate_seir(
        mean_susceptibility
    )

    # -----------------------------------------------------
    # Extract infectious trajectory
    # -----------------------------------------------------

    infectious_values = [
        row["infectious"]
        for row in simulation
    ]

    days = [
        row["day"]
        for row in simulation
    ]

    # -----------------------------------------------------
    # Epidemic peak
    # -----------------------------------------------------

    peak_infectious = max(
        infectious_values
    )

    peak_index = infectious_values.index(
        peak_infectious
    )

    peak_day = days[peak_index]

    # -----------------------------------------------------
    # Final cumulative infections
    # -----------------------------------------------------

    cumulative_infections = (
        simulation[-1][
            "cumulative_new_infections"
        ]
    )

    initial_susceptible = (
        TOTAL_POPULATION
        * mean_susceptibility
    )

    initial_protected = (
        TOTAL_POPULATION
        - initial_susceptible
        - INITIAL_EXPOSED
        - INITIAL_INFECTIOUS
    )

    simulation_outputs.append({
        "sample_year": SELECTED_YEAR,
        "enterovirus_type": virus_type,
        "mean_susceptibility":
            mean_susceptibility,
        "initial_susceptible":
            round(initial_susceptible, 3),
        "initial_protected":
            round(initial_protected, 3),
        "peak_infectious":
            round(peak_infectious, 3),
        "peak_day":
            peak_day,
        "cumulative_simulated_infections":
            round(
                cumulative_infections,
                3
            ),
        "simulation": simulation
    })

    print(
        "Peak infectious population:",
        round(
            peak_infectious,
            3
        )
    )

    print(
        "Peak day:",
        peak_day
    )

    print(
        "Cumulative simulated infections:",
        round(
            cumulative_infections,
            3
        )
    )


# =========================================================
# 6. SAVE SUMMARY CSV
# =========================================================

fieldnames = [
    "sample_year",
    "enterovirus_type",
    "mean_susceptibility",
    "initial_susceptible",
    "initial_protected",
    "peak_infectious",
    "peak_day",
    "cumulative_simulated_infections"
]


with summary_output.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for output in simulation_outputs:

        row = {
            key: output[key]
            for key in fieldnames
        }

        writer.writerow(row)


# =========================================================
# 7. CREATE EPIDEMIC CURVE COMPARISON
# =========================================================

plt.figure(figsize=(10, 6))

for output in simulation_outputs:

    days = [
        row["day"]
        for row in output["simulation"]
    ]

    infectious_values = [
        row["infectious"]
        for row in output["simulation"]
    ]

    plt.plot(
        days,
        infectious_values,
        marker="o",
        markersize=3,
        label=output[
            "enterovirus_type"
        ]
    )


plt.xlabel("Day")

plt.ylabel(
    "Number of infectious individuals"
)

plt.title(
    "Immunity-Adjusted SEIR Simulations by Enterovirus Type"
)

plt.legend()

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    epidemic_curve_output,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# =========================================================
# 8. CREATE PEAK COMPARISON
# =========================================================

virus_types = [
    output["enterovirus_type"]
    for output in simulation_outputs
]

peak_values = [
    output["peak_infectious"]
    for output in simulation_outputs
]


plt.figure(figsize=(10, 6))

plt.bar(
    virus_types,
    peak_values
)

plt.xlabel(
    "Enterovirus type"
)

plt.ylabel(
    "Peak infectious population"
)

plt.title(
    "Immunity-Adjusted SEIR Epidemic Peaks"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    peak_comparison_output,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# =========================================================
# 9. FINAL CONFIRMATION
# =========================================================

print()
print(
    "SEIR summary saved to:"
)

print(
    summary_output.resolve()
)

print()
print(
    "Epidemic curves saved to:"
)

print(
    epidemic_curve_output.resolve()
)

print()
print(
    "Peak comparison saved to:"
)

print(
    peak_comparison_output.resolve()
)

print()
print(
    "Immunity-adjusted SEIR analysis completed."
)