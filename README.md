# Real Estate Price Prediction

This project builds machine learning models to predict real estate
prices for **houses (maisons)** and **apartments (appartements)** using
historical French real estate transaction data.

The repository contains a complete machine learning pipeline including:

-   Data acquisition
-   Data preparation and feature engineering
-   Model training for different property types
-   A Flask web application for testing predictions

------------------------------------------------------------------------

# Project Overview

The workflow of the project is organized as follows:

1.  Download historical property transaction data
2.  Clean and prepare datasets
3.  Train separate machine learning models for houses and apartments
4.  Deploy a local Flask application to generate predictions

------------------------------------------------------------------------

# Installation

Clone the repository and install the required dependencies.

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# Data Acquisition

Download the raw datasets by running:

``` bash
python download_data.py
```

This script will:

-   Download real estate transaction datasets for the **last five years**
-   Store downloaded archives in:
  - tmp_downloads/
-   Extract CSV files into:
    - dataset_raw/

------------------------------------------------------------------------

# Data Preparation

Run the data preparation notebook:

    prep_data.ipynb

This notebook performs:

-   Data cleaning
-   Feature engineering
-   Property type separation
-   Dataset preparation for training

Prepared datasets are saved in:

    datasets_prepd/

Separate datasets are generated for:

-   Houses (Maisons)
-   Apartments (Appartements)

------------------------------------------------------------------------

# Model Training

Two training notebooks are provided.

## Apartment Model

    train_apt.ipynb

## House Model

    train_maison.ipynb

Training produces:

### Processed training datasets

    data_apt/
    data_maison/

### Trained models

    models/

------------------------------------------------------------------------

# Running the Web Application

After completing the previous steps, launch the Flask application:

``` bash
python app.py
```

The application will start locally at:

    http://127.0.0.1:5000

The interface allows users to enter property characteristics and obtain
a predicted property price.

------------------------------------------------------------------------

# Features

-   End-to-end machine learning workflow
-   Separate models for houses and apartments
-   Data preparation notebooks
-   Model training notebooks
-   Flask web interface for prediction testing

------------------------------------------------------------------------

# Repository Structure

    dataset_raw/        Raw downloaded datasets
    datasets_prepd/     Cleaned and prepared datasets
    data_apt/           Apartment training data
    data_maison/        House training data
    models/             Trained machine learning models
    tmp_downloads/      Temporary downloaded archives
    templates/          html for the flask app

    download_data.py    Dataset download script
    prep_data.ipynb     Data preparation notebook
    train_apt.ipynb     Apartment model training
    train_maison.ipynb  House model training
    app.py              Flask prediction interface

------------------------------------------------------------------------