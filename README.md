# Student Burnout & Dropout Risk Predictor

## Overview
This project implements a behavioral analytics system to predict student burnout and dropout risk early, enabling timely interventions.

## Problem Statement
Universities often identify academic issues only after performance drops. By analyzing behavioral signals such as LMS activity, submission patterns, and attendance, we can predict burnout risk before it becomes critical.

## Dataset

### Type: Synthetic
**Why**: No real behavioral dataset available for this use case.

**How Generated**: 
- Created 300 student records using Python with realistic behavioral patterns
- Rules-based approach: Risk scores calculated from behavioral indicators
- Distributions: 
  - LMS login frequency: 1-30 logins per week
  - Submission delays: 0-15 days
  - Attendance: 40-100%
  - Sentiment scores: -1 to 1
  - GPA: 1.5 to 4.0
  - Completion rate: 30-100%

**Features**:
1. `lms_login_frequency` - Weekly LMS logins (indicator of engagement)
2. `assignment_submission_delay_days` - Days late for submissions
3. `attendance_percentage` - Class attendance rate
4. `feedback_sentiment_score` - Sentiment from student feedback
5. `gpa` - Current GPA
6. `assignment_completion_rate` - Percentage of assignments completed

**Target Variable**: `burnout_risk` (Low/Medium/High)

## Feature Engineering

The burnout risk is determined by combining multiple behavioral signals:
- Low login frequency → High risk
- High submission delays → High risk
- Low attendance → High risk
- Negative sentiment → High risk
- Low GPA → High risk
- Low completion rate → High risk

## Model

**Algorithm**: Random Forest Classifier
- 100 decision trees
- Max depth: 10
- Random state: 42 (for reproducibility)

**Reasoning**: 
- Handles non-linear relationships between features
- Provides feature importance scores
- Robust to outliers
- Interpretable results

## Evaluation Metrics

- Classification Report (Precision, Recall, F1-Score)
- Confusion Matrix
- Feature Importance Analysis

## Project Structure

```
burnout_project/
├── data_generator.py      # Generate synthetic dataset
├── model.py               # Train ML model
├── app.py                 # Streamlit frontend
├── student_data.csv       # Generated dataset
├── burnout_model.pkl      # Trained model
├── feature_names.pkl      # Feature names
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate Data
```bash
python data_generator.py
```

### 3. Train Model
```bash
python model.py
```

### 4. Run Streamlit App
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## Features

### Prediction Page
- Input student behavioral data via sliders
- Get instant burnout risk prediction
- View probability distribution
- Receive personalized intervention recommendations

### Analytics Dashboard
- View overall risk distribution
- See feature importance
- Analyze behavioral patterns by risk level
- System-wide statistics

### About Page
- Understand the problem and solution
- Learn how the model works
- Review risk level definitions

## Deployment

### Deploy on Streamlit Cloud (Free)
1. Push code to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repo
4. Select `app.py` as main file
5. Deploy!

## Behavioral Insights

### High Risk Indicators
- LMS login frequency < 5 per week
- Assignment submission delays > 10 days
- Attendance < 60%
- Negative feedback sentiment
- GPA < 2.0
- Assignment completion < 50%

### Intervention Strategies
- **Engagement**: Increase LMS activity through reminders and support
- **Academic**: Provide tutoring and study groups
- **Emotional**: Offer counseling and mental health support
- **Administrative**: Flexible deadlines and attendance policies

## Assumptions

1. Behavioral patterns are predictive of burnout risk
2. All features are equally weighted in initial analysis
3. Synthetic data distribution reflects real student behavior
4. Risk categories are balanced across the dataset
5. No temporal dependencies (snapshot analysis)

## Future Improvements

- Incorporate temporal data (time-series analysis)
- Add real student data (with privacy protection)
- Implement deep learning models
- Add early warning system with notifications
- Include socioeconomic factors
- Develop personalized intervention recommendations

## Author
[I.Sri Mokshith]

## License
MIT
