# Respiratory Outbreak Simulator

## Python-Based Computational Epidemiology and Population-Immunity Modelling Project

An independent computational public-health modelling project developed to investigate infectious disease transmission, intervention scenarios, parameter uncertainty, population immunity and epidemic-emergence thresholds using Python.

---

## Research Question

How do model structure, intervention assumptions, population immunity patterns and uncertainty in epidemiological parameters influence simulated disease transmission and epidemic-emergence dynamics?

---

## Project Overview

The project began with deterministic SIR and SEIR compartmental epidemic models and was progressively extended to include:

- Public-health intervention scenarios
- Parameter sensitivity analysis
- Monte Carlo uncertainty analysis
- Computational validation
- Synthetic longitudinal population-immunity data
- Age-group analysis
- Birth-cohort analysis
- Calendar-time analysis
- Enterovirus-type analysis
- Population susceptibility estimation
- Immunity-adjusted SEIR modelling
- Effective reproduction number analysis
- Epidemic-emergence threshold analysis

The project is designed as a reproducible computational research portfolio rather than a real-world forecasting system.

---

## Models

### SIR

Susceptible → Infectious → Recovered/Removed

### SEIR

Susceptible → Exposed → Infectious → Recovered/Removed

The SEIR model introduces an exposed compartment controlled by the parameter σ.

---

## Baseline Parameters

- Population = 5,000
- Initial infectious population = 10
- β = 0.30
- γ = 0.20
- σ = 1.11
- Simulation period = 180 days

The baseline R₀ under the simplified SIR formulation is:

R₀ = β / γ = 1.5

The β and γ values are illustrative modelling assumptions. The σ value is treated as an evidence-informed modelling input rather than a universal biological constant.

---

## Intervention Modelling

The project includes:

1. Baseline
2. Vaccination
3. Transmission reduction
4. Combined intervention

The intervention assumptions are methodological demonstrations and should not be interpreted as empirical estimates of real-world intervention effectiveness.

---

## Sensitivity and Uncertainty

The project includes:

- One-way β sensitivity analysis
- One-way γ sensitivity analysis
- 1,000-run Monte Carlo uncertainty analysis
- Reproducible random seed

Monte Carlo results are reported as model-based percentile ranges rather than statistical confidence intervals.

---

## Population-Immunity Extension

A synthetic longitudinal-style dataset was generated to investigate how population immunity could be represented computationally.

The dataset includes:

- Synthetic participant identifiers
- Birth year
- Sampling year
- Age and age group
- Birth cohort
- Synthetic enterovirus-type labels
- Synthetic neutralizing antibody titres
- Synthetic immunity classification
- Susceptibility fraction

The synthetic data are **not real patient data**, not Finnish DIPP data and not clinical serological measurements.

---

## Immunity Analysis

Synthetic immunity was analysed by:

- Age group
- Birth cohort
- Calendar year
- Enterovirus type

The analysis then derived mean population susceptibility by calendar year and enterovirus type.

This creates the computational link:

Synthetic immunity → susceptibility → epidemic modelling

---

## Immunity-Adjusted SEIR

Synthetic population susceptibility was incorporated into an additional SEIR framework.

The analysis investigates how different susceptibility levels influence:

- Effective reproduction number
- Initial epidemic growth
- Peak infectious population
- Timing of the epidemic peak
- Cumulative simulated infections

---

## Epidemic-Emergence Threshold

Under the illustrative model parameters:

R₀ = 1.5

The critical susceptible fraction is approximately:

1 / R₀ = 66.7%

The project therefore evaluates the transition between:

- R_eff < 1 — no initial epidemic growth
- R_eff = 1 — threshold condition
- R_eff > 1 — potential initial epidemic growth

This is a model-derived threshold and has not been empirically validated against real epidemic data.

---

## Model Validation

Computational checks include:

- Initial condition verification
- Population conservation
- Non-negative compartments
- Expected compartment trajectories
- Reproducibility checks

These checks represent computational consistency rather than empirical validation.

---

## Repository Structure

```text
01_Project_Documentation/
02_Code/
03_Data/
04_Results/
05_Report/
README.md
