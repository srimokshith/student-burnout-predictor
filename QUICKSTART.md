# Quick Start Guide

## What You Have

✅ **Complete project with:**
- Synthetic dataset (300 student records)
- Trained ML model (Random Forest)
- Interactive Streamlit web app
- Full documentation
- Ready for GitHub deployment

## Run Locally (5 minutes)

### 1. Install Dependencies
```bash
cd /home/mokshith/burnout_project
pip install -r requirements.txt
```

### 2. Run the App
```bash
streamlit run app.py
```

### 3. Open Browser
Go to: `http://localhost:8501`

## What to Do Next

### Before Submission (by March 1, 11:59 PM)

1. **Create GitHub Repository**
   - Follow instructions in `GITHUB_SETUP.md`
   - Make it PUBLIC
   - Push all files

2. **Create PowerPoint Presentation**
   - Problem statement
   - Solution approach
   - Model architecture
   - Results & insights
   - Demo screenshots
   - Recommendations

3. **Verify Everything Works**
   - Run `streamlit run app.py` locally
   - Test all 3 pages (Prediction, Dashboard, About)
   - Try different input values

4. **Submit**
   - Copy GitHub repository link
   - Submit before 11:59 PM on March 1

## Project Structure

```
burnout_project/
├── data_generator.py          # Creates synthetic data
├── model.py                   # Trains ML model
├── app.py                     # Streamlit frontend
├── student_data.csv           # Generated dataset (300 records)
├── burnout_model.pkl          # Trained model
├── feature_names.pkl          # Feature names
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview
├── MODEL_EXPLANATION.md       # 5-page technical doc
├── GITHUB_SETUP.md           # GitHub instructions
└── QUICKSTART.md             # This file
```

## Key Features of Your App

### 🎯 Prediction Page
- Input student behavioral data
- Get instant risk prediction
- See probability distribution
- Get personalized recommendations

### 📊 Analytics Dashboard
- View overall risk distribution
- See feature importance
- Analyze patterns by risk level
- System statistics

### ℹ️ About Page
- Understand the problem
- Learn how the model works
- Review assumptions

## Model Performance

- **Accuracy**: 73%
- **High Risk Detection**: 82% precision
- **Training Data**: 300 synthetic records
- **Algorithm**: Random Forest (100 trees)

## Evaluation Criteria (What They're Grading)

✅ **Model Performance** - Your model achieves 73% accuracy
✅ **Feature Engineering** - 6 well-chosen behavioral features
✅ **Behavioral Insights** - Clear risk indicators and interventions
✅ **Practical Feasibility** - Uses realistic, available data
✅ **Clarity** - Well-documented code and explanations
✅ **Visualization** - Interactive dashboard with charts

## Common Issues & Solutions

**Issue**: `streamlit: command not found`
- Solution: Use `python3 -m streamlit run app.py`

**Issue**: `ModuleNotFoundError: No module named 'streamlit'`
- Solution: Run `pip install -r requirements.txt`

**Issue**: Model files not found
- Solution: Run `python3 data_generator.py` then `python3 model.py`

## Tips for Success

1. **Test everything locally first** before pushing to GitHub
2. **Keep code clean** - remove debug prints
3. **Document assumptions** - explain why you made each choice
4. **Use realistic data** - synthetic data should mimic real patterns
5. **Make it interactive** - Streamlit makes this easy
6. **Tell a story** - connect data → model → insights → recommendations

## Timeline

- **Now**: Run locally and verify everything works
- **Today/Tomorrow**: Create GitHub repo and push code
- **Before March 1**: Create PowerPoint presentation
- **March 1, 11:59 PM**: Submit GitHub link

You're all set! 🚀
