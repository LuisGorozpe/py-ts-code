<div align="left" style="position: relative;">
<img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" align="right" width="28%" style="margin: -20px 0 0 20px;">

# PY-TS-CODE

### Advanced Python Programming Practices and Introduction to Time Series Analysis

Official repository containing the notebooks and datasets used in the workshop.

</div>

---

# Project Navigation

<p>

<a href="https://luisgorozpe.github.io/py-ts-code">
<img src="https://img.shields.io/badge/Notebook-Catalog-blue?style=for-the-badge&logo=githubpages">
</a>

<a href="https://github.com/LuisGorozpe/py-ts-code">
<img src="https://img.shields.io/badge/View-Notebooks_on_GitHub-black?style=for-the-badge&logo=github">
</a>

<a href="https://github.com/LuisGorozpe/py-ts-code/archive/refs/heads/main.zip">
<img src="https://img.shields.io/badge/Download-Repository-success?style=for-the-badge&logo=github">
</a>

<a href="https://colab.research.google.com/github/LuisGorozpe/py-ts-code">
<img src="https://img.shields.io/badge/Open_in-Colab-orange?style=for-the-badge&logo=googlecolab">
</a>

</p>

---

# Project Status

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-blue)
![Binder](https://mybinder.org/badge_logo.svg)
![License](https://img.shields.io/github/license/LuisGorozpe/py-ts-code)
![Last Commit](https://img.shields.io/github/last-commit/LuisGorozpe/py-ts-code)
![Repo Size](https://img.shields.io/github/repo-size/LuisGorozpe/py-ts-code)
![Contributors](https://img.shields.io/github/contributors/LuisGorozpe/py-ts-code)

---

# Overview

This repository contains the **official materials for the workshop**

## Advanced Python Programming Practices and Introduction to Time Series Analysis

The project is designed for **students and self-learners** who want to explore time series analysis using Python through **hands-on notebooks and real datasets**.

Workshop announcement:

https://economicas.unam.mx/actividades/practicas-python-2025

Workshop webpage:

https://luisgorozpe.github.io/py-ts-course/#/schedule

---

# Notebook Catalog

All notebooks are also available as **interactive web pages**.

Explore them here:

https://luisgorozpe.github.io/py-ts-code

The web versions are automatically generated from the Jupyter notebooks using **Quarto**.

---

# Notebook Gallery

Below is a quick overview of the main workshop notebooks.

| Notebook | Topic | Colab |
|------|------|------|
| `sesion2.ipynb` | Introduction to Time Series Analysis | [Open](https://colab.research.google.com/github/LuisGorozpe/py-ts-code/blob/main/sesion2.ipynb) |
| `sesion3.ipynb` | Time Series Visualization and Exploration | [Open](https://colab.research.google.com/github/LuisGorozpe/py-ts-code/blob/main/sesion3.ipynb) |
| `sesion4.ipynb` | Classical Time Series Models | [Open](https://colab.research.google.com/github/LuisGorozpe/py-ts-code/blob/main/sesion4.ipynb) |
| `sesion5.ipynb` | Forecasting Methods | [Open](https://colab.research.google.com/github/LuisGorozpe/py-ts-code/blob/main/sesion5.ipynb) |

Students can run these notebooks directly in:

- **Google Colab**
- **Binder**
- **Local Jupyter environments**

---

# Features

This repository includes hands-on notebooks focused on **time series analysis and forecasting with Python**.

Topics covered:

- Time series analysis with Python
- Data visualization with **matplotlib** and **seaborn**
- Classical statistical models:
  - AR
  - MA
  - ARIMA
  - ARCH
  - GARCH
- Real-world datasets
- Computational notebooks for experimentation

Libraries used throughout the project:

- statsmodels
- scikit-learn
- prophet
- tensorflow
- pytorch
- sktime
- darts
- nixtla

---

# Datasets

The repository contains several datasets used for demonstrations and exercises.

| Dataset | Description |
|------|------|
| AirPassengers.csv | Classic dataset for airline passenger forecasting |
| AirlineSales.xls | Airline sales time series |
| Bank.xls | Financial time series dataset |
| CementProduction.xls | Industrial production dataset |
| ClayBricks.xls | Manufacturing dataset |
| Electricity.xls | Electricity demand dataset |
| HouseSales.xls | Housing market dataset |
| JapaneseCars.xls | Automobile sales dataset |
| MilkProduction.xls | Agricultural production dataset |

Descriptions can be expanded later if needed.

---

# Project Structure

Typical structure for a **data science course repository**.

```

py-ts-code
│
├── notebooks
│
├── sesion2.ipynb
├── sesion3.ipynb
├── sesion4.ipynb
├── sesion5.ipynb
│
├── datasets
│
├── dashboard
│   └── app.py
│
├── requirements.txt
├── README.md
└── LICENSE

```

---

# Web Notebook Assets

The folders

```

sesion2_files
sesion3_files
sesion4_files
sesion5_files

```

contain **automatically generated resources** produced when exporting notebooks to HTML using **Quarto**.

These directories include:

- JavaScript dependencies
- CSS stylesheets
- rendered figures
- static assets required for the web versions.

---

# Getting Started

## Prerequisites

To run the notebooks locally you will need:

- Python **≥ 3.13.5**
- JupyterLab or Jupyter Notebook

---

# Installation

## pip

```

git clone [https://github.com/LuisGorozpe/py-ts-code](https://github.com/LuisGorozpe/py-ts-code)
cd py-ts-code

pip install -r requirements.txt

```

---

## Poetry

```

git clone [https://github.com/LuisGorozpe/py-ts-code](https://github.com/LuisGorozpe/py-ts-code)
cd py-ts-code

poetry install

```

---

## Conda

```

conda create -n py-ts python=3.13
conda activate py-ts

pip install -r requirements.txt

```

---

# Running the Notebooks

Start Jupyter:

```

jupyter lab

```

---

# Launch in Binder

You can run the notebooks without installing anything.

```

[https://mybinder.org/v2/gh/LuisGorozpe/py-ts-code/main](https://mybinder.org/v2/gh/LuisGorozpe/py-ts-code/main)

```

---

# Dashboard

The repository also includes a small **interactive dashboard built with Streamlit**.

Run it locally with:

```

streamlit run dashboard/app.py

```

---

# Roadmap

Planned future extensions:

- Additional notebooks on classical time series theory
- Modern forecasting approaches
- Machine learning for time series
- Deep learning models for forecasting

---

# Contributing

Contributions are welcome.

You can:

- open issues
- propose improvements
- submit pull requests

Repository:

https://github.com/LuisGorozpe/py-ts-code

---

# License

This project is released under the

### GNU General Public License v3.0

See the LICENSE file for details.

---

# Acknowledgments

This material was developed with academic support from:

- National Autonomous University of Mexico (**UNAM**)
- Faculty of Economics
- **Center for Research in Mathematics (CIMAT)**
- **Secretariat of Science, Humanities, Technology and Innovation (SECIHTI)**

Recommended references:

- Hyndman & Athanasopoulos — *Forecasting: Principles and Practice*
- Hamilton — *Time Series Analysis*

