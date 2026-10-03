import csv
from pathlib import Path
input_file = (
    Path("..")
    / "03_Data"
    / "synthetic_enterovirus_immunity.csv"
)

records = []

with input_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        records.append(row)
print("Records loaded:", len(records))
print("First record:", records[0])
immunity_counts = {}

for row in records:
    level = row["immunity_level"]

    if level not in immunity_counts:
        immunity_counts[level] = 0

    immunity_counts[level] += 1

print("\nImmunity level counts:")

for level, count in immunity_counts.items():
    print(level, ":", count)
total_records = len(records)

print("\nImmunity level percentages:")

for level, count in immunity_counts.items():
    percentage = (count / total_records) * 100
    print(
        level,
        ":",
        round(percentage, 2),
        "%"
    )
age_group_counts = {}

for row in records:
    age_group = row["age_group"]

    if age_group not in age_group_counts:
        age_group_counts[age_group] = {
            "total": 0,
            "protected": 0
        }

    age_group_counts[age_group]["total"] += 1

    if row["immunity_level"] == "Protected":
        age_group_counts[age_group]["protected"] += 1


print("\nProtected proportion by age group:")

for age_group, values in age_group_counts.items():

    proportion = (
        values["protected"] /
        values["total"]
    ) * 100

    print(
        age_group,
        ":",
        round(proportion, 2),
        "%"
    )
virus_counts = {}

for row in records:
    virus_type = row["enterovirus_type"]

    if virus_type not in virus_counts:
        virus_counts[virus_type] = {
            "total": 0,
            "protected": 0
        }

    virus_counts[virus_type]["total"] += 1

    if row["immunity_level"] == "Protected":
        virus_counts[virus_type]["protected"] += 1


print("\nProtected proportion by enterovirus type:")

for virus_type, values in virus_counts.items():

    proportion = (
        values["protected"] /
        values["total"]
    ) * 100

    print(
        virus_type,
        ":",
        round(proportion, 2),
        "%"
    )
year_counts = {}

for row in records:
    sample_year = row["sample_year"]

    if sample_year not in year_counts:
        year_counts[sample_year] = {
            "total": 0,
            "protected": 0
        }

    year_counts[sample_year]["total"] += 1

    if row["immunity_level"] == "Protected":
        year_counts[sample_year]["protected"] += 1


print("\nProtected proportion by sampling year:")

for sample_year in sorted(year_counts):

    values = year_counts[sample_year]

    proportion = (
        values["protected"] /
        values["total"]
    ) * 100

    print(
        sample_year,
        ":",
        round(proportion, 2),
        "%"
    )
# ---------------------------------------------------------
# Save summary results as CSV files
# ---------------------------------------------------------

results_folder = Path("..") / "04_Results"
results_folder.mkdir(exist_ok=True)


# ---------------------------------------------------------
# 1. Immunity by age group
# ---------------------------------------------------------

age_output = results_folder / "immunity_by_age_group.csv"

with age_output.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "age_group",
        "total_records",
        "protected_records",
        "protected_percentage"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for age_group in sorted(age_group_counts):

        values = age_group_counts[age_group]

        percentage = (
            values["protected"]
            / values["total"]
        ) * 100

        writer.writerow({
            "age_group": age_group,
            "total_records": values["total"],
            "protected_records": values["protected"],
            "protected_percentage": round(
                percentage,
                2
            )
        })


# ---------------------------------------------------------
# 2. Immunity by enterovirus type
# ---------------------------------------------------------

virus_output = results_folder / "immunity_by_virus_type.csv"

with virus_output.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "enterovirus_type",
        "total_records",
        "protected_records",
        "protected_percentage"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for virus_type in sorted(virus_counts):

        values = virus_counts[virus_type]

        percentage = (
            values["protected"]
            / values["total"]
        ) * 100

        writer.writerow({
            "enterovirus_type": virus_type,
            "total_records": values["total"],
            "protected_records": values["protected"],
            "protected_percentage": round(
                percentage,
                2
            )
        })


# ---------------------------------------------------------
# 3. Immunity by sampling year
# ---------------------------------------------------------

year_output = results_folder / "immunity_by_year.csv"

with year_output.open(
    "w",
    newline="",
    encoding="utf-8"
) as file:

    fieldnames = [
        "sample_year",
        "total_records",
        "protected_records",
        "protected_percentage"
    ]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    for sample_year in sorted(year_counts):

        values = year_counts[sample_year]

        percentage = (
            values["protected"]
            / values["total"]
        ) * 100

        writer.writerow({
            "sample_year": sample_year,
            "total_records": values["total"],
            "protected_records": values["protected"],
            "protected_percentage": round(
                percentage,
                2
            )
        })


print("\nSummary files saved:")
print(age_output.resolve())
print(virus_output.resolve())
print(year_output.resolve())