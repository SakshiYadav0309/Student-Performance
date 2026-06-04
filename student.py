import streamlit as st
import pandas as pd
import joblib

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #1e3c72 0%,
        #2a5298 50%,
        #6dd5ed 100%
    );
}

h1 {
    color: white !important;
    text-align: center;
    font-size: 42px !important;
}

h3 {
    color: white !important;
}

label {
    color: white !important;
    font-weight: bold;
}

[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.1);
}

.stButton > button {
    background-color: #0072ff;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    width: 100%;
    height: 50px;
    border: none;
}

.stButton > button:hover {
    background-color: #0056d6;
}

.result-box {
    background-color: rgba(255,255,255,0.2);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# LOAD MODEL
# ==========================
model = joblib.load("student_performance_model.pkl")

# ==========================
# TITLE
# ==========================
st.title("🎓 Student Performance Prediction System")

st.markdown(
    "<h3 style='text-align:center;'>Predict Student Final Grade (G3)</h3>",
    unsafe_allow_html=True
)

# ==========================
# INPUTS
# ==========================

col1, col2 = st.columns(2)

with col1:

    school = st.selectbox("School", ["GP", "MS"])

    sex = st.selectbox("Gender", ["F", "M"])

    age = st.slider("Age", 15, 22, 17)

    address = st.selectbox("Address", ["U", "R"])

    famsize = st.selectbox("Family Size", ["LE3", "GT3"])

    Pstatus = st.selectbox("Parent Status", ["A", "T"])

    Medu = st.slider("Mother Education", 0, 4, 2)

    Fedu = st.slider("Father Education", 0, 4, 2)

    Mjob = st.selectbox(
        "Mother Job",
        ["teacher", "health", "services", "at_home", "other"]
    )

    Fjob = st.selectbox(
        "Father Job",
        ["teacher", "health", "services", "at_home", "other"]
    )

    reason = st.selectbox(
        "Reason",
        ["course", "home", "reputation", "other"]
    )

    guardian = st.selectbox(
        "Guardian",
        ["mother", "father", "other"]
    )

with col2:

    traveltime = st.slider("Travel Time", 1, 4, 1)

    studytime = st.slider("Study Time", 1, 4, 2)

    failures = st.slider("Past Failures", 0, 4, 0)

    schoolsup = st.selectbox("School Support", ["yes", "no"])

    famsup = st.selectbox("Family Support", ["yes", "no"])

    paid = st.selectbox("Paid Classes", ["yes", "no"])

    activities = st.selectbox("Extra Activities", ["yes", "no"])

    nursery = st.selectbox("Nursery", ["yes", "no"])

    higher = st.selectbox("Higher Education", ["yes", "no"])

    internet = st.selectbox("Internet Access", ["yes", "no"])

    romantic = st.selectbox("Romantic Relationship", ["yes", "no"])

    famrel = st.slider("Family Relationship", 1, 5, 3)

    freetime = st.slider("Free Time", 1, 5, 3)

    goout = st.slider("Going Out", 1, 5, 3)

    Dalc = st.slider("Weekday Alcohol", 1, 5, 1)

    Walc = st.slider("Weekend Alcohol", 1, 5, 1)

    health = st.slider("Health", 1, 5, 3)

    absences = st.slider("Absences", 0, 100, 5)

    G1 = st.slider("G1 Grade", 0, 20, 10)

    G2 = st.slider("G2 Grade", 0, 20, 10)

# ==========================
# DATAFRAME
# ==========================

input_data = pd.DataFrame({
    "school":[school],
    "sex":[sex],
    "age":[age],
    "address":[address],
    "famsize":[famsize],
    "Pstatus":[Pstatus],
    "Medu":[Medu],
    "Fedu":[Fedu],
    "Mjob":[Mjob],
    "Fjob":[Fjob],
    "reason":[reason],
    "guardian":[guardian],
    "traveltime":[traveltime],
    "studytime":[studytime],
    "failures":[failures],
    "schoolsup":[schoolsup],
    "famsup":[famsup],
    "paid":[paid],
    "activities":[activities],
    "nursery":[nursery],
    "higher":[higher],
    "internet":[internet],
    "romantic":[romantic],
    "famrel":[famrel],
    "freetime":[freetime],
    "goout":[goout],
    "Dalc":[Dalc],
    "Walc":[Walc],
    "health":[health],
    "absences":[absences],
    "G1":[G1],
    "G2":[G2]
})

# ==========================
# SAME ENCODING AS NOTEBOOK
# ==========================

cat_cols = input_data.select_dtypes(include="object").columns

for col in cat_cols:
    input_data[col] = input_data[col].astype("category").cat.codes

# ==========================
# PREDICT
# ==========================

if st.button("🎯 Predict Final Grade"):

    try:
        prediction = model.predict(input_data)[0]

        st.markdown(
            f"""
            <div class="result-box">
                Predicted G3 Score: {prediction:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"Error: {e}")