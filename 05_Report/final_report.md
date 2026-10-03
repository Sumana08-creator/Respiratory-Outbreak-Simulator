# Respiratory Outbreak Simulator

## Python-Based SIR, SEIR and Population-Immunity Computational Epidemiology Project

An independent computational public-health modelling project developed to explore respiratory disease transmission, public-health interventions, parameter sensitivity, uncertainty, population immunity and epidemic-emergence thresholds using Python.

\---

## 1\. Background

Respiratory and other infectious diseases can spread through populations in waves, with epidemic dynamics influenced by transmission intensity, duration of infectiousness, population susceptibility, immunity patterns and intervention timing.

This project began as a deterministic compartmental modelling exercise using SIR and SEIR models. It was subsequently extended to include a synthetic longitudinal population-immunity dataset and an immunity-adjusted SEIR framework.

The extended modelling context uses synthetic enterovirus-type categories to investigate how variation in population susceptibility could influence simulated epidemic dynamics. All immunity observations, antibody titres and susceptibility values introduced in this extension are synthetic modelling data. They are not Finnish DIPP study measurements and are not intended to represent real serological estimates.

The project is a computational learning and research-methodology exercise rather than a validated real-world forecasting system.

## 2\. Research Question

How do model structure, intervention assumptions, population immunity patterns and uncertainty in epidemiological parameters influence simulated respiratory disease transmission and epidemic-emergence dynamics?

## 3\. Objectives

The project aimed to:

1. Implement a deterministic SIR model in Python.
2. Extend the model to an SEIR structure.
3. Simulate epidemic trajectories over 180 days.
4. Compare illustrative public-health intervention scenarios.
5. Conduct sensitivity analysis of beta and gamma.
6. Conduct a 1,000-run Monte Carlo uncertainty analysis.
7. Validate the computational implementation.
8. Compare SIR and SEIR model structures.
9. Generate a reproducible synthetic population-immunity dataset.
10. Analyse synthetic immunity by age group, birth cohort, calendar year and enterovirus type.
11. Derive population susceptibility measures from the synthetic immunity data.
12. Integrate synthetic susceptibility into an immunity-adjusted SEIR model.
13. Examine the relationship between susceptibility and the effective reproduction number.
14. Identify a model-based susceptibility threshold for initial epidemic growth.
15. Build a reproducible GitHub portfolio demonstrating computational epidemiology and quantitative research skills.

## 4\. Model Selection

### 4.1 SIR Model

The SIR model divides the population into:

* Susceptible (S)
* Infectious (I)
* Recovered/Removed (R)

Structure:

S → I → R

The model uses:

New infections = beta × S × I / N

Recoveries = gamma × I

where beta is the transmission parameter, gamma is the recovery/removal rate and N is the total population.

The baseline population contains 5,000 synthetic individuals, with 4,990 susceptible, 10 infectious and 0 recovered/removed at the start.

### 4.2 SEIR Model

The SEIR model adds an exposed compartment:

S → E → I → R

The additional parameter sigma controls the transition from exposed to infectious.

The model uses:

New exposures = beta × S × I / N

Progression to infectious = sigma × E

Recoveries = gamma × I

The SEIR framework was used to investigate how explicitly representing an exposed period changes the timing and magnitude of the infectious epidemic peak.

## 5\. Model Parameters

### 5.1 Beta

The baseline transmission parameter was:

beta = 0.30 per day

This was selected as an illustrative teaching parameter rather than estimated from real surveillance data.

### 5.2 Gamma

The baseline recovery/removal parameter was:

gamma = 0.20 per day

The corresponding simplified mean infectious period is:

1 / gamma = 5 days

### 5.3 Sigma

The baseline SEIR parameter was:

sigma = 1.11 per day

This corresponds to an assumed mean exposed-to-infectious transition time of approximately 0.90 days.

The value was treated as an evidence-informed modelling input rather than a universal biological constant.

### 5.4 Basic Reproduction Number

For the baseline SIR/SEIR parameterisation:

R0 = beta / gamma = 0.30 / 0.20 = 1.5

The R0 value is model-derived and should not be interpreted as an empirical estimate for a specific enterovirus or real population.

## 6\. Model Assumptions

The main assumptions are:

