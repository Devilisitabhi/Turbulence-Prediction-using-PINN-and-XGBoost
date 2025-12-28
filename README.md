# Turbulence Prediction using PINN and XGBoost

## Overview

This repository presents a comparative study of a Physics-Informed Neural Network (PINN) and an XGBoost regression model for predicting turbulent flow characteristics in a narrow open channel using experimental data. The project evaluates the effectiveness of physics-aware learning against purely data-driven approaches when applied to real laboratory turbulence measurements.

The models are trained using Acoustic Doppler Velocimeter (ADV) data and are used to reconstruct mean velocity components and Reynolds shear stress at multiple streamwise locations and depths.

---

## Project Objectives

- Predict turbulent flow variables using spatial coordinates as inputs  
- Compare physics-informed and purely data-driven machine learning models  
- Evaluate prediction accuracy and physical smoothness of results  
- Reconstruct vertical profiles of velocity and Reynolds stress  
- Extract instantaneous velocity fluctuations from high-frequency ADV data  

---

## Methodology Summary

The PINN model is implemented using TensorFlow and trained to learn smooth and continuous mappings between spatial coordinates and turbulent flow variables. Input normalization and regularization are applied to improve generalization and physical realism.

The XGBoost model is implemented as a multi-output regression baseline using the same inputs and targets as the PINN. This allows for a fair and direct comparison between physics-informed and purely data-driven approaches.

Model performance is evaluated using statistical accuracy metrics and visual comparisons of predicted vertical profiles against experimental data.

---

## Key Findings

- The PINN achieves near-perfect accuracy across all predicted variables.
- PINN predictions are smooth, continuous, and physically consistent.
- XGBoost performs well for dominant velocity components but struggles with smaller turbulence quantities.
- Tree-based models produce jagged and non-physical profiles for sensitive variables such as Reynolds shear stress.
- Physics-informed learning provides clear advantages for turbulence reconstruction from experimental data.

---

## Data Description

The dataset consists of laboratory ADV measurements collected in a rectangular open channel. Measurements were taken at multiple depths and three streamwise locations. Both averaged velocity statistics and high-frequency instantaneous velocity data were used.

Instantaneous velocity data were processed to extract turbulence fluctuations for further analysis.

---

## Tools and Libraries

- Python  
- TensorFlow  
- XGBoost  
- NumPy  
- Pandas  
- Matplotlib  
- Scikit-learn  

---

## Repository Structure

- `Turbulence Prediction using PINN and XGBoost.ipynb` - Contains both PINN and XGBoost codes that evaluated the models on same data.
- `u'v'w'.py` – Instantaneous velocity fluctuation processing    

---

## Future Work

Future extensions include incorporating governing flow equations directly into the PINN framework, training models using instantaneous velocity data, and exploring hybrid physics-informed and data-driven approaches for more complex flow configurations.

---

## Author

Abhineet Kumar  
Final Year B.Tech Project  
Department of Civil Engineering
