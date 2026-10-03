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


# =========================================================
# 2. DERIVED EPIDEMIOLOGICAL VALUES
# =========================================================

R0 = BETA / GAMMA

CRITICAL_SUSCEPTIBILITY = 1 / R0

print(
    "Basic reproduction number (R0):",
    round(R0, 3)
)

print(
    "Critical susceptible fraction:",
    round(CRITICAL_SUSCEPTIBILITY, 4)
)

print(
    "Critical susceptible percentage:",
    round(
        CRITICAL_SUSCEPTIBILITY * 100,
        2
    ),
    "%"
)


# =========================================================
# 3. FILE PATHS
# =========================================================

results_folder = Path("..") / "04_Results"

results_folder.mkdir(exist_ok=True)

threshold_output = (
    results_folder
    / "immunity_threshold_analysis.csv"
)

threshold_plot = (
    results_folder
    / "immunity_threshold_analysis.png"
)


# =========================================================
# 4. SEIR SIMULATION FUNCTION
# =========================================================

def simulate_seir(
    susceptible_fraction
):
    """
    Run a deterministic SEIR simulation for a specified
    initial susceptible fraction.

    This is a synthetic methodological model and does
    not represent real enterovirus transmission data.
    """

    susceptible = (
        TOTAL_POPULATION
        * susceptible_fraction
    )

    exposed = INITIAL_EXPOSED

    infectious = INITIAL_INFECTIOUS

    removed = (
        TOTAL_POPULATION
        - susceptible
        - exposed
        - infectious
    )

    if removed < 0:
        raise ValueError(
            "Initial population allocation is invalid."
        )

    results = []

    cumulative_infections = 0.0

    results.append({
        "day": 0,
        "susceptible": susceptible,
        "exposed": exposed,
        "infectious": infectious,
        "removed": removed,
        "cumulative_infections":
            cumulative_infections
    })

    for day in range(
        1,
        SIMULATION_DAYS + 1
    ):

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

        susceptible -= new_exposures

        exposed += (
            new_exposures
            - new_infectious
        )

        infectious += (
            new_infectious
            - new_recoveries
        )

        removed += new_recoveries

        cumulative_infections += (
            new_exposures
        )

        results.append({
            "day": day,
            "susceptible": susceptible,
            "exposed": exposed,
            "infectious": infectious,
            "removed": removed,
            "cumulative_infections":
                cumulative_infections
        })

    return results


# =========================================================
# 5. SUSCEPTIBILITY SCENARIOS
# =========================================================

susceptibility_scenarios = [
    0.10,
    0.20,
    0.30,
    0.40,
    0.50,
    0.60,
    0.70,
    0.80,
    0.90
]


# =========================================================
# 6. RUN THRESHOLD ANALYSIS
# =========================================================

analysis_results = []


for susceptible_fraction in susceptibility_scenarios:

    # -----------------------------------------------------
    # Effective reproduction number
    # -----------------------------------------------------

    effective_reproduction = (
        R0
        * susceptible_fraction
    )

    # -----------------------------------------------------
    # Determine initial transmission status
    # -----------------------------------------------------

    if effective_reproduction > 1:

        emergence_indicator = (
            "Potential initial epidemic growth"
        )

    elif effective_reproduction == 1:

        emergence_indicator = (
            "Threshold condition"
        )

    else:

        emergence_indicator = (
            "No initial epidemic growth"
        )

    # -----------------------------------------------------
    # Run SEIR simulation
    # -----------------------------------------------------

    simulation = simulate_seir(
        susceptible_fraction
    )

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
    # Cumulative simulated infections
    # -----------------------------------------------------

    cumulative_infections = (
        simulation[-1][
            "cumulative_infections"
        ]
    )

    # -----------------------------------------------------
    # Initial susceptible population
    # -----------------------------------------------------

    initial_susceptible = (
        TOTAL_POPULATION
        * susceptible_fraction
    )

    initial_protected = (
        TOTAL_POPULATION
        - initial_susceptible
        - INITIAL_INFECTIOUS
        - INITIAL_EXPOSED
    )

    analysis_results.append({

        "susceptible_fraction":
            susceptible_fraction,

        "susceptible_percentage":
            susceptible_fraction * 100,

        "effective_reproduction_number":
            round(
                effective_reproduction,
                4
            ),

        "critical_susceptibility":
            round(
                CRITICAL_SUSCEPTIBILITY,
                4
            ),

        "emergence_indicator":
            emergence_indicator,

        "initial_susceptible":
            round(
                initial_susceptible,
                3
            ),

        "initial_protected":
            round(
                initial_protected,
                3
            ),

        "peak_infectious":
            round(
                peak_infectious,
                3
            ),

        "peak_day":
            peak_day,

        "cumulative_simulated_infections":
            round(
                cumulative_infections,
                3
            )
    })

    print()
    print(
        "Susceptible fraction:",
        round(
            susceptible_fraction * 100,
            1
        ),
        "%"
    )

    print(
        "R_eff:",
        round(
            effective_reproduction,
            4
        )
    )

    print(
        "Status:",
        emergence_indicator
    )

    print(
        "Peak infectious:",
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
# 7. SAVE RESULTS TO CSV
# =========================================================

fieldnames = [
    "susceptible_fraction",
    "susceptible_percentage",
    "effective_reproduction_number",
    "critical_susceptibility",
    "emergence_indicator",
    "initial_susceptible",
    "initial_protected",
    "peak_infectious",
    "peak_day",
    "cumulative_simulated_infections"
]


with threshold_output.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(
        analysis_results
    )


# =========================================================
# 8. CREATE R_EFF THRESHOLD GRAPH
# =========================================================

susceptibility_percentages = [
    result["susceptible_percentage"]
    for result in analysis_results
]

r_eff_values = [
    result["effective_reproduction_number"]
    for result in analysis_results
]


plt.figure(figsize=(10, 6))

plt.plot(
    susceptibility_percentages,
    r_eff_values,
    marker="o"
)

plt.axhline(
    y=1,
    linestyle="--",
    label="R_eff = 1 threshold"
)

plt.axvline(
    x=CRITICAL_SUSCEPTIBILITY * 100,
    linestyle="--",
    label="Critical susceptibility"
)

plt.xlabel(
    "Susceptible population (%)"
)

plt.ylabel(
    "Effective reproduction number"
)

plt.title(
    "Synthetic Susceptibility Threshold for Epidemic Growth"
)

plt.legend()

plt.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    threshold_plot,
    dpi=300,
    bbox_inches="tight"
)

plt.close()


# =========================================================
# 9. FINAL CONFIRMATION
# =========================================================

print()
print(
    "Threshold analysis completed."
)

print(
    "Results saved to:"
)

print(
    threshold_output.resolve()
)

print()
print(
    "Threshold plot saved to:"
)

print(
    threshold_plot.resolve()
)