* The core synthetic population contains 5,000 individuals.
* Individuals mix homogeneously.
* Population size remains constant over the simulation.
* Births, deaths and migration are not explicitly represented.
* Baseline parameters remain constant within a scenario unless an intervention changes transmission.
* Baseline SIR and SEIR simulations are deterministic.
* The vaccination intervention uses a simplified representation.
* Intervention effects are illustrative.
* No age, household, geographic or contact-network structure is explicitly represented in the core epidemic model.
* Healthcare capacity and clinical outcomes are not modelled.
* The population-immunity extension uses synthetic observations rather than real serological measurements.
* Synthetic antibody titres and immunity thresholds are methodological assumptions.
* The immunity-adjusted SEIR model uses mean synthetic susceptibility as an initial-condition input.
* The epidemic-emergence indicator is a model-based threshold measure, not a validated real-world prediction.

## 7\. Computational Implementation

The project was implemented in Python.

Core modelling scripts include:

* `baseline\_sir.py`
* `vaccination\_scenario.py`
* `transmission\_reduction.py`
* `combined\_intervention.py`
* `compare\_scenarios.py`
* `sensitivity\_beta.py`
* `sensitivity\_gamma.py`
* `monte\_carlo.py`
* `validate\_model.py`
* `seir\_model.py`
* `seir\_transmission\_reduction.py`
* `sir\_vs\_seir.py`
* `final\_model\_comparison.py`
* `final\_analysis.py`

Population-immunity and epidemic-emergence scripts include:

* `generate\_synthetic\_immunity\_data.py`
* `analyse\_synthetic\_immunity.py`
* `plot\_immunity\_patterns.py`
* `immunity\_adjusted\_seir.py`
* `epidemic\_risk\_analysis.py`
* `immunity\_threshold\_analysis.py`

CSV results and visualisations are stored in `04\_Results`.

## 8\. Baseline SIR Simulation

The baseline SIR simulation used:

* Population = 5,000
* Initial infectious = 10
* beta = 0.30
* gamma = 0.20
* Simulation period = 180 days

The simulated epidemic reached:

* Peak infectious population = 330.729
* Peak day = Day 52

By Day 180:

* Susceptible ≈ 2,042.840
* Infectious ≈ 0.036
* Recovered/Removed ≈ 2,957.124

These are model outputs under illustrative assumptions.

## 9\. Intervention Scenarios

### 9.1 Baseline

No intervention.

### 9.2 Vaccination

The illustrative vaccination scenario assumed:

* Coverage = 40%
* Effectiveness = 80%

Effective protected population:

5,000 × 0.40 × 0.80 = 1,600

Results:

* Peak infectious = 10.494
* Peak day = Day 28
* Cumulative simulated infections ≈ 279.811

The implementation is deliberately simplified and does not include a dedicated vaccinated compartment.

### 9.3 Transmission Reduction

A 50% reduction in beta was introduced from Day 30:

beta = 0.30 before Day 30

beta = 0.15 from Day 30

Results:

* Peak infectious = 129.822
* Peak day = Day 29
* Cumulative simulated infections ≈ 665.939

### 9.4 Combined Intervention

The combined scenario applied the illustrative vaccination assumptions and a 50% transmission reduction from Day 30.

Results:

* Peak infectious = 10.494
* Peak day = Day 28
* Cumulative simulated infections ≈ 80.822

## 10\. Sensitivity Analysis

### 10.1 Beta Sensitivity

With gamma fixed at 0.20:

|beta|Peak infectious|Peak day|Cumulative simulated infections|
|-:|-:|-:|-:|
|0.25|117.238|76|1,882.559|
|0.30|330.729|52|2,957.124|
|0.35|570.905|39|3,616.966|

Increasing beta increased epidemic peak size and shifted the peak earlier.

### 10.2 Gamma Sensitivity

With beta fixed at 0.30:

|gamma|Mean infectious period|R0|Peak infectious|Peak day|Cumulative simulated infections|
|-:|-:|-:|-:|-:|-:|
|0.15|6.67 days|2.00|800.079|42|4,030.702|
|0.20|5.00 days|1.50|330.729|52|2,957.124|
|0.25|4.00 days|1.20|83.318|68|1,610.970|

Lower gamma, corresponding to a longer infectious period, increased simulated epidemic size.

## 11\. Monte Carlo Uncertainty Analysis

A 1,000-run Monte Carlo simulation sampled:

* beta uniformly between 0.25 and 0.35
* gamma uniformly between 0.15 and 0.25

A fixed random seed was used for reproducibility.

Simulated epidemic peaks were:

|Summary measure|Peak infectious|
|-|-:|
|Minimum|11.336|
|5th percentile|46.476|
|Median|328.374|
|95th percentile|838.264|
|Maximum|1,024.882|

The 5th–95th percentile interval is a model-based uncertainty range under the specified parameter distributions. It is not a statistical confidence interval for a real population.

## 12\. Model Validation

The computational validation script checked:

