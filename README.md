# Water Quality Prediction

## Overview

This project aims to predict whether water is **safe or unsafe** for consumption based on various chemical parameters using Machine Learning. The model takes multiple water quality indicators as input and classifies the water as **potable (safe)** or **non-potable (unsafe)**.

## Dataset

The dataset contains various physicochemical properties of water, including:

- **pH Level**: Measure of how acidic or basic the water is.
- **Hardness**: The concentration of dissolved minerals.
- **Solids**: Total dissolved solids (TDS) in water.
- **Chloramines**: Concentration of disinfectants used in water treatment.
- **Sulfate**: Presence of sulfate ions.
- **Conductivity**: Ability of water to conduct electricity.
- **Organic Carbon**: Organic contaminants in water.
- **Trihalomethanes**: Byproducts of chlorination.
- **Turbidity**: Clarity of water.
- **Potability**: (Target Variable) **1 = Safe water**, **0 = Unsafe water**

## Project Structure

- `Water_Quality_Prediction.ipynb` - Jupyter Notebook for data analysis, preprocessing, and model training.
- `app.py` - A Flask/Streamlit web application for water quality prediction.
- `svm.pkl` - Serialized Machine Learning model for prediction.
- `requirements.txt` - Dependencies required to run the project.
- `README.md` - Documentation of the project.

## Installation & Setup

1. Clone this repository:
   ```bash
   git clone "https://github.com/PrajwalMalokar/Water_Quality_Prediction.git"
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook for training and evaluation:
   ```bash
   jupyter notebook Water_Quality_Prediction.ipynb
   ```
4. To launch the web app:
   ```bash
   streamlit run app.py
   ```

## Model Used

The project utilizes **Support Vector Machine (SVM)** or other classifiers (Random Forest, Logistic Regression, etc.) for predicting water potability. The best-performing model is saved as `svm.pkl` for deployment.

## Features & Functionality

- **Data Cleaning & Preprocessing:**
  - Handling missing values
  - Normalization & scaling of features
  - Feature selection
- **Machine Learning Model Training:**
  - Splitting dataset into training and testing
  - Training models and evaluating accuracy
- **Web Application:**
  - User inputs water quality parameters
  - Model predicts and displays whether the water is safe or unsafe

## Results

The trained model achieves **78% accuracy** on test data, making it a reliable predictor for water safety.

## Future Improvements

- Incorporate deep learning models for better accuracy.
- Collect real-world data for further training.
- Deploy the application on cloud platforms.

## License

This project is licensed under the MIT License.

---

### Contributors

- **Prajwal Malokar**
- **Tanmay Patil**
- **Yash Gangurde** 



