import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Burnout Predictor", layout="wide")
st.title("🎓 Student Burnout & Dropout Risk Predictor")
st.markdown("---")

@st.cache_resource
def load_model():
    with open('burnout_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('feature_names.pkl', 'rb') as f:
        features = pickle.load(f)
    return model, features

model, features = load_model()

page = st.sidebar.radio("Select Page", ["Prediction", "Analytics Dashboard", "About"])

if page == "Prediction":
    st.header("Individual Student Risk Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        lms_login = st.slider("LMS Login Frequency (per week)", 1, 30, 15)
        submission_delay = st.slider("Assignment Submission Delay (days)", 0, 15, 5)
        attendance = st.slider("Attendance Percentage (%)", 40, 100, 80)
    
    with col2:
        sentiment = st.slider("Feedback Sentiment Score", -1.0, 1.0, 0.0)
        gpa = st.slider("GPA", 1.5, 4.0, 3.0)
        completion_rate = st.slider("Assignment Completion Rate (%)", 30, 100, 75)
    
    if st.button("Predict Burnout Risk"):
        input_data = np.array([[lms_login, submission_delay, attendance, sentiment, gpa, completion_rate / 100]])
        
        prediction = model.predict(input_data)[0]
        probabilities = model.predict_proba(input_data)[0]
        
        st.markdown("---")
        col1, col2 = st.columns([1, 2])
        
        with col1:
            if prediction == "High":
                st.error(f"⚠️ Risk Level: {prediction}")
            elif prediction == "Medium":
                st.warning(f"⚠️ Risk Level: {prediction}")
            else:
                st.success(f"✅ Risk Level: {prediction}")
        
        with col2:
            risk_probs = pd.DataFrame({
                'Risk Level': ['Low', 'Medium', 'High'],
                'Probability': probabilities
            })
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.barh(risk_probs['Risk Level'], risk_probs['Probability'], color=['green', 'orange', 'red'])
            ax.set_xlabel('Probability')
            ax.set_title('Risk Level Probabilities')
            st.pyplot(fig)
        
        st.markdown("---")
        st.subheader("📋 Intervention Recommendations")
        
        recommendations = []
        if lms_login < 5:
            recommendations.append("🔴 Increase LMS engagement - Student is logging in very infrequently")
        if submission_delay > 10:
            recommendations.append("🔴 Address submission delays - Student is consistently late with assignments")
        if attendance < 60:
            recommendations.append("🔴 Improve attendance - Student is missing many classes")
        if sentiment < -0.3:
            recommendations.append("🟡 Provide emotional support - Negative feedback sentiment detected")
        if gpa < 2.0:
            recommendations.append("🟡 Academic tutoring needed - GPA is below 2.0")
        if completion_rate < 0.5:
            recommendations.append("🔴 Increase assignment completion - Student is completing less than 50% of assignments")
        
        if recommendations:
            for rec in recommendations:
                st.write(rec)
        else:
            st.success("✅ No immediate interventions needed - Student appears to be on track")

elif page == "Analytics Dashboard":
    st.header("📊 System Analytics Dashboard")
    
    df = pd.read_csv('student_data.csv')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Students", len(df))
    with col2:
        high_risk = len(df[df['burnout_risk'] == 'High'])
        st.metric("High Risk Students", high_risk, f"{high_risk/len(df)*100:.1f}%")
    with col3:
        medium_risk = len(df[df['burnout_risk'] == 'Medium'])
        st.metric("Medium Risk Students", medium_risk, f"{medium_risk/len(df)*100:.1f}%")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig, ax = plt.subplots(figsize=(8, 5))
        risk_counts = df['burnout_risk'].value_counts()
        colors = {'Low': 'green', 'Medium': 'orange', 'High': 'red'}
        ax.pie(risk_counts.values, labels=risk_counts.index, autopct='%1.1f%%',
               colors=[colors[x] for x in risk_counts.index])
        ax.set_title('Burnout Risk Distribution')
        st.pyplot(fig)
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 5))
        feature_importance = model.feature_importances_
        ax.barh(features, feature_importance, color='steelblue')
        ax.set_xlabel('Importance Score')
        ax.set_title('Feature Importance in Prediction')
        st.pyplot(fig)
    
    st.markdown("---")
    st.subheader("📈 Behavioral Patterns by Risk Level")
    
    for risk_level in ['Low', 'Medium', 'High']:
        subset = df[df['burnout_risk'] == risk_level]
        st.write(f"**{risk_level} Risk Students (n={len(subset)})**")
        
        stats = {
            'Avg LMS Logins/week': subset['lms_login_frequency'].mean(),
            'Avg Submission Delay (days)': subset['assignment_submission_delay_days'].mean(),
            'Avg Attendance (%)': subset['attendance_percentage'].mean(),
            'Avg GPA': subset['gpa'].mean(),
            'Avg Completion Rate (%)': subset['assignment_completion_rate'].mean() * 100,
        }
        
        st.dataframe(pd.DataFrame([stats]).T, use_container_width=True)

else:
    st.header("ℹ️ About This System")
    
    st.markdown("""
    ### Problem Statement
    Universities often identify academic issues only after performance drops. This system uses behavioral analytics 
    to predict burnout and dropout risk early, enabling timely interventions.
    
    ### How It Works
    The system analyzes 6 key behavioral indicators:
    - **LMS Login Frequency**: How often students access the learning management system
    - **Assignment Submission Delays**: How late students submit assignments
    - **Attendance Percentage**: Class attendance rate
    - **Feedback Sentiment**: Emotional tone in student feedback
    - **GPA**: Academic performance
    - **Assignment Completion Rate**: Percentage of assignments completed
    
    ### Model
    - **Algorithm**: Random Forest Classifier
    - **Training Data**: 300 synthetic student records
    - **Output**: Risk classification (Low/Medium/High) with probability scores
    
    ### Risk Levels
    - **Low Risk**: Student is engaged and performing well
    - **Medium Risk**: Some concerning behavioral patterns detected
    - **High Risk**: Multiple warning signs - immediate intervention recommended
    
    ### Data
    This system uses synthetically generated data based on realistic behavioral patterns.
    """)
