# Student Exam Performance Predictor

## Project Overview

This repository contains a Flask web application for predicting student exam performance using a trained machine learning model. The app provides a simple user interface to submit demographic and exam preparation details, then returns a predicted score using serialized model artifacts.

## Key Features

- Flask web application with landing page and prediction form
- Navigation buttons between home and prediction pages
- Prediction pipeline loads model and preprocessor from `artifacts/`
- Custom input wrapper to convert form data into a DataFrame
- Structured exception and logging support in `src/`

## Repository Structure

- `app.py` - Flask routes and prediction endpoint
- `templates/index.html` - Home page with navigation buttons
- `templates/home.html` - Prediction page and input form
- `src/pipeline/predict_pipeline.py` - Prediction pipeline and custom input data class
- `src/utils.py` - Utility functions for saving/loading objects and model evaluation
- `src/exception.py` - Custom exception handling
- `src/logger.py` - Basic logging configuration
- `artifacts/` - Serialized model and preprocessor artifacts used for inference
- `notebook/` - Analysis and model training notebooks
- `requirements.txt` - Python package dependencies
- `setup.py` - Package setup for installation

## Installation

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Optionally install the package in editable mode:

   ```powershell
   pip install -e .
   ```

## Running the Application

1. Start the Flask app:

   ```powershell
   python app.py
   ```

2. Open a browser and go to:

   ```text
   http://127.0.0.1:5000/
   ```

3. Use the home page buttons to navigate to the prediction page.

## Live Deployment

The project is deployed on Render and available at:

```text
https://practiceproject-8eeg.onrender.com/
```

## Prediction Input Fields

The web form accepts the following fields:

- `gender`
- `race_ethnicity`
- `parental_level_of_education`
- `lunch`
- `test_preparation_course`
- `reading_score`
- `writing_score`

The app passes these inputs to the prediction pipeline, converts them into a DataFrame, preprocesses the data, and then uses the trained model to predict a score.

## Notes

- Ensure `artifacts/model.pkl` and `artifacts/preprocessor.pkl` exist before running the app.
- Training notebooks are available in `notebook/` for data exploration and model development.
- If you modify the model or preprocessing pipeline, regenerate the artifacts and place them back into `artifacts/`.

## Contact

Author: Yash

Project version: `0.0.1`

