# 🚀 Deploy to GitHub & Streamlit Cloud - RIGHT NOW

## What You Need

1. GitHub account (free at https://github.com)
2. Your GitHub username

## Step 1: Create GitHub Repository (2 mins)

1. Go to https://github.com/new
2. Fill in:
   - Repository name: `student-burnout-predictor`
   - Description: `Early detection of student burnout and dropout risk`
   - Select: **PUBLIC**
3. Click "Create repository"

## Step 2: Get Personal Access Token (2 mins)

1. Go to https://github.com/settings/tokens
2. Click "Generate new token"
3. Name: `streamlit-deploy`
4. Select scope: `repo`
5. Click "Generate token"
6. **Copy the token** (you'll need it in next step)

## Step 3: Push Code to GitHub (2 mins)

Replace `YOUR_USERNAME` with your GitHub username and `YOUR_TOKEN` with the token from Step 2:

```bash
cd /home/mokshith/burnout_project

git config user.name "Your Name"
git config user.email "your.email@example.com"

git remote add origin https://github.com/YOUR_USERNAME/student-burnout-predictor.git
git branch -M main
git push -u origin main
```

When prompted:
- Username: `YOUR_USERNAME`
- Password: Paste your `YOUR_TOKEN`

## Step 4: Verify on GitHub (1 min)

Go to: `https://github.com/YOUR_USERNAME/student-burnout-predictor`

You should see all your files there ✅

## Step 5: Deploy on Streamlit Cloud (2 mins)

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select:
   - Repository: `YOUR_USERNAME/student-burnout-predictor`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
5. Click "Deploy"

## Done! 🎉

Your app will be live at:
```
https://share.streamlit.io/YOUR_USERNAME/student-burnout-predictor/main/streamlit_app.py
```

---

## Troubleshooting

**Error: "fatal: remote origin already exists"**
```bash
git remote remove origin
# Then run the git remote add command again
```

**Error: "Authentication failed"**
- Make sure you're using a Personal Access Token, not your password
- Generate a new token at https://github.com/settings/tokens

**Streamlit Cloud won't deploy**
- Make sure `streamlit_app.py` exists in your repo
- Make sure `requirements.txt` has all dependencies
- Make sure `student_data.csv` and `.pkl` files are in the repo

---

## Your GitHub Link (After Step 4)

```
https://github.com/YOUR_USERNAME/student-burnout-predictor
```

## Your Streamlit App Link (After Step 5)

```
https://share.streamlit.io/YOUR_USERNAME/student-burnout-predictor/main/streamlit_app.py
```

**Use this link for submission!**
