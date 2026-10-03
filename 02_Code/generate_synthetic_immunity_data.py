import csv
import random
from pathlib import Path


# ---------------------------------------------------------
# 1. Reproducibility and project settings
# ---------------------------------------------------------

random.seed(42)

NUM_PARTICIPANTS = 1000

BIRTH_YEAR_MIN = 1950
BIRTH_YEAR_MAX = 2020

SAMPLE_YEARS = [2005, 2010, 2015, 2020, 2025]

ENTEROVIRUS_TYPES = [
    "EV-A71",
    "EV-D68",
    "CVA6",
    "CVA16"
]


# ---------------------------------------------------------
# 2. Synthetic antibody titre scale
# ---------------------------------------------------------

ANTIBODY_TITRES = [
    8,
    16,
    32,
    64,
    128,
    256,
    512
]


# ---------------------------------------------------------
# 3. Synthetic antibody-generation function
# ---------------------------------------------------------

def generate_antibody_titre(
    age,
    birth_year,
    sample_year,
    virus_type
):
    """
    Generate a synthetic antibody titre.

    This is a synthetic modelling rule created for
    methodological demonstration.

    It does not represent real laboratory measurements,
    Finnish DIPP data, or validated clinical thresholds.
    """

    score = 2.5

    # Age-related synthetic variation
    if age <= 4:
        score -= 0.9

    elif age <= 9:
        score -= 0.4

    elif age <= 14:
        score += 0.0

    elif age <= 19:
        score += 0.15

    elif age <= 39:
        score += 0.25

    elif age <= 59:
        score += 0.10

    else:
        score -= 0.05

    # Birth-cohort variation
    if birth_year < 1970:
        score += 0.10

    elif birth_year < 1990:
        score += 0.00

    elif birth_year < 2005:
        score -= 0.20

    elif birth_year < 2015:
        score -= 0.35

    else:
        score -= 0.50

    # Calendar-year variation
    year_effect = {
        2005: -0.30,
        2010: -0.50,
        2015: 0.10,
        2020: 0.20,
        2025: 0.00
    }

    score += year_effect[sample_year]

    # Synthetic virus-type variation
    virus_effect = {
        "EV-A71": 0.10,
        "EV-D68": -0.30,
        "CVA6": 0.05,
        "CVA16": -0.20
    }

    score += virus_effect[virus_type]

    # Individual-level random variation
    score += random.gauss(0, 1.3)

    # Convert score into one of the available titre categories
    score = round(score)

    score = max(
        0,
        min(score, len(ANTIBODY_TITRES) - 1)
    )

    return ANTIBODY_TITRES[score]


# ---------------------------------------------------------
# 4. Generate synthetic participants
# ---------------------------------------------------------

participants = []

for i in range(1, NUM_PARTICIPANTS + 1):

    participant = {
        "participant_id": f"P{i:04d}",
        "birth_year": random.randint(
            BIRTH_YEAR_MIN,
            BIRTH_YEAR_MAX
        )
    }

    participants.append(participant)


# ---------------------------------------------------------
# 5. Generate longitudinal sampling records
# ---------------------------------------------------------

records = []

for participant in participants:

    birth_year = participant["birth_year"]

    for sample_year in SAMPLE_YEARS:

        # Never sample an individual before birth
        if sample_year < birth_year:
            continue

        # Calculate age at sampling
        age = sample_year - birth_year

        # Assign age group
        if age <= 4:
            age_group = "0-4"

        elif age <= 9:
            age_group = "5-9"

        elif age <= 14:
            age_group = "10-14"

        elif age <= 19:
            age_group = "15-19"

        elif age <= 39:
            age_group = "20-39"

        elif age <= 59:
            age_group = "40-59"

        else:
            age_group = "60+"

        # Create one observation for every virus type
        for virus_type in ENTEROVIRUS_TYPES:

            antibody_titre = generate_antibody_titre(
                age,
                birth_year,
                sample_year,
                virus_type
            )

            # -------------------------------------------------
            # Synthetic immunity classification
            #
            # These are modelling assumptions only.
            # They are NOT clinical thresholds.
            # -------------------------------------------------

            if antibody_titre < 32:

                antibody_positive = 0
                immunity_level = "Susceptible"
                susceptibility_fraction = 1.00

            elif antibody_titre < 64:

                antibody_positive = 1
                immunity_level = "Partially protected"
                susceptibility_fraction = 0.50

            else:

                antibody_positive = 1
                immunity_level = "Protected"
                susceptibility_fraction = 0.10

            record = {
                "participant_id": participant["participant_id"],
                "birth_year": birth_year,
                "sample_year": sample_year,
                "age": age,
                "age_group": age_group,
                "enterovirus_type": virus_type,
                "neutralizing_ab_titer": antibody_titre,
                "antibody_positive": antibody_positive,
                "immunity_level": immunity_level,
                "susceptibility_fraction": susceptibility_fraction
            }

            records.append(record)


# ---------------------------------------------------------
# 6. Define output file
# ---------------------------------------------------------

output_file = (
    Path("..")
    / "03_Data"
    / "synthetic_enterovirus_immunity.csv"
)


# ---------------------------------------------------------
# 7. Define CSV columns
# ---------------------------------------------------------

fieldnames = [
    "participant_id",
    "birth_year",
    "sample_year",
    "age",
    "age_group",
    "enterovirus_type",
    "neutralizing_ab_titer",
    "antibody_positive",
    "immunity_level",
    "susceptibility_fraction"
]


# ---------------------------------------------------------
# 8. Write CSV file
# ---------------------------------------------------------

with output_file.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(records)


# ---------------------------------------------------------
# 9. Print confirmation
# ---------------------------------------------------------

print("Synthetic records created:", len(records))

print(
    "Dataset saved to:",
    output_file.resolve()
)