# Verify Energies

> Lucas Palmeira: scientific initiation scholarship holder at the Laboratory of Bioinformatics and Computational Chemistry - UESB.

## Motivations

Due to the needs of the laboratory and the progress of the research, it was necessary to create alternatives to accelerate and automate tasks.

## Project description

The affinity energies (Kcal/mol) resulting from the molecular docking calculations for each molecule are extracted. After obtaining the affinity energies, a table (CSV) is created with the energy values and a histogram is also created. In addition, with these data, the arithmetic mean, median, variance and the most common energy value among the data are calculated.


## Prerequisites

Some libraries must be installed:

matplotlib (https://matplotlib.org/)

```bash
pip3 install matplotlib
```

pandas (https://pandas.pydata.org/)

```bash
pip3 install pandas
```

Python release version used in the project: 3.8

## Run

Running

```bash
chmod +x verify_energies.py
./verify_energies
```



