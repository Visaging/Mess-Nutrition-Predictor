# Mess Nutrition Predictor

## 1. Project Overview
We've all experienced it: trying to meet our daily protein or calorie goals while eating at a college dining hall with strict, limited, and often changing menus. The Mess Nutrition Predictor is a web application that uses machine learning. It replaces the tedious task of calculating macros from dining hall meals with an AI system that figures out your exact nutritional intake based on the school dining hall and the meal choices you make.

## 2. Features
* **Interactive CLI Interface:** A robust, terminal-native menu system that guides the user through building a daily meal plan without requiring any GUI dependencies.
* **Cascading Logic:** The system dynamically filters your available meal options. For example, selecting "JMB Mess" on "Thursday" will only show the meals actually served there that day.
* **Multi-Mess Support:** The model is trained on a custom dataset featuring real-world meal combinations across distinct campus dining halls.

## 3. Technologies Used
* **Language:** Python
* **Libraries:**
    * `pandas` (For data manipulation)
    * `scikit-learn`
    * `os`
    * `sys`

## 4. Folder Structure
```text
Mess-Nutrition-Predictor/
├── Screenshots/
    ├── Dashboard.png
    ├── Live-Prediction.png
├── main.py
├── mess_nutrition.csv
└── README.md
```
## 5. Installation and Setup Steps
Follow these instructions to run the project.

**Prerequisites**
* Python 3.x installed
* pip (Python package manager) installed

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
pip install pandas scikit-learn
```
**Step 3: Run the application**
```bash
python main.py
```

## 6. Instructions for Testing
To verify the functionality of the system, follow these steps:

**Test 1: Verifying the Selection**
* Launch the app via `python main.py`.
* When prompted to select a facility, enter the number corresponding to `JMB`.
* When prompted for the day, enter the number for `Thursday`.
* _The system successfully filters the dataset and only displays "Uttappam" as the valid Breakfast option for that specific mess on that day._

**Test 2: Generating a Live Prediction**
* Proceed through the menu by selecting:
   * Breakfast: `Uttappam`
   * Lunch: `Sada Bati + Churma`
   * Snack: `Vada Pav`
   * Dinner: `Mutter Paneer + Dal Makhani`
* _The ML pipeline processes the inputs, transforms the text into numerical data, and successfully outputs the predicted Protein, Carbs, Fats, and Calories in a formatted terminal table._

## 7. Screenshots
**1. Dashboard**
<img width="1920" height="1080" alt="Dashboard" src="https://github.com/user-attachments/assets/21698542-079e-4058-ac54-5539e1a846a4" />

**2. Live Prediction**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f5724e11-517b-482e-8d41-1c5ff4528e94" />
