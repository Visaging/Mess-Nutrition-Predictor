# Mess Nutrition Predictor

## 1. Project Overview
We all know the frustration of trying to consume a certain amount of protein or calories when eating at a college cafeteria, where the menu is strict, limited, and changes frequently. The Mess Nutrition Predictor is a web application that utilizes machine learning to take the guesswork out of calculating your macros based on the school dining hall and the meals you consume.

## 2. Features
* **Interactive CLI Interface:** A powerful menu interface that walks the user through the process of creating a daily meal plan without the need for any GUI dependencies.
* **Cascading Logic:** The system dynamically narrows your choices for the available meals.
* **Multi-Mess Support:** The model was trained on a custom data set with actual combinations of meals from different campus dining halls.

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
    ├── 1-Dashboard.png
    ├── 2-Selection.png
    ├── 3-Live Prediction.png
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
* Run the app using the command: `python main.py`.
* Select the option for the facility by entering the number that corresponds to `JMB`.
* Select the option for the day by entering the number that corresponds to `Thursday`.
* _The system correctly filters the data and only shows "Uttappam" as the valid option for Breakfast for that specific mess on that day._

**Test 2: Generating a Live Prediction**
* Navigate through the menu by entering the following:
   * Breakfast: `Uttappam`
   * Lunch: `Sada Bati + Churma`
   * Snack: `Vada Pav`
   * Dinner: `Mutter Paneer + Dal Makhani`
* _The machine learning pipeline correctly processes all the input data, converts the text into numerical form, and displays the predicted Protein, Carbs, Fats, and Calories in a formatted table in the terminal._

## 7. Screenshots
* **1. Dashboard**
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/69f7d452-5c8e-4f7d-bba5-8d22f3821208" />

* **2. Selection**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/78763381-e970-41e3-813e-ce2110c6b8aa" />

* **3. Live Prediction**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7e9435cc-7a37-4485-8d9f-00c0748e0b60" />

