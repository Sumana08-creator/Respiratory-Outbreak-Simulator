# Respiratory Outbreak Simulator

## 1. Background

Respiratory infectious diseases can spread through populations in waves, with the timing and size of an epidemic influenced by transmission, infectious duration, population susceptibility, intervention timing and model assumptions.

This project uses a synthetic population to demonstrate how compartmental epidemiological models can be implemented, analysed and compared using Python. The disease context for the extended model is seasonal influenza. Influenza is a contagious respiratory illness; current CDC guidance describes a typical incubation period of about 1–4 days and notes that infectiousness can begin before symptoms appear. [1]

This project is a computational learning and research-methodology exercise. The simulated results are not intended to forecast a real outbreak.

## 2. Research Question

How do model structure, intervention assumptions and uncertainty in epidemiological parameters influence simulated respiratory disease transmission and epidemic peak dynamics?

## 3. Objectives

The project aimed to:

1. Implement a deterministic SIR model in Python.
2. Extend the model to an SEIR structure.
3. Simulate epidemic trajectories over 180 days.
4. Examine illustrative public-health intervention scenarios.
5. Conduct one-way sensitivity analysis of the transmission and recovery parameters.
6. Conduct a 1,000-run Monte Carlo uncertainty analysis.
7. Validate the computational implementation.
8. Compare SIR and SEIR model structures.
9. Develop a reproducible computational portfolio suitable for GitHub and PhD applications.

## 4. Model Selection

### 4.1 SIR Model

The SIR model divides the synthetic population into three compartments:

- Susceptible (S)
- Infectious (I)
- Recovered/Removed (R)

The model structure is:

S → I → R

The discrete-time implementation used:

New infections = β × S × I / N

Recoveries = γ × I

where:

- β is the effective transmission parameter.
- γ is the recovery/removal rate.
- N is the total population.

The baseline population was 5,000, with 4,990 susceptible individuals, 10 infectious individuals and 0 recovered/removed individuals at the start.

### 4.2 SEIR Model

The SEIR extension introduced an exposed/latent compartment:

S → E → I → R

The additional parameter σ controls movement from exposed to infectious.

The transition equations were represented as:

New exposures = β × S × I / N

Progression from exposed to infectious = σ × E

Recoveries = γ × I

The SEIR structure was used to explore how explicitly representing a pre-infectious period changes the epidemic trajectory.

## 5. Model Parameters

### 5.1 Beta (β)

The baseline value was:

β = 0.30 per day

This value was selected as an illustrative teaching parameter rather than estimated from real surveillance data.

The basic SIR reproduction number under the baseline assumptions can be expressed as:

R₀ = β / γ

Using β = 0.30 and γ = 0.20 gives:

R₀ = 1.5

### 5.2 Gamma (γ)

The baseline value was:

γ = 0.20 per day

The corresponding mean infectious period under the simplified SIR formulation is:

1 / γ = 5 days

The β and γ values were deliberately selected as illustrative modelling assumptions so that parameter sensitivity could be demonstrated transparently.

### 5.3 Sigma (σ)

For the SEIR model:

σ = 1.11 per day

This corresponds to an assumed mean exposed-to-infectious transition time of approximately:

1 / σ ≈ 0.90 days

The 0.90-day value was treated as an evidence-informed modelling input based on a recent household influenza transmission study. That study estimated latent-period values that depended on assumptions about the incubation period; under its primary scenario, the reported latent period was approximately 0.9 days. The study also emphasised uncertainty around these estimates. [2]

Therefore, σ = 1.11 was used as an informed starting parameter rather than as a universal biological constant.

## 6. Model Assumptions

The main assumptions were:

- The simulated population contains 5,000 individuals.
- Individuals mix homogeneously.
- Population size remains constant over the simulation.
- Births, deaths and migration are not explicitly modelled.
- The baseline parameters remain constant within each scenario unless an intervention changes β.
- The baseline SIR model is deterministic.
- The vaccination scenario uses a simplified representation of protection.
- The intervention effects are illustrative rather than empirically estimated.
- The model is not calibrated to real surveillance data.
- No age, demographic, household or contact-network structure is explicitly represented.
- Healthcare capacity and clinical outcomes are not modelled.

