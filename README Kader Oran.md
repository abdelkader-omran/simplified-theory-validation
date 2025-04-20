# Simplified Theory of Everything – Validation Pipeline

This repository contains the full implementation of the automated validation pipeline for the Simplified Theory of Everything by Dr. Ali Bouteben Abderrahmane (Université de Batna 2).

## Author of the Pipeline
Dr Abdelkader Omran (Chercheur indépendant en arts et sciences, deep learner).

## Pipeline Overview
- Three deep learning models validate the theory across CMB, redshift, and LHC data.
- Reproducibility is ensured with DVC and GitHub Actions.
- All models are trained with validation support, metrics logging, and visual summary generation.

## Contents
- `/scripts/`: Model training, validation metric extraction, and aggregation scripts.
- `/checkpoints/`: Best-performing models.
- `/predictions/`: Output predictions for evaluation.
- `dvc.yaml`, `dvc.lock`: DVC pipeline definition and lock state.
- `.github/workflows/`: Continuous integration pipeline via GitHub Actions.

## Results Summary
- Validation loss (final epoch):
  - CMB model: `0.000843`
  - Redshift model: `0.001072`
  - LHC model: `0.000961`
- Summary plot available as artifact: `validation_metrics_plot.png`

## Citation
Based on the theory: "La théorie du tout simplifiée" par Dr Ali Bouteben Abderrahmane (DOI: 10.13140/RG.2.2.23201.62569)

Validation pipeline developed by Dr Abdelkader Omran, chercheur indépendant.
