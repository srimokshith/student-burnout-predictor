# GitHub Setup Instructions

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `student-burnout-predictor`
3. Description: "Early detection of student burnout and dropout risk using behavioral analytics"
4. Select **Public** (required for submission)
5. Click "Create repository"

## Step 2: Initialize Local Git Repository

```bash
cd /home/mokshith/burnout_project
git init
git add .
git commit -m "Initial commit: Student burnout prediction system"
```

## Step 3: Connect to GitHub

Replace `<YOUR_USERNAME>` with your GitHub username:

```bash
git remote add origin https://github.com/<YOUR_USERNAME>/student-burnout-predictor.git
git branch -M main
git push -u origin main
```

## Step 4: Verify Repository

- Go to https://github.com/<YOUR_USERNAME>/student-burnout-predictor
- Verify all files are present:
  - ✅ README.md
  - ✅ data_generator.py
  - ✅ model.py
  - ✅ app.py
  - ✅ requirements.txt
  - ✅ MODEL_EXPLANATION.md
  - ✅ .gitignore

## Step 5: Deploy on Streamlit Cloud (Optional but Recommended)

1. Go to https://share.streamlit.io
2. Click "New app"
3. Select your GitHub repository
4. Branch: `main`
5. File path: `app.py`
6. Click "Deploy"

Your app will be live at: `https://share.streamlit.io/YOUR_USERNAME/student-burnout-predictor/main/app.py`

## Submission Checklist

- [ ] GitHub repository is public
- [ ] All code files are present
- [ ] README.md is complete
- [ ] MODEL_EXPLANATION.md (5 pages) is complete
- [ ] Dataset is generated and documented
- [ ] Model is trained and saved
- [ ] Streamlit app runs without errors
- [ ] Repository link is ready for submission