These assumptions make the model computationally manageable but limit direct interpretation as a real-world forecasting system.

## 7. Computational Implementation

The project was implemented in Python.

The main code components include:

- `baseline_sir.py` — baseline SIR simulation
- `vaccination_scenario.py` — vaccination scenario
- `transmission_reduction.py` — transmission-reduction scenario
- `combined_intervention.py` — combined intervention scenario
- `compare_scenarios.py` — scenario comparison
- `sensitivity_beta.py` — β sensitivity analysis
- `sensitivity_gamma.py` — γ sensitivity analysis
- `monte_carlo.py` — Monte Carlo uncertainty analysis
- `validate_model.py` — computational validation checks
- `seir_model.py` — baseline SEIR simulation
- `seir_transmission_reduction.py` — SEIR intervention scenario
- `sir_vs_seir.py` — SIR versus SEIR comparison
- `final_model_comparison.py` — final cross-model comparison
- `final_analysis.py` — consolidated SIR scenario analysis

The workflow produces CSV result files and PNG visualisations in the `04_Results` directory.

## 8. Intervention Scenarios

### 8.1 Baseline

The baseline scenario used:

- Population = 5,000
- Initial infectious population = 10
- β = 0.30
- γ = 0.20
- Simulation period = 180 days

The baseline SIR simulation produced:

- Peak infectious population = 330.729
- Peak day = Day 52
- Final susceptible population ≈ 2,042.840
- Final infectious population ≈ 0.036
- Final recovered/removed population ≈ 2,957.124

The baseline scenario provides the reference trajectory against which the intervention scenarios were compared.

### 8.2 Vaccination

The illustrative vaccination scenario assumed:

- 40% population coverage
- 80% effectiveness

This produced:

40% × 80% = 32% effectively protected

For a population of 5,000:

5,000 × 0.32 = 1,600 effectively protected individuals

The simplified implementation placed these protected individuals into the removed/protected compartment at the start of the simulation.

Results:

- Peak infectious population = 10.494
- Peak day = Day 28
- Cumulative simulated infections ≈ 279.811

This is a simplified representation. A future model should use a dedicated vaccination compartment and explicitly model vaccine timing, waning and partial protection.

### 8.3 Transmission Reduction

The transmission-reduction scenario applied a 50% reduction in β from Day 30.

Therefore:

- β = 0.30 before Day 30
- β = 0.15 from Day 30

Results:

- Peak infectious population = 129.822
- Peak day = Day 29
- Cumulative simulated infections ≈ 665.939

The simulated peak occurred immediately before the intervention took effect, illustrating the importance of intervention timing.

### 8.4 Combined Intervention

The combined scenario applied the illustrative vaccination assumptions together with the 50% reduction in β from Day 30.

Results:

- Peak infectious population = 10.494
- Peak day = Day 28
- Cumulative simulated infections ≈ 80.822

The peak remained the same as the vaccination-only scenario because the transmission-reduction intervention began after the early peak, but the combined scenario further reduced infections later in the simulation.

## 9. Sensitivity Analysis

One-way sensitivity analysis was used to examine how changes in model parameters affected epidemic dynamics.

### 9.1 Beta Sensitivity

β was varied while γ remained fixed at 0.20.

| β | Peak infectious | Peak day | Cumulative simulated infections |
|---:|---:|---:|---:|
| 0.25 | 117.238 | 76 | 1,882.559 |
| 0.30 | 330.729 | 52 | 2,957.124 |
| 0.35 | 570.905 | 39 | 3,616.966 |

Higher β produced a larger and earlier epidemic peak in the simulations.

### 9.2 Gamma Sensitivity

γ was varied while β remained fixed at 0.30.

| γ | Mean infectious period | R₀ | Peak infectious | Peak day | Cumulative simulated infections |
|---:|---:|---:|---:|---:|---:|
| 0.15 | 6.67 days | 2.00 | 800.079 | 42 | 4,030.702 |
| 0.20 | 5.00 days | 1.50 | 330.729 | 52 | 2,957.124 |
| 0.25 | 4.00 days | 1.20 | 83.318 | 68 | 1,610.970 |

