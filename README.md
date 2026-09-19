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