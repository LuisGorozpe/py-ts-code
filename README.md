<div align="left" style="position: relative;">

# 🧠 PY-TS-CODE

<img src="portada.png" align="right" width="45%" style="margin: -20px 0 0 20px;">


Official repository containing the notebooks and datasets used in the workshop: [**Advanced Python Programming Practices and Introduction to Time Series Analysis.**](https://luisgorozpe.github.io/py-ts-course)

 <p>Built with the tools and technologies:</p>
        <p>
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat-square&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat-square&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/SymPy-3B5526.svg?style=flat-square&logo=SymPy&logoColor=white" alt="SymPy">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat-square&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat-square&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
	<img src="https://img.shields.io/badge/Poetry-60A5FA.svg?style=flat-square&logo=Poetry&logoColor=white" alt="Poetry">
	<img src="https://img.shields.io/badge/SciPy-8CAAE6.svg?style=flat-square&logo=SciPy&logoColor=white" alt="SciPy">
</p>
</div>



## 📚 Table of Contents

- 🧠 [ PY-TS-CODE](#PY-TS-CODE)
- 📚 [ Table of Contents](#-Table-of-Contents)
- 🧭 [ Project Navigation](#-Project-Navigation)
- 👀 [ Overview](#-Overview)
- 🚦 [ Project Status](#-Project-Status)
- 📓 [ Notebook Catalog](#-Notebook-Catalog)
- 🖼️ [ Notebook Gallery](#-Notebook-Gallery)
- ✨ [ Features](#-features)
- 🗂️ [ Datasets](#-Datasets)
- 🏗️ [ Project Structure](#-project-structure)
  - 📦 [ Web Notebook Assets](#-Web-Notebook-Assets)
- 🚀 [ Getting Started](#-getting-started)
  - 📋 [ Prerequisites](#-prerequisites)
  - ⚙️ [ Installation](#-installation)
    - 🐍 [ Pip](#-pip)
    - 📜 [ Poetry](#-poetry)
    - 🐍‍⬛ [ Conda](#-conda)
- ▶️ [ Running the Notebooks](#-Running-the-Notebooks)
  - 🌐 [ Launch in Binder](#-Launch-in-Binder)
- 📊 [ Dashboard](#-Dashboard)
- 🗺️ [ Roadmap](#-Roadmap)
- 🤝 [ Contributing](#-contributing)
- 📄 [ License](#-license)
- 🙏 [ Acknowledgments](#-acknowledgments)

---

# 🧭 Project Navigation

<p>

<a href="https://luisgorozpe.github.io/py-ts-code">
<img src="https://img.shields.io/badge/Notebook-Catalog-blue?style=for-the-badge&logo=githubpages">
</a> <a href="https://github.com/LuisGorozpe/py-ts-code">
<img src="https://img.shields.io/badge/View-Notebooks_on_GitHub-black?style=for-the-badge&logo=github">
</a> <a href="https://github.com/LuisGorozpe/py-ts-code/archive/refs/heads/main.zip">
<img src="https://img.shields.io/badge/Download-Repository-success?style=for-the-badge&logo=github">
</a> <a href="https://colab.research.google.com/github/LuisGorozpe/py-ts-code">
<img src="https://img.shields.io/badge/Open_in-Colab-orange?style=for-the-badge&logo=googlecolab">
</a>
</p>

---

# 🚦Project Status

![Python](https://img.shields.io/badge/Python-3.13+-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-blue)
![Binder](https://mybinder.org/badge_logo.svg)
![License](https://img.shields.io/github/license/LuisGorozpe/py-ts-code)
![Last Commit](https://img.shields.io/github/last-commit/LuisGorozpe/py-ts-code)
![Repo Size](https://img.shields.io/github/repo-size/LuisGorozpe/py-ts-code)
![Contributors](https://img.shields.io/github/contributors/LuisGorozpe/py-ts-code)

---

# 👀 Overview

This repository contains the official materials for the workshop **Advanced Python Programming Practices and Introduction to Time Series Analysis**.

The project is designed for **students and self-learners** who want to explore time series analysis using Python through **hands-on notebooks and real datasets**.

Workshop announcement:

https://economicas.unam.mx/actividades/practicas-python-2025

Workshop webpage:

https://luisgorozpe.github.io/py-ts-course/#/schedule

---

# 📓 Notebook Catalog

All notebooks are also available as **interactive web pages**.

Explore them here:

https://luisgorozpe.github.io/py-ts-code

The web versions are automatically generated from the Jupyter notebooks using [**Quarto**](https://quarto.org/) through [VScode](https://code.visualstudio.com/).

---

# 🖼️ Notebook Gallery

Below is a quick overview of the main workshop notebooks.

| Notebook | Topic | Colab |
|------|------|------|
| `sesion2.ipynb` | Introduction to Time Series Analysis: Visualization and Exploration | [Open](https://colab.research.google.com/github/LuisGorozpe/py-ts-code/blob/main/sesion2.ipynb) |
| `sesion3.ipynb` | Manipulation and modelling with advanced libraries (Python/R) | [Open](https://colab.research.google.com/github/LuisGorozpe/py-ts-code/blob/main/sesion3.ipynb) |
| `sesion4.ipynb` | Advanced Topics in Time Series | [Open](https://colab.research.google.com/github/LuisGorozpe/py-ts-code/blob/main/sesion4.ipynb) |
| `sesion5.ipynb` | Documentation, Presentation, and Styling of Python Code | [Open](https://colab.research.google.com/github/LuisGorozpe/py-ts-code/blob/main/sesion5.ipynb) |

Students can run these notebooks directly in:

- **Google Colab**
- **Binder**
- **Local Jupyter environments**

---

# ✨ Features

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

# 🗂️ Datasets

The repository contains several datasets used for demonstrations and exercises.

| Dataset | Description |
|------|------|
| AirPassengers.csv | Classic benchmark dataset used in time series forecasting. Contains monthly totals of international airline passengers from **1949–1960**, measured in thousands. Widely used in the literature for demonstrating **ARIMA, SARIMA, seasonal decomposition, and exponential smoothing models**. The data exhibits clear **trend and multiplicative seasonality**, making it ideal for teaching forecasting methods. |
| AirlineSales.xls | Time series dataset representing airline passengers. [airpass_ts](https://cran.r-project.org/web/packages/timeSeriesDataSets/timeSeriesDataSets.pdf). |
| ClayBricks.xls | Manufacturing time series dataset related to clay brick production. Only Bricks production in millions of bricks from 1956-03-01 to 1969-01-01 - [ebricksq_ts](https://cran.r-project.org/web/packages/timeSeriesDataSets/timeSeriesDataSets.pdf) - [Reference](https://rpubs.com/jhnfrr_/DATA624_HW1). |
| Electricity.xls | Electricity demand or production time series dataset. [elec_ts](https://cran.r-project.org/web/packages/timeSeriesDataSets/timeSeriesDataSets.pdf). |
| HouseSales.xls | Housing market dataset containing time series observations of house sales. |
| JapaneseCars.xls | Time series dataset describing sales or production of Japanese automobiles over time. |
| MilkProduction.xls | Monthly milk production per cow (in pounds) [milk_ts](https://cran.r-project.org/web/packages/timeSeriesDataSets/timeSeriesDataSets.pdf).|

Datasets are sets of time series typically studied in the literature.



---

# 🏗️ Project Structure

Structure of the **data science course repository**.

```
py-ts-code
│
├── notebooks
│
├── sesion*.ipynb
│
├── datasets
|
├── *.xls
├── *.csv
│
├── Noteboks web
|
├── sesion*.html
|
├── dashboard
│   └── app.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📦 Web Notebook Assets

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

# 🚀 Getting Started

## 📋 Prerequisites

To run the notebooks locally you will need:

- Python **≥ 3.13.5**
- JupyterLab or Jupyter Notebook

---

## ⚙️ Installation

### 🐍 pip

```sh
❯ git clone ttps://github.com/LuisGorozpe/py-ts-code
❯ cd py-ts-code
❯ pip install -r requirements.txt
```

---

### 📜 Poetry

```sh
❯ git clone https://github.com/LuisGorozpe/py-ts-code
❯ cd py-ts-code
❯ poetry install
```

---

### 🐍‍⬛ Conda

```sh
❯ conda create -n py-ts python=3.13
❯ conda activate py-ts
❯ pip install -r requirements.txt
```

---

# ▶️ Running the Notebooks

Start Jupyter Notebook, Jupyterlab or VScode in the local directory.

---

## 🌐 Launch in Binder

You can run the notebooks without installing anything.



[https://mybinder.org/v2/gh/LuisGorozpe/py-ts-code/main](https://mybinder.org/v2/gh/LuisGorozpe/py-ts-code/main)



---

# 📊 Dashboard

The repository also includes a small **interactive dashboard built with Streamlit**.

Run it locally with:

```sh
❯ streamlit run dashboard/app.py
```

---

# 🗺️ Roadmap

Planned future extensions:

- Additional notebooks on classical time series theory
- Modern forecasting approaches
- Machine learning for time series
- Deep learning models for forecasting

---

# 🤝 Contributing

Contributions are welcome.

You can:

- open issues
- propose improvements
- submit pull requests

Repository:

https://github.com/LuisGorozpe/py-ts-code

---

# 📄 License

This project is released under the

### GNU General Public License v3.0

See the LICENSE file for details.

---

# 🙏 Acknowledgments

This material was developed with academic support from:

- Institute of Economic Sciences - **National Autonomous University of Mexico** (**UNAM**)
- **Center for Research in Mathematics (CIMAT)**
- **Secretariat of Science, Humanities, Technology and Innovation (SECIHTI)**

Recommended references:

 + R. A. D. Peter and J. Brockwell, “Time Series: Theory and Methods,” 2nd Edition, Springer, New York, 1991. [![DOI:10.1007/978-1-4419-0320-4](https://zenodo.org/badge/DOI/10.1007/978-3-319-76207-4_15.svg)](https://doi.org/10.1007/978-1-4419-0320-4)
 + Wei, W. W. S. (2006). Time Series Analysis: Univariate and Multivariate Methods. Reino Unido: Pearson Addison Wesley. [PDF](https://civil.colorado.edu/~balajir/CVEN6833/lectures/wwts-book.pdf)
 + Luis Enrique, A. G. (2025, octubre 29). Modelos de Varianza Condicional: ARCH, GARCH, etc. - Series de Tiempo. Zenodo. [![DOI:10.5281/zenodo.17469881](https://zenodo.org/badge/DOI/10.1007/978-3-319-76207-4_15.svg)](https://doi.org/10.5281/zenodo.17469881)
+ A systematic review of Python packages for time series analysis [ArXiv](https://arxiv.org/abs/2104.07406) [Overview](https://siebert-julien.github.io/time-series-analysis-python) [Page](https://siebert-julien.github.io/time-series-analysis-python/overview.html)
+ MATH6011: Forecasting, course [Universidad de Southampton](https://www.southampton.ac.uk/courses/2026-27/modules/math6011) [PDF](https://www.southampton.ac.uk/~abz1e14/papers/Forecasting.pdf) [Paper](https://www.southampton.ac.uk/~abz1e14/papers/ForecastingPaper.pdf).


