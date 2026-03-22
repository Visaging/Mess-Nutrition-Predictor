# Mess Nutrition Predictor

## 1. Project Overview
We've all been there: trying to hit our daily protein or calorie goals while relying on a college mess with strict, conditional, and ever-changing menus. The Campus Mess Macro Predictor is a Machine Learning web application built for the Bring Your Own Project (BYOP) capstone. It replaces the guesswork of estimating macros from dining hall buffets with an AI-driven system that predicts your exact nutritional intake based on the specific campus mess and meal combinations you choose.

## 2. Features
* **Multi-Mess Support:** The model is trained on a custom dataset featuring 84 real-world meal combinations across 5 distinct campus dining halls (Mayuri Boys, Mayuri Girls, Rassense, Safal, JMB, and AB Caterers).
* **Cascading UI Logic:** The intelligent user interface dynamically filters your available meal options. For example, selecting "JMB Mess" on "Thursday" will only show the meals actually served there that day.
* **Instant Visual Feedback:** Displays the predicted macronutrients in a clean, modern dashboard format using interactive metric cards.

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
    ├── app_dashboard.png
    ├── cascading_dropdowns.png
    ├── successful_prediction.png
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
cd Campus-Mess-Predictor
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
* _The system successfully filters the dataset and only displays "Uttappam" (the actual JMB Thursday breakfast)._

**Test 2: Generating a Live Prediction**
* Leave the Mess as JMB and Day as Thursday.
* Select Sada Bati + Churma for Lunch.
* Select Vada Pav for Snack.
* Select Mutter Paneer + Dal Makhani for Dinner.
* Click the Calculate Macros button.
* _The ML pipeline processes the inputs, transforms the text into numerical data using OneHotEncoding, and successfully outputs the predicted Protein, Carbs, Fats, and Calories in the metric cards._

## 7. Future Enhancements
* **Cloud Database Integration:** Migrate mess_nutrition.csv to a cloud database (like PostgreSQL or Firebase) so caterers can log in and update their weekly menus live.
* **API Deployment:** Wrap the Scikit-Learn model in FastAPI to allow mobile apps or campus websites to pull macro predictions remotely.
* **Personalized Fitness Tracking:** Allow users to create profiles, input their body weight, and track their daily AI-predicted macros against personal fitness goals.

## 8. Screenshots
**1. Dashboard**
TBA

**2. Live Prediction**
TBA