* Initial conditions
* Population conservation
* Negative values
* Expected susceptible decline
* Expected recovered increase

Validation results:

* Initial conditions correct = True
* Population conserved = True
* Maximum population error = 0.0
* Negative compartment values = 0
* Susceptible population decreased = True
* Recovered population increased = True
* Overall validation = PASSED

These checks demonstrate computational consistency. They do not constitute empirical validation against observed enterovirus or influenza surveillance data.

## 13\. SIR versus SEIR Comparison

The baseline SIR model produced:

* Peak infectious = 330.729
* Peak day = 52

The baseline SEIR model produced:

* Peak infectious = 279.054
* Peak day = 64

The SEIR model therefore produced a lower and later simulated infectious peak under the same beta and gamma assumptions.

This illustrates the effect of model structure: explicitly representing an exposed compartment changes the timing and magnitude of the simulated infectious trajectory.

# Population-Immunity Extension

## 14\. Synthetic Population-Immunity Dataset

The project was extended with a reproducible synthetic longitudinal-style immunity dataset.

The dataset contains:

* 1,000 synthetic participant identifiers
* Birth years from 1950 to 2020
* Sampling years: 2005, 2010, 2015, 2020 and 2025
* Four synthetic enterovirus-type labels: EV-A71, EV-D68, CVA6 and CVA16
* Age
* Age group
* Birth cohort
* Synthetic neutralizing antibody titre
* Synthetic antibody-positive status
* Synthetic immunity classification
* Susceptibility fraction

The generated dataset contains 18,232 observations.

The data are deliberately synthetic. They do not represent actual patient records, Finnish DIPP samples or validated laboratory measurements.

## 15\. Synthetic Antibody and Immunity Rules

Synthetic antibody titres were generated on a discrete scale:

8, 16, 32, 64, 128, 256 and 512.

The generator introduces controlled variation according to:

* Age
* Birth year
* Sampling year
* Synthetic enterovirus type
* Individual-level random variation

A fixed random seed of 42 was used for reproducibility.

The synthetic classification rules were:

|Synthetic titre|Model classification|Susceptibility fraction|
|-:|-|-:|
|<32|Susceptible|1.00|
|32–63|Partially protected|0.50|
|>=64|Protected|0.10|

These thresholds are computational assumptions created for this project. They are not clinical antibody thresholds.

## 16\. Population-Immunity Analysis

The synthetic dataset was analysed by age group, birth cohort, calendar year and enterovirus type.

### 16.1 Overall Synthetic Immunity Distribution

|Synthetic immunity level|Percentage|
|-|-:|
|Protected|44.37%|
|Partially protected|26.68%|
|Susceptible|28.94%|

### 16.2 Protected Records by Age Group

|Age group|Protected|
|-|-:|
|0–4|13.52%|
|5–9|24.93%|
|10–14|37.06%|
|15–19|43.30%|
|20–39|50.30%|
|40–59|49.81%|
|60+|52.32%|

These values are synthetic and demonstrate age-stratified variation in the modelling dataset.

### 16.3 Protected Records by Enterovirus Type

|Type|Protected|
|-|-:|
|EV-A71|50.33%|
|EV-D68|38.94%|
|CVA6|47.61%|
|CVA16|40.61%|

These differences are synthetic model-generated patterns rather than biological findings.

### 16.4 Protected Records by Sampling Year

|Sampling year|Protected|
|-:|-:|
|2005|38.50%|
|2010|32.79%|
|2015|49.67%|
|2020|52.12%|
|2025|46.25%|

Because the dataset includes repeated participants, different ages and multiple enterovirus types, these percentages describe the synthetic record set rather than direct estimates of population prevalence.

### 16.5 Protected Records by Birth Cohort

|Birth cohort|Protected|
|-|-:|
|1950–1959|48.26%|
|1960–1969|51.10%|
|1970–1979|49.77%|
|1980–1989|51.29%|
|1990–1999|42.54%|
|2000–2009|33.79%|
|2010–2019|25.88%|
|2020|18.75%|

The birth-cohort analysis demonstrates that the synthetic framework can represent variation across cohorts and provides a methodological basis for investigating immunity gaps.

## 17\. Population Susceptibility

The individual-level synthetic susceptibility fractions were aggregated by sampling year and enterovirus type.

The resulting file, `population\_susceptibility\_by\_year\_type.csv`, provides the bridge between the immunity dataset and the epidemic model.

Conceptually:

Synthetic antibody data

→ immunity classification

→ susceptibility fraction

→ mean population susceptibility

→ SEIR initial conditions

This integration allows population-immunity assumptions to influence simulated transmission dynamics.

