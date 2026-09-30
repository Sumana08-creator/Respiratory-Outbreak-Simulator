\# Respiratory Outbreak Simulator



\## Python-Based SIR and SEIR Computational Epidemiology Project



An independent computational public-health modelling project developed to explore respiratory disease transmission, intervention scenarios, parameter sensitivity and model uncertainty using Python.



\---



\## Project Overview



This project implements deterministic compartmental epidemic models to simulate disease transmission over a 180-day period.



The project began with a basic:



SIR model



and was subsequently extended to:



SEIR



to examine how introducing an exposed/latent compartment changes the simulated epidemic trajectory.



The project also evaluates illustrative public-health intervention scenarios and explores uncertainty in model parameters using sensitivity analysis and Monte Carlo simulation.



\---



\## Research Question



How do model structure, intervention assumptions and uncertainty in epidemiological parameters influence simulated respiratory disease transmission and epidemic peak dynamics?



\---



\## Objectives



\- Implement a deterministic SIR model in Python.

\- Extend the model to an SEIR structure.

\- Simulate epidemic trajectories over 180 days.

\- Compare illustrative intervention scenarios.

\- Conduct sensitivity analysis of β and γ.

\- Conduct a 1,000-run Monte Carlo uncertainty analysis.

\- Validate the computational implementation.

\- Compare SIR and SEIR model structures.

\- Develop reproducible research outputs for GitHub.



\---



\## Models



\### SIR



The SIR model contains:



\- Susceptible (S)

\- Infectious (I)

\- Recovered/Removed (R)



Structure:



S → I → R



\### SEIR



The SEIR model adds an exposed/latent compartment:



S → E → I → R



The additional parameter σ controls the transition from exposed to infectious.



\---



\## Model Parameters



\### Baseline SIR



\- β = 0.30

\- γ = 0.20

\- Population = 5,000

\- Initial infectious population = 10

\- Simulation period = 180 days



\### SEIR



\- β = 0.30

\- γ = 0.20

\- σ = 1.11

\- Population = 5,000

\- Initial infectious population = 10

\- Simulation period = 180 days



The SEIR σ value was treated as an evidence-informed initial modelling parameter and as an uncertain quantity rather than a biological constant.



\---



\## Intervention Scenarios



The project explored illustrative scenarios including:



1\. Baseline

2\. Vaccination

3\. Transmission reduction

4\. Combined intervention



The transmission-reduction scenario introduced a 50% reduction in the effective transmission parameter from Day 30.



The vaccination scenario used an illustrative 40% coverage assumption with 80% effectiveness.



These intervention assumptions are methodological demonstrations and should not be interpreted as empirical estimates of real-world intervention effectiveness.



\---



\## Sensitivity Analysis



One-way sensitivity analysis examined the effect of varying:



\### β



\- 0.25

\- 0.30

\- 0.35



\### γ



\- 0.15

\- 0.20

\- 0.25



The analysis examined changes in:



\- Peak infectious population

\- Timing of epidemic peak

\- Cumulative simulated infections



\---



\## Monte Carlo Uncertainty Analysis



A 1,000-run Monte Carlo simulation randomly sampled:



\- β between 0.25 and 0.35

\- γ between 0.15 and 0.25



The resulting simulated peak infectious populations were summarised using:



\- Minimum

\- 5th percentile

\- Median

\- 95th percentile

\- Maximum



The resulting uncertainty distribution demonstrated substantial variation in epidemic peak size under parameter uncertainty.



\---



\## Model Validation



Computational validation checks included:



\- Initial condition verification

\- Population conservation

\- Non-negative compartment values

\- Expected susceptible decline

\- Expected recovered/removed increase



The baseline implementation passed all programmed validation checks.



This represents computational consistency checking rather than empirical validation against real-world surveillance data.



\---



\## Key Results



\### Baseline SIR



\- Peak infectious population: 330.729

\- Peak day: 52



\### Baseline SEIR



\- Peak infectious population: 279.054

\- Peak day: 64



\### SIR vs SEIR



The SEIR model produced a lower and later simulated infectious peak under the same β and γ assumptions.



\### Monte Carlo analysis



Across 1,000 simulations:



\- 5th percentile: 46.476

\- Median: 328.374

\- 95th percentile: 838.264



\---



\## Limitations



This project is a methodological computational modelling exercise.



Important limitations include:



\- Homogeneous mixing assumption

\- Simplified compartment structure

\- No age or demographic structure

\- No explicit healthcare-capacity modelling

\- No empirical calibration to surveillance data

\- Simplified intervention representations

\- Deterministic baseline model

\- Illustrative parameter assumptions



The simulated outputs should therefore not be interpreted as forecasts of a real-world outbreak.



\---



\## Future Development



Potential extensions include:



\- Age-stratified SEIR modelling

\- Stochastic transmission

\- Separate vaccination compartments

\- Contact-network modelling

\- Agent-based modelling

\- Evidence-based parameter calibration

\- Real-world epidemiological dataset integration

\- Healthcare-capacity modelling

\- Bayesian uncertainty analysis



\---



\## Tools



\- Python

\- NumPy

\- Matplotlib

\- CSV data processing

\- Excel for dataset inspection



\---



\## Reproducibility



The project stores:



\- Model code

\- Simulation outputs

\- CSV datasets

\- Visualisations

\- Documentation

\- Validation scripts



The repository is structured so that the computational workflow can be followed from model assumptions through simulation and analysis.



\---



\## Academic Purpose



This project was developed independently to build practical understanding of:



\- Computational epidemiology

\- Mathematical modelling

\- Python-based simulation

\- Sensitivity analysis

\- Monte Carlo uncertainty

\- Model validation

\- Public-health intervention modelling

\- Reproducible computational research



It is intended as a learning and research-methodology portfolio project rather than a validated epidemiological forecasting system.

