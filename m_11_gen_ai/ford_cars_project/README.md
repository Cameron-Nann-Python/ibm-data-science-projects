# Final Project: Ford Car Pricing Dataset

## Overview

In this IBM project, I took on the role of a data scientist at a consultancy firm with a resale car dealer as client. The client wants a model that predicts the optimal price for their Ford vehicles. Sales data for model training will take the form of a modified version of the ![Ford Car Pricing Dataset](https://www.kaggle.com/datasets/adhurimquku/ford-car-price-prediction), which has the CC0: Public Domain license. 

## Tasks

The following tasks were performed to achieve the business objective:
- data cleaning: remove duplicate entries and imputing missing values
- exploratory data analysis (EDA): examine relationship between features and price
  - identify number of sales per fuel type
  - identify transmission type with highest number of price outliers
- selecting model architecture: compare linear, polynomial, and ridge regression for univariate and multivariate analysis
- hyperparameter tuning: GridSearch on Ridge regression model for best model performance

## Dataset Description

| Variable | Description |
|----------|-------------|
| model | Car model name |
| year | Year of car make |
| transmission | Type of transmission (Automatic, Manual, or Semi-Auto)|
| mileage | Number of miles traveled |
| fuelType | The type of fuel (Petrol, Diesel, Hybrid, Electric, Other) |
| tax | Annual tax in USD |
| mpg | Miles per gallon |
| engineSize | Engine size of the car |
| price | price of car in USD |

## Results

### Data Insights and Visualization

An exploration of the data revealed key relationships between the Ford cars:
- Over 67.8% of cars used petrol as their fuel type
- Manual transmissions had the greatest number of price outliers
- The price of a car steadily declines as mpg rises

### Model Development and Evaluation

A collection of linear regression and ridge regression models were used to predict the price of a Ford car. The best performing model achieved an r<sup>2</sup> score of 0.7807 and an mean squared error of 5004788 using a Ridge regression model with a second degree polynomial transform.  

## Technologies Used
- Python3.13
- Pandas=3.02: DataFrame operations
- Matplotlib=3.10.7: data visualization
- Seaborn=0.13.2: data visualization
- Sklearn=1.8.0: model development and evaluation

## Getting Started
1. Download VS Code
2. Install Anaconda Navigator. Create a virtual environment to hold lab dependencies
3. Install the Juypter Extension on VS Code. Install the ipykernel for the virtual environment.
4. Run the following command in the Conda terminal:
```
pip install -r requirements.txt
```
5. Open the notebook in VS Code. Connect the virtual environment as the kernel.

## Files Included
- `ford_car_pricing.ipynb`: notebook containing full code implementation
- `prompts.txt`: IBM-provided prompts for LLM-guided workflow (Used Copilot for this lab)
- `requirements.txt`: List of Python dependencies