## 18\. Immunity-Adjusted SEIR Model

An additional SEIR model was implemented using the synthetic mean susceptibility for each year and enterovirus type.

The model uses:

* beta = 0.30
* gamma = 0.20
* sigma = 1.11
* Population = 5,000
* Initial infectious population = 10
* Simulation period = 180 days

The synthetic mean susceptibility determines the initial susceptible population.

Under the examined synthetic 2025 profiles, effective reproduction remained below the epidemic-growth threshold, resulting in an infectious peak at the initial Day 0 level in the corresponding simulations.

This demonstrates that the synthetic susceptibility profile can suppress epidemic growth under the selected beta and gamma assumptions.

## 19\. Epidemic-Emergence Analysis

The baseline reproduction number is:

R0 = beta / gamma

R0 = 0.30 / 0.20 = 1.5

A simple model-derived effective reproduction indicator was calculated as:

R\_eff = R0 × susceptible fraction

The critical susceptibility threshold is therefore:

1 / R0 = 1 / 1.5 ≈ 0.667

or approximately 66.7% susceptible.

Under this simplified model:

* Susceptible fraction below 66.7% → R\_eff < 1
* Susceptible fraction of approximately 66.7% → threshold condition
* Susceptible fraction above 66.7% → R\_eff > 1

This is a deterministic model threshold and should not be interpreted as a validated real-world epidemic-risk threshold.

## 20\. Susceptibility Threshold Analysis

A separate threshold analysis tested susceptible fractions from 10% to 90%.

The analysis demonstrated the transition around the theoretical threshold.

Examples from the SEIR simulations include:

|Susceptible fraction|R\_eff|Peak infectious|Peak day|
|-:|-:|-:|-:|
|70%|1.05|11.935|32|
|80%|1.20|59.051|49|
|90%|1.35|152.023|46|

The results demonstrate that increasing susceptibility beyond the threshold changes the simulated system from declining transmission to potential initial epidemic growth.

The threshold graph is stored as `immunity\_threshold\_analysis.png` and the full scenario table is stored as `immunity\_threshold\_analysis.csv`.

## 21\. Integrated Computational Workflow

The extended project now follows this workflow:

Synthetic population

→ Synthetic longitudinal immunity data

→ Age / birth cohort / year / virus-type analysis

→ Individual susceptibility fractions

→ Population susceptibility

→ Immunity-adjusted SEIR

→ Effective reproduction indicator

→ Epidemic-emergence threshold

→ Simulated epidemic dynamics

This creates a continuous computational chain from a population-immunity construct to epidemic-dynamics analysis.

## 22\. Interpretation

Several computational findings emerge from the integrated project.

First, the original SIR and SEIR analyses demonstrate that transmission and infectious duration materially affect simulated epidemic dynamics.

Second, the synthetic immunity extension demonstrates how population susceptibility can be represented from individual-level synthetic observations and aggregated by age, cohort, calendar time and virus type.

Third, the immunity-adjusted SEIR analysis shows that sufficiently low susceptibility can prevent initial epidemic growth under the selected illustrative beta and gamma values.

Fourth, the threshold analysis demonstrates that epidemic growth is highly dependent on the proportion of the population that remains susceptible. Under the model parameters used here, approximately 66.7% susceptibility marks the R\_eff = 1 threshold.

Fifth, the framework demonstrates how immunity information can become an input to an epidemic model rather than remaining a descriptive dataset.

These findings are methodological demonstrations. They do not constitute forecasts of enterovirus circulation or epidemic risk in Finland.

## 23\. Limitations

### Synthetic immunity data

The immunity dataset is synthetic and therefore cannot establish real epidemiological associations.

### No real DIPP data

The project does not use the Finnish DIPP longitudinal serum collection or real neutralizing antibody measurements.

### Synthetic antibody thresholds

The titre categories and immunity thresholds were defined for computational demonstration and are not clinical cut-offs.

### Simplified susceptibility representation

Each synthetic record is assigned a fixed susceptibility fraction based on its synthetic immunity category.

### Repeated observations

Participants can contribute multiple observations across years and multiple virus types. Record-level percentages should therefore not be interpreted as direct estimates of population prevalence.

### Simplified epidemic model

The immunity-adjusted SEIR model represents population susceptibility through an initial condition rather than modelling dynamic immune acquisition, waning or reinfection.

### No contact structure

The model assumes homogeneous mixing.

### No vaccination dynamics

The extended enterovirus model does not include vaccine-induced immunity as a separate dynamic compartment.

### No real surveillance integration

Healthcare surveillance, wastewater measurements and laboratory surveillance are not yet integrated.