Lower γ corresponds to a longer infectious period and produced a larger simulated epidemic peak.

## 10. Monte Carlo Uncertainty Analysis

A Monte Carlo simulation was used to explore how uncertainty in β and γ affected the simulated epidemic peak.

The model ran 1,000 simulations.

Parameters were sampled from:

- β ~ Uniform(0.25, 0.35)
- γ ~ Uniform(0.15, 0.25)

A fixed random seed was used to make the simulation reproducible.

The resulting simulated peak distribution was:

| Summary measure | Simulated peak |
|---|---:|
| Minimum | 11.336 |
| 5th percentile | 46.476 |
| Median | 328.374 |
| 95th percentile | 838.264 |
| Maximum | 1,024.882 |

The 5th–95th percentile interval is a model-based uncertainty range under the specified parameter distributions. It is not a statistical confidence interval for a real population.

The analysis demonstrated that plausible variation in β and γ can produce substantial variation in epidemic peak size.

## 11. Model Validation

The baseline implementation included computational quality checks.

The validation script checked:

- Correct initial conditions
- Conservation of total population
- Absence of negative compartment values
- Decrease in the susceptible compartment
- Increase in the recovered/removed compartment

Validation results:

- Initial conditions correct = True
- Population conserved = True
- Maximum population error = 0.0
- Negative compartment values = 0
- Susceptible population decreased = True
- Recovered population increased = True
- Overall validation = PASSED

These checks demonstrate computational consistency of the implementation. They do not constitute empirical validation against real influenza surveillance data.

## 12. SIR vs SEIR Comparison

The baseline SIR and SEIR models were run using the same β and γ values.

| Model | Peak infectious | Peak day |
|---|---:|---:|
| SIR | 330.729 | 52 |
| SEIR | 279.054 | 64 |

The SEIR model produced a lower and later infectious peak.

The difference arises from the additional exposed compartment, which delays the movement of newly infected individuals into the infectious compartment.

The SEIR baseline results were:

- Final susceptible ≈ 2,048.235
- Final exposed ≈ 0.030
- Final infectious ≈ 0.251
- Final recovered ≈ 2,951.485

This comparison demonstrates that model structure itself can materially influence simulated epidemic dynamics.

## 13. Results

The principal SIR scenario results were:

| Scenario | Peak infectious | Peak day | Cumulative simulated infections |
|---|---:|---:|---:|
| Baseline | 330.729 | 52 | 2,957.124 |
| Vaccination | 10.494 | 28 | 279.811 |
| Transmission Reduction | 129.822 | 29 | 665.939 |
| Combined Intervention | 10.494 | 28 | 80.822 |

The cross-model intervention comparison was:

| Model | Scenario | Peak infectious | Peak day |
|---|---|---:|---:|
| SIR | Baseline | 330.729 | 52 |
| SIR | Transmission Reduction | 129.822 | 29 |
| SEIR | Baseline | 279.054 | 64 |
| SEIR | Transmission Reduction | 72.841 | 30 |

Under the model assumptions, the transmission-reduction scenario reduced the SIR peak by approximately 60.75% relative to the SIR baseline.

Under the SEIR assumptions, the same transmission-reduction scenario reduced the peak by approximately 73.90% relative to the SEIR baseline.

These percentages describe differences between the simulated scenarios and should not be interpreted as estimates of real-world intervention effectiveness.

## 14. Interpretation

The modelling exercise demonstrates several computational epidemiology principles.

First, transmission intensity matters substantially. Increasing β increased both epidemic peak size and the amount of simulated infection.

Second, the recovery/removal parameter influences the duration for which individuals remain infectious. A lower γ increased the mean infectious period and substantially increased the simulated epidemic peak.

Third, intervention timing matters. In the transmission-reduction scenario, the intervention began on Day 30 and the SIR peak occurred on Day 29, illustrating that changing transmission after the peak does not necessarily change the timing or size of the already established maximum in the same way as an earlier intervention.

Fourth, model structure matters. The addition of an exposed compartment in the SEIR model changed both the magnitude and timing of the epidemic peak.

Finally, parameter uncertainty can produce a wide range of simulated outcomes. The Monte Carlo analysis demonstrated that uncertainty in β and γ should be considered when interpreting deterministic model outputs.

