import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(42)

# Generate synthetic student data
n_students = 300

data = {
    'student_id': range(1, n_students + 1),
    'lms_login_frequency': np.random.randint(1, 30, n_students),  # logins per week
    'assignment_submission_delay_days': np.random.randint(0, 15, n_students),  # days late
    'attendance_percentage': np.random.randint(40, 100, n_students),  # 40-100%
    'feedback_sentiment_score': np.random.uniform(-1, 1, n_students),  # -1 to 1
    'gpa': np.random.uniform(1.5, 4.0, n_students),
    'assignment_completion_rate': np.random.uniform(0.3, 1.0, n_students),  # 30-100%
}

df = pd.DataFrame(data)

# Create burnout_risk based on behavioral patterns
def assign_burnout_risk(row):
    risk_score = 0
    
    # Low login frequency = high risk
    if row['lms_login_frequency'] < 5:
        risk_score += 3
    elif row['lms_login_frequency'] < 10:
        risk_score += 1
    
    # High submission delays = high risk
    if row['assignment_submission_delay_days'] > 10:
        risk_score += 3
    elif row['assignment_submission_delay_days'] > 5:
        risk_score += 1
    
    # Low attendance = high risk
    if row['attendance_percentage'] < 60:
        risk_score += 3
    elif row['attendance_percentage'] < 75:
        risk_score += 1
    
    # Negative sentiment = high risk
    if row['feedback_sentiment_score'] < -0.3:
        risk_score += 2
    
    # Low GPA = high risk
    if row['gpa'] < 2.0:
        risk_score += 2
    elif row['gpa'] < 2.5:
        risk_score += 1
    
    # Low completion rate = high risk
    if row['assignment_completion_rate'] < 0.5:
        risk_score += 3
    elif row['assignment_completion_rate'] < 0.7:
        risk_score += 1
    
    # Assign category
    if risk_score >= 8:
        return 'High'
    elif risk_score >= 4:
        return 'Medium'
    else:
        return 'Low'

df['burnout_risk'] = df.apply(assign_burnout_risk, axis=1)

# Save dataset
df.to_csv('/home/mokshith/burnout_project/student_data.csv', index=False)
print(f"Dataset created with {len(df)} records")
print(f"\nBurnout Risk Distribution:\n{df['burnout_risk'].value_counts()}")
print(f"\nFirst few rows:\n{df.head()}")
