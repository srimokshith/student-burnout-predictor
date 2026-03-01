import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

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

# Initialize session state for history tracking
if 'prediction_history' not in st.session_state:
    st.session_state.prediction_history = []

page = st.sidebar.radio("Select Page", ["Prediction", "Student Search", "Analytics Dashboard", "About"])

# ==================== PREDICTION PAGE ====================
if page == "Prediction":
    st.header("Individual Student Risk Assessment")
    
    view_mode = st.radio("Select View", ["Student View", "Faculty Dashboard"], horizontal=True)
    
    if view_mode == "Student View":
        col1, col2 = st.columns(2)
        
        with col1:
            lms_login = st.slider("LMS Login Frequency (per week)", 1, 30, 15)
            submission_delay = st.slider("Assignment Submission Delay (days)", 0, 15, 5)
            attendance = st.slider("Attendance Percentage (%)", 40, 100, 80)
        
        with col2:
            sentiment = st.slider("Feedback Sentiment Score", -1.0, 1.0, 0.0)
            gpa = st.slider("GPA", 1.5, 4.0, 3.0)
            completion_rate = st.slider("Assignment Completion Rate (%)", 30, 100, 75)
        
        col1, col2 = st.columns(2)
        with col1:
            predict_btn = st.button("Predict Burnout Risk", use_container_width=True)
        with col2:
            simulate_btn = st.button("What-If Simulator", use_container_width=True)
        
        if predict_btn:
            input_data = np.array([[lms_login, submission_delay, attendance, sentiment, gpa, completion_rate / 100]])
            
            prediction = model.predict(input_data)[0]
            probabilities = model.predict_proba(input_data)[0]
            risk_score = max(probabilities) * 100
            
            # Store in history
            st.session_state.prediction_history.append({
                'date': datetime.now(),
                'risk_score': risk_score,
                'prediction': prediction
            })
            
            st.markdown("---")
            
            # 1. BURNOUT METER GAUGE
            st.subheader("📊 Burnout Risk Meter")
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=risk_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Risk Score"},
                delta={'reference': 50},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 33], 'color': "lightgreen"},
                        {'range': [33, 66], 'color': "lightyellow"},
                        {'range': [66, 100], 'color': "lightcoral"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 90
                    }
                }
            ))
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # 2. RISK EXPLANATION PANEL
            st.markdown("---")
            st.subheader("🔎 Why This Student Is At Risk")
            
            reasons = []
            if lms_login < 5:
                reasons.append(("Low LMS Engagement", f"Only {lms_login} logins/week (recommended: 10+)"))
            if submission_delay > 10:
                reasons.append(("High Submission Delays", f"{submission_delay} days average delay"))
            if attendance < 60:
                reasons.append(("Low Attendance", f"Only {attendance}% attendance"))
            if sentiment < -0.3:
                reasons.append(("Negative Sentiment", "Concerning feedback tone detected"))
            if gpa < 2.0:
                reasons.append(("Low GPA", f"GPA: {gpa:.2f}"))
            if completion_rate < 50:
                reasons.append(("Low Completion Rate", f"Only {completion_rate}% assignments completed"))
            
            if reasons:
                for reason_title, reason_detail in reasons:
                    st.warning(f"⚠️ **{reason_title}**: {reason_detail}")
            else:
                st.success("✅ No major risk factors detected!")
            
            # 3. BURNOUT SCORE BREAKDOWN
            st.markdown("---")
            st.subheader("📈 Burnout Score Breakdown")
            
            breakdown = {
                'Academic Stress': min(100, (submission_delay / 15 * 100 + (100 - gpa / 4 * 100)) / 2),
                'Lifestyle Risk': min(100, (100 - attendance) + (100 - lms_login / 30 * 100)) / 2,
                'Mental Fatigue': min(100, max(0, -sentiment * 100 + 50)),
                'Social Isolation': min(100, (100 - completion_rate) / 2)
            }
            
            breakdown_df = pd.DataFrame(list(breakdown.items()), columns=['Factor', 'Score'])
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.barh(breakdown_df['Factor'], breakdown_df['Score'], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
            ax.set_xlabel('Score (%)')
            ax.set_title('Burnout Risk Breakdown by Factor')
            ax.set_xlim(0, 100)
            st.pyplot(fig)
            
            # 4. STUDENT PROFILE CLASSIFICATION
            st.markdown("---")
            st.subheader("👤 Student Profile Classification")
            
            if gpa > 3.5 and submission_delay > 8:
                profile = "🎯 Overworked Achiever"
                desc = "High performer but showing signs of overwork"
            elif lms_login < 5 and completion_rate < 50:
                profile = "🔕 Socially Isolated"
                desc = "Low engagement with coursework and peers"
            elif attendance < 70 and sentiment < -0.3:
                profile = "😰 Academically Stressed"
                desc = "Struggling with academic demands"
            elif attendance > 80 and gpa > 3.0 and completion_rate > 80:
                profile = "⚖️ Balanced Learner"
                desc = "Well-balanced academic and personal life"
            else:
                profile = "⚠️ At-Risk Student"
                desc = "Multiple concerning indicators"
            
            st.info(f"**{profile}**\n{desc}")
            
            # 5. PERSONAL IMPROVEMENT SUGGESTIONS
            st.markdown("---")
            st.subheader("🎯 Recommended Actions")
            
            suggestions = []
            if lms_login < 10:
                suggestions.append(("Increase LMS Engagement", "Log in at least 10 times per week"))
            if submission_delay > 5:
                suggestions.append(("Improve Time Management", "Aim for 2-3 days early submission"))
            if attendance < 80:
                suggestions.append(("Boost Attendance", "Attend at least 80% of classes"))
            if sentiment < -0.3:
                suggestions.append(("Seek Support", "Talk to counselor or peer mentor"))
            if gpa < 2.5:
                suggestions.append(("Academic Tutoring", "Join study groups or get tutoring"))
            if completion_rate < 80:
                suggestions.append(("Complete Assignments", "Aim for 90%+ completion rate"))
            
            if suggestions:
                suggestion_df = pd.DataFrame(suggestions, columns=['Issue', 'Suggestion'])
                st.dataframe(suggestion_df, use_container_width=True, hide_index=True)
            
            # 6. EARLY WARNING ALERT
            if len(st.session_state.prediction_history) > 1:
                st.markdown("---")
                prev_score = st.session_state.prediction_history[-2]['risk_score']
                curr_score = risk_score
                
                if curr_score > prev_score + 10:
                    st.error(f"🚨 **ALERT**: Burnout risk increased by {curr_score - prev_score:.1f}% compared to last assessment!")
                elif curr_score < prev_score - 10:
                    st.success(f"✅ **IMPROVEMENT**: Burnout risk decreased by {prev_score - curr_score:.1f}%!")
            
            # 7. BURNOUT HISTORY TRACKER
            st.markdown("---")
            st.subheader("📊 Your Burnout History")
            
            if len(st.session_state.prediction_history) > 1:
                history_df = pd.DataFrame(st.session_state.prediction_history)
                history_df['date'] = history_df['date'].dt.strftime('%Y-%m-%d %H:%M')
                
                fig, ax = plt.subplots(figsize=(10, 5))
                ax.plot(range(len(history_df)), history_df['risk_score'], marker='o', linewidth=2, markersize=8)
                ax.set_xlabel('Assessment Number')
                ax.set_ylabel('Risk Score (%)')
                ax.set_title('Burnout Risk Trend Over Time')
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
                
                st.dataframe(history_df, use_container_width=True, hide_index=True)
        
        if simulate_btn:
            st.markdown("---")
            st.subheader("⭐ What-If Simulator")
            st.info("Adjust the sliders below to see how changes would affect your burnout risk")
            
            col1, col2 = st.columns(2)
            with col1:
                sim_lms = st.slider("Simulated LMS Logins", 1, 30, lms_login, key="sim_lms")
                sim_delay = st.slider("Simulated Submission Delay", 0, 15, submission_delay, key="sim_delay")
                sim_attendance = st.slider("Simulated Attendance", 40, 100, attendance, key="sim_att")
            
            with col2:
                sim_sentiment = st.slider("Simulated Sentiment", -1.0, 1.0, sentiment, key="sim_sent")
                sim_gpa = st.slider("Simulated GPA", 1.5, 4.0, gpa, key="sim_gpa")
                sim_completion = st.slider("Simulated Completion Rate", 30, 100, completion_rate, key="sim_comp")
            
            sim_data = np.array([[sim_lms, sim_delay, sim_attendance, sim_sentiment, sim_gpa, sim_completion / 100]])
            sim_pred = model.predict(sim_data)[0]
            sim_probs = model.predict_proba(sim_data)[0]
            sim_score = max(sim_probs) * 100
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Current Risk Score", f"{risk_score:.1f}%")
            with col2:
                st.metric("Simulated Risk Score", f"{sim_score:.1f}%", delta=f"{sim_score - risk_score:.1f}%")
            
            if sim_score < risk_score:
                st.success(f"✅ These changes would **reduce** your burnout risk by {risk_score - sim_score:.1f}%!")
            elif sim_score > risk_score:
                st.warning(f"⚠️ These changes would **increase** your burnout risk by {sim_score - risk_score:.1f}%")
            else:
                st.info("These changes would keep your risk level the same")
    
    else:  # Faculty Dashboard
        st.subheader("👨‍🏫 Faculty Dashboard - Multiple Students Overview")
        
        df = pd.read_csv('student_data.csv')
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Students", len(df))
        with col2:
            high_risk = len(df[df['burnout_risk'] == 'High'])
            st.metric("High Risk", high_risk)
        with col3:
            medium_risk = len(df[df['burnout_risk'] == 'Medium'])
            st.metric("Medium Risk", medium_risk)
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        with col1:
            fig, ax = plt.subplots(figsize=(8, 5))
            risk_counts = df['burnout_risk'].value_counts()
            colors = {'Low': 'green', 'Medium': 'orange', 'High': 'red'}
            ax.pie(risk_counts.values, labels=risk_counts.index, autopct='%1.1f%%',
                   colors=[colors.get(x, 'gray') for x in risk_counts.index])
            ax.set_title('Risk Distribution')
            st.pyplot(fig)
        
        with col2:
            fig, ax = plt.subplots(figsize=(8, 5))
            feature_importance = model.feature_importances_
            ax.barh(features, feature_importance, color='steelblue')
            ax.set_xlabel('Importance')
            ax.set_title('Feature Importance')
            st.pyplot(fig)

# ==================== STUDENT SEARCH PAGE ====================
elif page == "Student Search":
    st.header("🔍 Individual Student Performance Dashboard")
    
    df = pd.read_csv('student_data.csv')
    
    col1, col2 = st.columns([3, 1])
    with col1:
        student_id = st.text_input("Enter Student ID", placeholder="e.g., 1, 2, 3...")
    with col2:
        search_btn = st.button("Search", use_container_width=True)
    
    if search_btn and student_id:
        try:
            student_id = int(student_id)
            student = df[df['student_id'] == student_id]
            
            if len(student) == 0:
                st.error(f"❌ Student ID {student_id} not found")
            else:
                student = student.iloc[0]
                
                st.markdown("---")
                st.subheader("1️⃣ Basic Details")
                
                col1, col2, col3, col4, col5 = st.columns(5)
                with col1:
                    st.metric("Student ID", student['student_id'])
                with col2:
                    st.metric("GPA", f"{student['gpa']:.2f}")
                with col3:
                    st.metric("Attendance", f"{student['attendance_percentage']:.1f}%")
                with col4:
                    st.metric("LMS Logins", f"{student['lms_login_frequency']:.0f}/week")
                with col5:
                    risk_color = {'Low': '🟢', 'Medium': '🟡', 'High': '🔴'}
                    st.metric("Risk Level", f"{risk_color.get(student['burnout_risk'], '⚪')} {student['burnout_risk']}")
                
                st.markdown("---")
                st.subheader("2️⃣ Performance Overview")
                
                # Create performance metrics
                metrics_data = {
                    'Metric': ['GPA', 'Attendance %', 'Completion Rate %', 'LMS Logins/week', 'Submission Delay (days)'],
                    'Value': [
                        student['gpa'],
                        student['attendance_percentage'],
                        student['assignment_completion_rate'] * 100,
                        student['lms_login_frequency'],
                        student['assignment_submission_delay_days']
                    ],
                    'Status': [
                        '✅' if student['gpa'] > 3.0 else '⚠️',
                        '✅' if student['attendance_percentage'] > 80 else '⚠️',
                        '✅' if student['assignment_completion_rate'] > 0.8 else '⚠️',
                        '✅' if student['lms_login_frequency'] > 10 else '⚠️',
                        '✅' if student['assignment_submission_delay_days'] < 5 else '⚠️'
                    ]
                }
                
                st.dataframe(pd.DataFrame(metrics_data), use_container_width=True, hide_index=True)
                
                st.markdown("---")
                st.subheader("📊 Trend Analysis")
                
                # Simulate trend data
                days = np.arange(0, 30, 5)
                gpa_trend = student['gpa'] + np.random.normal(0, 0.1, len(days))
                attendance_trend = student['attendance_percentage'] + np.random.normal(0, 2, len(days))
                delay_trend = student['assignment_submission_delay_days'] + np.random.normal(0, 1, len(days))
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    fig, ax = plt.subplots(figsize=(6, 4))
                    ax.plot(days, gpa_trend, marker='o', color='blue', linewidth=2)
                    ax.set_xlabel('Days')
                    ax.set_ylabel('GPA')
                    ax.set_title('📈 GPA Trend')
                    ax.grid(True, alpha=0.3)
                    st.pyplot(fig)
                
                with col2:
                    fig, ax = plt.subplots(figsize=(6, 4))
                    ax.plot(days, attendance_trend, marker='o', color='green', linewidth=2)
                    ax.set_xlabel('Days')
                    ax.set_ylabel('Attendance %')
                    ax.set_title('📊 Attendance Trend')
                    ax.grid(True, alpha=0.3)
                    st.pyplot(fig)
                
                with col3:
                    fig, ax = plt.subplots(figsize=(6, 4))
                    ax.plot(days, delay_trend, marker='o', color='red', linewidth=2)
                    ax.set_xlabel('Days')
                    ax.set_ylabel('Delay (days)')
                    ax.set_title('📅 Assignment Delay Trend')
                    ax.grid(True, alpha=0.3)
                    st.pyplot(fig)
                
                # Download Report
                st.markdown("---")
                st.subheader("📥 Download Report")
                
                report = f"""
STUDENT PERFORMANCE REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

STUDENT INFORMATION
Student ID: {student['student_id']}
Risk Level: {student['burnout_risk']}

PERFORMANCE METRICS
GPA: {student['gpa']:.2f}
Attendance: {student['attendance_percentage']:.1f}%
Assignment Completion Rate: {student['assignment_completion_rate']*100:.1f}%
LMS Login Frequency: {student['lms_login_frequency']:.0f} times/week
Assignment Submission Delay: {student['assignment_submission_delay_days']:.1f} days
Feedback Sentiment Score: {student['feedback_sentiment_score']:.2f}

RISK ASSESSMENT
Current Risk Level: {student['burnout_risk']}
Recommendation: {'Immediate intervention needed' if student['burnout_risk'] == 'High' else 'Monitor closely' if student['burnout_risk'] == 'Medium' else 'Student is on track'}

GENERATED BY: Student Burnout Predictor System
"""
                
                st.download_button(
                    label="📄 Download Report (TXT)",
                    data=report,
                    file_name=f"student_{student['student_id']}_report.txt",
                    mime="text/plain"
                )
                
                # JSON Report
                json_report = {
                    'student_id': int(student['student_id']),
                    'risk_level': student['burnout_risk'],
                    'metrics': {
                        'gpa': float(student['gpa']),
                        'attendance_percentage': float(student['attendance_percentage']),
                        'completion_rate': float(student['assignment_completion_rate']),
                        'lms_logins_per_week': float(student['lms_login_frequency']),
                        'submission_delay_days': float(student['assignment_submission_delay_days'])
                    },
                    'generated_at': datetime.now().isoformat()
                }
                
                st.download_button(
                    label="📊 Download Report (JSON)",
                    data=json.dumps(json_report, indent=2),
                    file_name=f"student_{student['student_id']}_report.json",
                    mime="application/json"
                )
        
        except ValueError:
            st.error("❌ Please enter a valid Student ID (number)")

# ==================== ANALYTICS DASHBOARD ====================
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
               colors=[colors.get(x, 'gray') for x in risk_counts.index])
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
            'Avg LMS Logins/week': f"{subset['lms_login_frequency'].mean():.1f}",
            'Avg Submission Delay (days)': f"{subset['assignment_submission_delay_days'].mean():.1f}",
            'Avg Attendance (%)': f"{subset['attendance_percentage'].mean():.1f}",
            'Avg GPA': f"{subset['gpa'].mean():.2f}",
            'Avg Completion Rate (%)': f"{subset['assignment_completion_rate'].mean() * 100:.1f}",
        }
        
        st.dataframe(pd.DataFrame([stats]).T, use_container_width=True)

# ==================== ABOUT PAGE ====================
else:
    st.header("ℹ️ About This System")
    
    st.markdown("""
    ### Problem Statement
    Universities often identify academic issues only after performance drops. This system uses behavioral analytics 
    to predict burnout and dropout risk early, enabling timely interventions.
    
    ### Key Features
    ✅ **Risk Prediction** - ML-based burnout risk classification
    ✅ **Explainable AI** - Understand why a student is at risk
    ✅ **What-If Simulator** - See how changes affect risk
    ✅ **Student Profiles** - Classify student types
    ✅ **History Tracking** - Monitor trends over time
    ✅ **Actionable Suggestions** - Personalized recommendations
    ✅ **Faculty Dashboard** - Multi-student overview
    ✅ **Performance Reports** - Downloadable student reports
    
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
    """)