## 15. Limitations

The project has several important limitations.

### Homogeneous mixing

All individuals are assumed to mix in the same way. Real populations have structured contacts influenced by households, schools, workplaces, geography and social networks.

### Synthetic population

The population of 5,000 is synthetic and does not represent a specific real community.

### Simplified disease dynamics

The SIR model does not include a latent/exposed stage. Even the SEIR model remains simplified compared with real influenza transmission.

### Illustrative parameters

The baseline β and γ values were selected for teaching and modelling demonstration rather than calibrated from real surveillance data.

### Simplified vaccination

Vaccination is represented using an initial protected group rather than a dedicated vaccinated compartment. Vaccine timing, waning and partial protection are not modelled dynamically.

### No demographic structure

Age-specific susceptibility, infectiousness, vaccination coverage and contact rates are not represented.

### No healthcare capacity

The model does not include hospital admissions, intensive care capacity, healthcare demand or resource constraints.

### No empirical calibration

The simulations were not fitted to observed influenza case counts or other surveillance data.

### Deterministic baseline

The main simulations are deterministic, so they do not directly represent random transmission events.

### Interpretation of cumulative infections

The cumulative infection quantities reported in this project are simulation-derived measures and should not be interpreted as precise estimates of real-world cumulative incidence.

## 16. Future Model Development

Potential extensions include:

1. Age-stratified SEIR modelling.
2. A dedicated vaccinated compartment.
3. Waning vaccine protection.
4. Stochastic transmission.
5. Household and workplace contact structures.
6. Contact-network modelling.
7. Agent-based modelling.
8. Evidence-based parameter calibration.
9. Integration with real-world influenza surveillance data.
10. Healthcare-capacity modelling.
11. Bayesian parameter uncertainty.
12. Time-varying transmission parameters based on observed interventions.

A particularly useful next step would be to develop an age-stratified SEIR model with separate vaccination compartments and calibrate selected parameters against a real surveillance dataset.

## 17. Reproducibility

The repository is organised into:

```text
01_Project_Documentation/
02_Code/
03_Data/
04_Results/
05_Report/
README.md
```

The `02_Code` directory contains the model, sensitivity, uncertainty, intervention and validation scripts.

The `04_Results` directory contains CSV outputs and visualisations generated from the simulations.

The `05_Report` directory contains this research report.

The project uses a fixed random seed for the Monte Carlo simulation so that the uncertainty analysis can be reproduced.

The workflow is designed to connect:

Model assumptions
→ Python implementation
→ Simulation
→ Validation
→ Sensitivity analysis
→ Monte Carlo uncertainty
→ Cross-model comparison
→ Interpretation

This structure supports transparent and reproducible computational research.

## 18. Conclusion

This project developed a Python-based computational framework for exploring respiratory infectious disease transmission using SIR and SEIR models.

The simulations demonstrated that changes in transmission, infectious duration, intervention timing, model structure and parameter uncertainty can substantially affect simulated epidemic dynamics.

The project also demonstrates practical skills in:

- Mathematical epidemiological modelling
- Python programming
- Simulation design
- Data handling
- Visualisation
- Sensitivity analysis
- Monte Carlo uncertainty analysis
- Computational validation
- Model comparison
- Reproducible research

The results should be interpreted as outputs of a synthetic methodological modelling exercise rather than forecasts of a real influenza outbreak.

## References

1. Centers for Disease Control and Prevention (CDC). **About Influenza (Flu)**. Updated February 26, 2026.

2. Chan, L. Y. H., Morris, S. E., Stockwell, M. S., Bowman, N. M., Asturias, E., Rao, S., Lutrick, K., Ellingson, K. D., Nguyen, H. Q., Maldonado, Y., McLaren, S. H., Sano, E., Biddle, J. E., Smith-Jeffcoat, S. E., Biggerstaff, M., Rolfes, M. A., Talbot, H. K., Grijalva, C. G., Borchering, R. K., Mellis, A. M., RVTN-Sentinel Study Group. **Estimating the generation time for influenza transmission using household data in the United States.** *Epidemics*. 2025;50:100815. doi:10.1016/j.epidem.2025.100815.
