# Install ipywidgets if it's not already installed
!pip install ipywidgets

import numpy as np
import ipywidgets as widgets
from IPython.display import display

def assess_blood_glucose(glucose_level):
    """Assess the blood glucose level and categorize it."""
    if glucose_level < 70:
        return ("**Hypoglycemia**: Your blood glucose level is low. "
                "Eat or drink something with sugar immediately (e.g., juice, candy). "
                "If symptoms persist, consider using a glucagon injection if prescribed.")
    elif 70 <= glucose_level < 126:
        return ("**Normal**: Your blood glucose level is within the normal range. "
                "Diet: Maintain a balanced diet rich in fruits, vegetables, whole grains, and lean proteins. "
                "Limit sugar and refined carbs.")
    elif 126 <= glucose_level < 200:
        return ("**Hyperglycemia**: Your blood glucose level is elevated. "
                "Consider focusing on a low-carb diet and consulting your healthcare provider. "
                "If your blood sugar remains high, your doctor may recommend medication such as metformin or insulin.")
    else:
        return ("**Severe Hyperglycemia**: Your blood glucose level is very high. "
                "Seek medical attention immediately. "
                "Consult a healthcare professional about the need for insulin or other emergency medications.")

def calculate_hba1c(average_glucose):
    """Calculate HbA1c based on the average blood glucose level."""
    if average_glucose is not None:
        hba1c = (average_glucose + 46.7) / 28.7
        return hba1c
    return None

# User Inputs
user_name = widgets.Text(value='', placeholder='Enter your name', description='Name:')
age = widgets.IntSlider(value=30, min=0, max=120, step=1, description='Age:')
glucose_input = widgets.FloatText(value=100.0, description='Current Glucose (mg/dL):')

# Average Glucose Input
average_glucose = widgets.FloatText(value=100.0, description='Average Glucose (mg/dL):')

# Function to handle button click for assessment
def on_assess_click(b):
    assessment = assess_blood_glucose(glucose_input.value)
    print(f"\nAssessment for {user_name.value} (Age: {age.value}):")
    print(assessment)

# Function to handle button click for HbA1c calculation
def on_hba1c_click(b):
    hba1c_result = calculate_hba1c(average_glucose.value)
    if hba1c_result is not None:
        print(f"\nEstimated HbA1c for {user_name.value} (Age: {age.value}): {hba1c_result:.2f}%")
    else:
        print("Please enter a valid average glucose level.")

# Create buttons
assess_button = widgets.Button(description="Assess Blood Glucose")
hba1c_button = widgets.Button(description="Calculate HbA1c")

# Set button click event handlers
assess_button.on_click(on_assess_click)
hba1c_button.on_click(on_hba1c_click)

# Display all widgets
display(user_name, age, glucose_input, assess_button, average_glucose, hba1c_button)
