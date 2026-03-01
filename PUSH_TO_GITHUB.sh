#!/bin/bash

# Replace YOUR_USERNAME with your actual GitHub username
USERNAME="YOUR_USERNAME"
REPO_NAME="student-burnout-predictor"

echo "🚀 Pushing to GitHub..."
echo "Username: $USERNAME"
echo "Repository: $REPO_NAME"
echo ""

# Set git config
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add remote
git remote add origin https://github.com/$USERNAME/$REPO_NAME.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main

echo ""
echo "✅ Done! Your repository is at:"
echo "https://github.com/$USERNAME/$REPO_NAME"
