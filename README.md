# 🍽️ Campus Mess Macro Predictor (BYOP Capstone)

## 📌 Project Overview
The Campus Mess Macro Predictor is a Machine Learning web application designed to solve a real-world problem for college students: tracking daily nutritional intake across multiple university dining halls with complex, conditional menus. 

This project uses a **Multi-Output Random Forest Regressor** to predict Protein, Carbohydrates, Fats, and Total Calories simultaneously based on a student's daily meal selections.

## 🚀 Features
* **Multi-Mess Support:** Trained on 84 real-world meal combinations across 5 distinct campus dining halls (Mayuri Boys, Mayuri Girls, Rassense, Safal, JMB, and AB Caterers).
* **Cascading UI Logic:** The Streamlit interface dynamically filters available meals based on the specific mess and day selected.
* **Multi-Target Prediction:** Predicts four separate macro-nutritional values (Protein, Carbs, Fats, Kcal) in a single inference step.

## 🛠️ Tech Stack
* **Python 3**
* **Pandas** (Data manipulation and feature engineering)
* **Scikit-Learn** (Machine Learning Pipeline, OneHotEncoding, MultiOutputRegressor)
* **Streamlit** (Interactive Web Interface)

## 📂 File Structure
* `mess_nutrition.csv`: The custom dataset built from actual campus mess timetables.
* `app.py`: The core Machine Learning pipeline and Streamlit web interface.
* `Run_Predictor.bat`: A Windows executable batch file for 1-click deployment.

## 💻 How to Run Locally

### Option 1: The Easy Way (Windows Only)
1. Download or clone this repository to your local machine.
2. Double-click the `Run_Predictor.bat` file.
3. The application will automatically launch in your default web browser.

### Option 2: Using the Terminal (Windows / Mac / Linux)
1. Open your terminal and navigate to the project directory.
2. Ensure you have the required libraries installed:
   ```bash
   pip install pandas scikit-learn streamlit
