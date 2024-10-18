import streamlit as st

def assess_blood_glucose(glucose_level):
    """Assess the blood glucose level and categorize it as normal, hyperglycemia, or hypoglycemia."""
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

# Streamlit app layout
st.title("Blood Glucose Assessment Tool")
st.markdown("### Developer: Your Name Here")  # Replace with your name
st.markdown("### Tribute to My Daughter: [Daughter's Name]")  # Replace with your daughter's name

# Adding sections for Blood and Injections
st.markdown("#### 🩸 Blood Management")
st.markdown("Keep track of your blood glucose levels and maintain a balanced diet for optimal health.")

st.markdown("#### 💉 Injection Management")
st.markdown("If you require insulin injections, ensure you follow the recommended guidelines and consult your healthcare provider.")

# User Inputs
user_name = st.text_input("What is your name?")
age = st.number_input("Please enter your age:", min_value=0, max_value=120)
glucose_input = st.number_input("Enter your current blood glucose level (mg/dL):", min_value=0.0)

if st.button("Assess Blood Glucose"):
    assessment = assess_blood_glucose(glucose_input)
    st.write(assessment)

    average_glucose = st.number_input("Enter your average blood glucose level (mg/dL) to calculate HbA1c:", min_value=0.0)
    
    if st.button("Calculate HbA1c"):
        hba1c_result = calculate_hba1c(average_glucose)
        
            st.write(f"Your estimated HbA1c is {hba1c_result:.2f}%.")
        
            st.write("Please enter a valid average glucose level.")

st.write(f"Thank you for using the blood glucose and HbA1c assessment tool, {user_name}. Stay healthy!")
