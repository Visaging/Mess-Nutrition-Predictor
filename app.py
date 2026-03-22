import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

st.set_page_config(page_title="Campus Mess Predictor", page_icon="🍽️", layout="centered")
#url = "https://docs.google.com/spreadsheets/d/1hqSp7UFG5nCnwMOaLbR29u74k9VW9d344jlO039mkNA/gviz/tq?tqx=out:csv&sheet=Sheet1"
@st.cache_data
def load_data():
    return pd.read_csv("mess_nutrition.csv")
df = load_data()

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

st.title("Campus Mess Nutrition Predictor")
st.markdown("Select your mess and day to see your meal options.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Time & Place")
    mess_name = st.selectbox("Select Mess", df['Mess_Name'].unique())
    filtered_by_mess = df[df['Mess_Name'] == mess_name]

    day = st.selectbox("Select Day", filtered_by_mess['Day'].unique())
    filtered_by_day = filtered_by_mess[filtered_by_mess['Day'] == day]

with col2:
    st.subheader("Meals")
    breakfast = st.selectbox("Breakfast", filtered_by_day['Breakfast_Main'].unique())
    lunch = st.selectbox("Lunch", filtered_by_day['Lunch_Main'].unique())
    snack = st.selectbox("Snack", filtered_by_day['Snack_Choice'].unique())
    dinner = st.selectbox("Dinner", filtered_by_day['Dinner_Main'].unique())

st.divider()

if st.button("Calculate Macros", use_container_width=True):
    input_data = pd.DataFrame({
        'Mess_Name': [mess_name],
        'Day': [day],
        'Breakfast_Main': [breakfast],
        'Lunch_Main': [lunch],
        'Snack_Choice': [snack],
        'Dinner_Main': [dinner]
    })
    
    pred = model.predict(input_data)[0]
    
    st.success("AI Prediction Complete!")
    
    res1, res2, res3, res4 = st.columns(4)
    res1.metric(label="Protein", value=f"{pred[0]:.0f}g")
    res2.metric(label="Carbs", value=f"{pred[1]:.0f}g")
    res3.metric(label="Fats", value=f"{pred[2]:.0f}g")
    res4.metric(label="Calories", value=f"{pred[3]:.0f} kcal")