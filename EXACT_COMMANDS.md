# Exact Commands to Follow (Copy & Paste)

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

If that doesn't work, try:
```bash
pip3 install -r requirements.txt
```

## 2. Generate Data

```bash
cd /home/mokshith/burnout_project
python3 data_generator.py
```

Expected output:
```
Dataset created with 300 records
Burnout Risk Distribution:
burnout_risk
Medium    155
Low        76
High       69
```

## 3. Train Model

```bash
python3 model.py
```

Expected output:
```
Model Performance:
              precision    recall  f1-score   support
        High       0.82      0.64      0.72        14
         Low       0.91      0.56      0.69        18
      Medium       0.66      0.89      0.76        28

    accuracy                           0.73        60
```

## 4. Run Streamlit App

```bash
streamlit run app.py
```

Expected output:
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Then open: http://localhost:8501 in your browser

## 5. Setup GitHub (One-Time)

### 5a. Create GitHub Account (if you don't have one)
- Go to https://github.com/signup
- Create account with your email

### 5b. Create Repository
- Go to https://github.com/new
- Repository name: `student-burnout-predictor`
- Description: "Early detection of student burnout and dropout risk using behavioral analytics"
- Select **Public**
- Click "Create repository"

### 5c. Initialize Git Locally

```bash
cd /home/mokshith/burnout_project
git init
git add .
git commit -m "Initial commit: Student burnout prediction system"
```

### 5d. Connect to GitHub

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/student-burnout-predictor.git
git branch -M main
git push -u origin main
```

When prompted for password, use a Personal Access Token:
1. Go to https://github.com/settings/tokens
2. Click "Generate new token"
3. Select scopes: `repo`
4. Copy the token
5. Paste it when prompted for password

### 5e. Verify Upload

Go to: https://github.com/YOUR_USERNAME/student-burnout-predictor

You should see all your files there.

## 6. Deploy on Streamlit Cloud (Optional)

### 6a. Go to Streamlit Cloud
- Visit https://share.streamlit.io
- Sign in with GitHub

### 6b. Deploy App
- Click "New app"
- Select your repository: `student-burnout-predictor`
- Branch: `main`
- File path: `app.py`
- Click "Deploy"

Your app will be live at:
```
https://share.streamlit.io/YOUR_USERNAME/student-burnout-predictor/main/app.py
```

## 7. Create PowerPoint Presentation

Use Microsoft PowerPoint, Google Slides, or LibreOffice Impress:

1. Create 16 slides (follow `PRESENTATION_OUTLINE.md`)
2. Add screenshots from your Streamlit app
3. Include charts and visualizations
4. Save as PDF or PPTX
5. Keep it in your project folder

## 8. Final Submission

### What to Submit:
- GitHub Repository Link: `https://github.com/YOUR_USERNAME/student-burnout-predictor`

### Where to Submit:
- Follow your course instructions for submission portal
- Submit before: **March 1, 11:59 PM**

### What They'll Check:
- ✅ GitHub repo is public
- ✅ All code files present
- ✅ README.md is complete
- ✅ MODEL_EXPLANATION.md (5 pages)
- ✅ Code runs without errors
- ✅ Model makes sense
- ✅ App is interactive
- ✅ Documentation is clear

## Troubleshooting

### Problem: `command not found: streamlit`
**Solution**: Use full path
```bash
python3 -m streamlit run app.py
```

### Problem: `ModuleNotFoundError: No module named 'streamlit'`
**Solution**: Install dependencies
```bash
pip3 install -r requirements.txt
```

### Problem: `git: command not found`
**Solution**: Install git
```bash
sudo apt-get install git
```

### Problem: Can't push to GitHub
**Solution**: Use Personal Access Token instead of password
1. Go to https://github.com/settings/tokens
2. Generate new token with `repo` scope
3. Use token as password when pushing

### Problem: App crashes when running
**Solution**: Check if all files exist
```bash
ls -la /home/mokshith/burnout_project/
```

Should show:
- student_data.csv
- burnout_model.pkl
- feature_names.pkl

If missing, run:
```bash
python3 data_generator.py
python3 model.py
```

## Quick Reference

| Task | Command |
|------|---------|
| Install packages | `pip3 install -r requirements.txt` |
| Generate data | `python3 data_generator.py` |
| Train model | `python3 model.py` |
| Run app | `streamlit run app.py` |
| Initialize git | `git init` |
| Add files | `git add .` |
| Commit | `git commit -m "message"` |
| Push to GitHub | `git push -u origin main` |

## File Checklist

Before submitting, verify these files exist:

```
/home/mokshith/burnout_project/
├── app.py                    ✅
├── data_generator.py         ✅
├── model.py                  ✅
├── student_data.csv          ✅
├── burnout_model.pkl         ✅
├── feature_names.pkl         ✅
├── requirements.txt          ✅
├── README.md                 ✅
├── MODEL_EXPLANATION.md      ✅
├── QUICKSTART.md             ✅
├── BEGINNER_GUIDE.md         ✅
├── GITHUB_SETUP.md           ✅
├── PRESENTATION_OUTLINE.md   ✅
├── EXACT_COMMANDS.md         ✅
└── .gitignore                ✅
```

## You're All Set! 🚀

Follow these commands in order and you'll have:
1. ✅ Working app locally
2. ✅ Code on GitHub
3. ✅ Ready for submission

Good luck! 🎓
