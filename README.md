# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
```

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**
- Created a reproducible Anaconda environment and a structured Git repository for physical simulations.
- Implemented and benchmarked pure-Python and optimized NumPy approaches for radioactive decay modeling.

**Speed comparison (loop vs NumPy):**
- loop : 6.8595 s
- numpy : 0.0003 s
- speed-up: 25441.4 x faster

**Tests:** all passing? (yes / no)
- yes

**Conclusion:**
- Standard Python loops introduce significant performance overhead when iterating over hundreds of thousands of independent atoms.
- Using NumPy's vectorized functions, such as `rng.binomial`, processes arrays simultaneously, providing massive execution speed-ups.
- Configuring a comprehensive `.gitignore` and automated `pytest` verification ensures seamless reproducibility across different machines.

---

## PW1 - Lab B: Data, Plotting, and Automation

**What the data showed:**
- The provided dataset contains two columns: experimental time values and the corresponding remaining particle counts. It records a clear exponential decay process over time.

**Comparison with Analytical Law:**
- Based on the generated side-by-side subplots, the observed data points on the left perfectly match the smooth analytical curve \(N(t) = N_0 e^{-\lambda t}\) plotted on the right. The two figures share the exact same scale and decay progression.

**Pipeline Automation:**
- The Snakemake pipeline automates the generation of `figure.png` by tracking modifications in `decay_observed.csv` and `plot.py`, ensuring that the visualization is efficiently rebuilt only when its input sources change.

# Lab A: Motion Analysis from Tracking Data

## Overview
In this lab, we analyzed 1D free-fall motion data from `freefall.csv` using Python (`numpy`, `scipy`, `matplotlib`).

## Results
- **Mean Acceleration:** -8.58 m/s²
- **Standard Deviation of Acceleration:** 28.72 m/s²
- **Max Difference in Recovered Position:** 0.7846 m

## Generated Plots
The processed graphs showing position, velocity, and acceleration over time are saved in `motion.png`.

## PW2 - Lab B: Optimization in Chemistry

### Part 2: Optimization Methods Comparison
- **Convex function f(x):** All three methods (Gradient Descent, Newton's method, SLSQP) converged to $x = 3.0$.
- **Harder function g(x):** 
  - Starting at $x_0 = 0.0$, Newton landed on a local maximum ($x \approx 0.17$, $g'' < 0$), while SLSQP converged to $x \approx -1.30$.
  - Starting at $x_0 = 2.0$, Newton converged to a local minimum ($x \approx 1.13$), while SLSQP found $x \approx -1.30$.
  - *Conclusion:* On complex non-convex functions, local optimization methods strongly depend on the starting point and algorithm.

### Part 3: Reaction Rate Fitting
- **Fitted Rate Constant (k):** $0.2618 \text{ s}^{-1}$
- Plot saved as `kinetics.png`.

### Part 4: Chemical Equilibrium
- **Equilibrium Extent (x):** $0.6638$ (Newton and SLSQP agree).
- **Equilibrium Composition:** $H_2 = 0.3362 \text{ mol}$, $I_2 = 0.3362 \text{ mol}$, $HI = 1.3277 \text{ mol}$.
- Plot saved as `equilibrium.png`.

### Part 5: Titration Equivalence Point
- **Equivalence Point Volume:** $50.0 \text{ mL}$ (identified by the peak of $d(pH)/dV$).
- Plot saved as `titration.png`.