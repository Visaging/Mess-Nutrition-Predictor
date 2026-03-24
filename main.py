import os
import sys
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def clear_screen():
    os.system('cls')

def print_header():
    print("==================================================")
    print("            CAMPUS MESS MACRO PREDICTOR            ")
    print("==================================================\n")

def get_user_choice(prompt, options):
    while True:
        print(f"\n{prompt}")
        for idx, option in enumerate(options, 1):
            print(f"  {idx}. {option}")
        
        try:
            choice = int(input("\nEnter the number of your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    clear_screen()
    print_header()
    print("Initializing")
    
    # 1. Load Data
    try:
        df = pd.read_csv('mess_nutrition.csv')
    except FileNotFoundError:
        print("ERROR: 'mess_nutrition.csv' not found in the current directory.")
        print("Please ensure the dataset is in the same folder as this script.")
        sys.exit(1)

    # 2. Train Model
    categorical_features = ['Mess_Name', 'Day', 'Breakfast_Main', 'Lunch_Main', 'Snack_Choice', 'Dinner_Main']
    X = df[categorical_features]
    y = df[['Protein_g', 'Carbs_g', 'Fats_g', 'Total_kcal']]

    preprocessor = ColumnTransformer(
        transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)]
    )
    
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', MultiOutputRegressor(RandomForestRegressor(n_estimators=100, random_state=42)))
    ])
    
    model.fit(X, y)

    # 3. Interactive CLI Menu
    while True:
        clear_screen()
        print_header()
        
        # Selection Logic
        messes = df['Mess_Name'].unique().tolist()
        selected_mess = get_user_choice("Select your Mess Facility:", messes)
        
        filtered_by_mess = df[df['Mess_Name'] == selected_mess]
        days = filtered_by_mess['Day'].unique().tolist()
        selected_day = get_user_choice("Select the Day of the Week:", days)
        
        filtered_by_day = filtered_by_mess[filtered_by_mess['Day'] == selected_day]
        
        breakfast = get_user_choice("Select your Breakfast:", filtered_by_day['Breakfast_Main'].unique().tolist())
        lunch = get_user_choice("Select your Lunch:", filtered_by_day['Lunch_Main'].unique().tolist())
        snack = get_user_choice("Select your Snack:", filtered_by_day['Snack_Choice'].unique().tolist())
        dinner = get_user_choice("Select your Dinner:", filtered_by_day['Dinner_Main'].unique().tolist())

        # 4. Make Prediction
        input_data = pd.DataFrame({
            'Mess_Name': [selected_mess],
            'Day': [selected_day],
            'Breakfast_Main': [breakfast],
            'Lunch_Main': [lunch],
            'Snack_Choice': [snack],
            'Dinner_Main': [dinner]
        })

        clear_screen()
        print("Running AI Prediction...\n")
        pred = model.predict(input_data)[0]

        print("==================================================")
        print("            📊 YOUR DAILY MACROS 📊            ")
        print("==================================================")
        print(f"  Facility: {selected_mess}")
        print(f"  Day:      {selected_day}")
        print("--------------------------------------------------")
        print(f"  🥩 Protein:       {pred[0]:.0f} g")
        print(f"  🍚 Carbohydrates: {pred[1]:.0f} g")
        print(f"  🥑 Fats:          {pred[2]:.0f} g")
        print(f"  🔥 Total Kcal:    {pred[3]:.0f} kcal")
        print("==================================================\n")

        # 5. Loop or Exit
        again = input("Would you like to calculate another day? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThank you for using the Campus Nutrition Predictor.")
            break

if __name__ == "__main__":
    main()
