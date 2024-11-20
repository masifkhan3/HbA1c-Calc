import streamlit as st

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
    hba1c = (average_glucose + 46.7) / 28.7
    return hba1c

# Streamlit app layout
st.set_page_config(page_title="Blood Glucose Assessment Tool", layout="wide")
st.title("🩸 Blood Glucose Assessment Tool")
st.markdown("<h5 style='color:blue;'>Developer: mak3.1 </h5>", unsafe_allow_html=True)
st.markdown("<h5 style='color:purple;'>Tribute to My Daughter: Rameen Khan</h5>", unsafe_allow_html=True)

# Styling for the sidebar
st.sidebar.title("User Input")
st.sidebar.markdown("Please provide your details below:")

# User Input
user_name = st.sidebar.text_input("What is your name?")
age = st.sidebar.number_input("Please enter your age:", min_value=0, max_value=120)

# Input for blood glucose level
glucose_input = st.sidebar.number_input("Enter your current blood glucose level (mg/dL):", min_value=0.0)

# Assess Blood Glucose
if st.sidebar.button("Assess Blood Glucose"):
    assessment = assess_blood_glucose(glucose_input)
    st.markdown(f"<div style='background-color: lightgreen; padding: 10px; border-radius: 5px;'>"
                f"<h5>{assessment}</h5></div>", unsafe_allow_html=True)

    # Input for average blood glucose level
    average_glucose = st.sidebar.number_input("Enter your average blood glucose level (mg/dL) to calculate HbA1c:", min_value=0.0)
    
    # Calculate HbA1c after assessing glucose level
    if st.sidebar.button("Calculate HbA1c"):
        hba1c_result = calculate_hba1c(average_glucose)
        st.markdown(f"<div style='background-color: lightblue; padding: 10px; border-radius: 5px;'>"
                    f"<h5>Your estimated HbA1c is **{hba1c_result:.2f}%**.</h5>"
                    f"<h5>Age: {age} years</h5></div>", unsafe_allow_html=True)

# Final message
if user_name:
    st.markdown(f"<h5 style='color:green;'>Thank you for using the blood glucose and HbA1c assessment tool, {user_name}. Stay healthy!</h5>", unsafe_allow_html=True)

# Optional: Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<footer style='text-align: center; color: gray;'>© 2024 Your Name Here</footer>", unsafe_allow_html=True)
