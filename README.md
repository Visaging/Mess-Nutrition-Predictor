# Mess Nutrition Predictor

## 1. Project Overview
We've all experienced it: trying to meet our daily protein or calorie goals while eating at a college dining hall with strict, limited, and often changing menus. The Mess Nutrition Predictor is a web application that uses machine learning. It replaces the tedious task of calculating macros from dining hall meals with an AI system that figures out your exact nutritional intake based on the school dining hall and the meal choices you make.

## 2. Features
* **Multi-Mess Support:** The model's training is based on a distinct dataset containing 84 real meal combinations. These options come from five unique campus dining locations: Mayuri Boys, Mayuri Girls, Rassense, Safal, JMB, and AB Caterers
* **Cascading UI Logic:** The interface is designed to filter meal choices as you make them. Select "JMB Mess" for "Thursday," and you'll only see what's available that day.
* **Instant Visual Feedback:** Dynamic metric cards present the predicted macronutrients, all laid out in a modern, easy-to-read dashboard.

## 3. Technologies Used
* **Language:** Python
* **Libraries:**
    * `pandas` (For data manipulation)
    * `scikit-learn`
    * `streamlit` (For interactive web interface)

## 4. Folder Structure
```text
Mess-Nutrition-Predictor/
├── Screenshots/
    ├── Dashboard.png
    ├── Live-Prediction.png
├── app.py
├── mess_nutrition.csv
└── README.md
```
## 5. Installation and Setup Steps
Follow these instructions to run the project.

**Prerequisites**
* Python 3.x installed
* pip (Python package manager) installed
* An active internet connection

**Step 1: Clone the repository**
Open terminal and run:
```bash
git clone https://github.com/Visaging/Mess-Nutrition-Predictor.git
```
```bash
cd Mess-Nutrition-Predictor
```
**Step 2: Install Dependencies**
Install the firebase library:
```bash
pip install pandas scikit-learn streamlit
```
**Step 3: Run the application**
```bash
python -m streamlit run app.py
```

## 6. Instructions for Testing
To verify the functionality of the system, follow these steps:

**Test 1: Verifying the Cascading Dropdowns**
*Launch the app.
* Under "Time & Place", change the Select Mess dropdown to JMB.
* Change the Select Day dropdown to Thursday.
* Click the Breakfast dropdown.
* _The system successfully filters the dataset and only displays "Uttappam"._

**Test 2: Generating a Live Prediction**
* Leave the Mess as JMB and Day as Thursday.
* Select Sada Bati + Churma for Lunch.
* Select Vada Pav for Snack.
* Select Mutter Paneer + Dal Makhani for Dinner.
* Click the Calculate Macros button.
* _The ML pipeline handles the inputs, converts the text into numerical data, and accurately produces the predicted Protein, Carbs, Fats, and Calories in the metric card_

## 8. Screenshots
**1. Dashboard**
<img width="1920" height="1080" alt="Dashboard" src="https://github.com/user-attachments/assets/21698542-079e-4058-ac54-5539e1a846a4" />

**2. Live Prediction**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f5724e11-517b-482e-8d41-1c5ff4528e94" />