### No predictive validation

The epidemic-emergence indicator has not been validated against observed historical epidemic events.

### Parameter uncertainty

The beta, gamma and sigma values are illustrative or evidence-informed modelling inputs rather than calibrated enterovirus-specific estimates.

## 24\. Future Model Development

The next logical extensions include:

1. Integrating real or openly available epidemiological surveillance data.
2. Developing an age-stratified SEIR model.
3. Modelling dynamic immunity acquisition and waning.
4. Representing antibody titre as a continuous rather than categorical exposure.
5. Including a more explicit relationship between antibody level and susceptibility.
6. Adding stochastic transmission.
7. Integrating synthetic or real wastewater indicators.
8. Integrating healthcare surveillance data.
9. Developing a multivariable epidemic-risk prediction model.
10. Validating predictions against historical epidemic events.
11. Exploring Bayesian uncertainty and parameter calibration.
12. Modelling contact networks or household transmission.

A future research version could therefore progress from:

population immunity → susceptibility → transmission → epidemic emergence

to:

population immunity + surveillance signals + wastewater indicators → validated epidemic-risk prediction.

## 25\. Reproducibility

The repository is organised as:

```text
01\_Project\_Documentation/
02\_Code/
03\_Data/
04\_Results/
05\_Report/
README.md
```

The `02\_Code` directory contains model implementation, synthetic data generation, immunity analysis, threshold analysis, intervention analysis and validation scripts.

The `03\_Data` directory contains the synthetic enterovirus immunity dataset and documentation.

The `04\_Results` directory contains CSV summaries and visualisations generated from the simulations.

The `05\_Report` directory contains this report.

A fixed random seed is used for synthetic data generation and Monte Carlo analysis where applicable.

The project is designed so that the workflow can be followed from model assumptions through simulation, data analysis, susceptibility estimation, threshold analysis and interpretation.

## 26\. Academic and PhD-Relevant Computational Skills Demonstrated

The project demonstrates practical experience in:

* Python-based epidemiological modelling
* Deterministic SIR and SEIR simulation
* Translating epidemiological concepts into mathematical models
* Synthetic longitudinal data generation
* CSV data processing
* Age-stratified analysis
* Birth-cohort analysis
* Calendar-time analysis
* Type-specific analysis
* Population susceptibility estimation
* Intervention modelling
* Parameter sensitivity analysis
* Monte Carlo uncertainty analysis
* Computational validation
* Effective reproduction number analysis
* Threshold analysis
* Data visualisation
* Reproducible computational workflows
* Research documentation
* GitHub-based versioned project presentation

The project specifically demonstrates developing competence in connecting population-level immunity concepts with epidemic modelling.

## 27\. Conclusion

This project evolved from a basic SIR outbreak simulation into a broader computational epidemiology framework incorporating SIR, SEIR, intervention modelling, sensitivity analysis, Monte Carlo uncertainty, synthetic population immunity and epidemic-emergence threshold analysis.

The population-immunity extension demonstrates how synthetic individual-level observations can be organised across age, birth cohort, calendar time and virus type, transformed into susceptibility measures and then incorporated into epidemic modelling.

Under the illustrative parameterisation used in this project, the model indicates a critical susceptible fraction of approximately 66.7% for the effective reproduction indicator to reach one.

The integrated framework therefore demonstrates an important computational research concept:

> Population immunity can be represented quantitatively, translated into population susceptibility and incorporated into an epidemic model to investigate conditions associated with epidemic emergence.

The project is intentionally transparent about its limitations. The immunity data are synthetic, the transmission parameters are illustrative, and the epidemic-emergence indicator has not been empirically validated.

The resulting GitHub portfolio is therefore best understood as evidence of developing computational epidemiology and quantitative research capability, rather than evidence of completed real-world enterovirus prediction.

## References

1. Centers for Disease Control and Prevention (CDC). About Influenza (Flu). Updated February 26, 2026.
2. Chan, L. Y. H., Morris, S. E., Stockwell, M. S., Bowman, N. M., Asturias, E., Rao, S., Lutrick, K., Ellingson, K. D., Nguyen, H. Q., Maldonado, Y., McLaren, S. H., Sano, E., Biddle, J. E., Smith-Jeffcoat, S. E., Biggerstaff, M., Rolfes, M. A., Talbot, H. K., Grijalva, C. G., Borchering, R. K., Mellis, A. M., RVTN-Sentinel Study Group. Estimating the generation time for influenza transmission using household data in the United States. Epidemics. 2025;50:100815. doi:10.1016/j.epidem.2025.100815.

