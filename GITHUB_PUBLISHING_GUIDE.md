# GitHub Publishing Guide for Flashcard Creator

This guide will help you publish your Flashcard Creator application to GitHub with all the necessary files and documentation.

## 📋 Pre-Publishing Checklist

### ✅ Files Created
- [x] `README.md` - Comprehensive documentation
- [x] `LICENSE` - MIT License
- [x] `requirements.txt` - Python dependencies
- [x] `.gitignore` - Git ignore rules
- [x] `CONTRIBUTING.md` - Contribution guidelines
- [x] `sample_flashcards.md` - Example output
- [x] `setup.py` - Package setup
- [x] `publish_to_github.py` - Helper script
- [x] `run_flashcard_creator.bat` - Windows launcher
- [x] `run_flashcard_creator.sh` - Unix launcher
- [x] `.github/workflows/build.yml` - CI/CD pipeline

### 🔧 Files to Update
- [ ] Update `README.md` with your actual GitHub username
- [ ] Update `setup.py` with your name and email
- [ ] Update `publish_to_github.py` if needed

## 🚀 Step-by-Step Publishing Process

### 1. Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right → "New repository"
3. Name it `flashcard-creator` (or your preferred name)
4. Make it public
5. **Don't** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

### 2. Initialize Local Repository

```bash
# Navigate to your project directory
cd /path/to/your/flashcard-creator

# Initialize git repository
git init

# Add all files
git add .

# Make initial commit
git commit -m "Initial commit: Flashcard Creator for Obsidian"

# Add remote origin (replace with your actual repository URL)
git remote add origin https://github.com/YOUR_USERNAME/flashcard-creator.git

# Push to GitHub
git push -u origin main
```

### 3. Update Personal Information

**Update README.md:**
- Replace `yourusername` with your actual GitHub username
- Update any other personal information

**Update setup.py:**
- Change `author` to your name
- Change `author_email` to your email
- Update the repository URL

### 4. Create a Release

1. Go to your GitHub repository
2. Click "Releases" on the right side
3. Click "Create a new release"
4. Tag version: `v1.0.0`
5. Release title: `Flashcard Creator v1.0.0`
6. Description:
   ```
   ## What's New
   - Initial release of Flashcard Creator
   - Compatible with Obsidian's Space Repetition plugin
   - Clean, intuitive GUI interface
   - Support for Question First and Answer First formats
   
   ## Downloads
   - Windows: Download the .exe file
   - Source: Clone the repository and run with Python
   
   ## Installation
   See README.md for detailed installation instructions.
   ```
7. Upload your `templater.exe` file from the `dist/` folder
8. Click "Publish release"

### 5. Enable GitHub Actions

1. Go to your repository's "Actions" tab
2. The workflow should automatically run on your next push
3. This will build executables for different platforms

### 6. Add Repository Topics

Go to your repository settings and add these topics:
- `flashcards`
- `obsidian`
- `spaced-repetition`
- `anki`
- `education`
- `python`
- `desktop-app`
- `study-tools`

### 7. Create Issues Template

Create `.github/ISSUE_TEMPLATE/bug_report.md`:
```markdown
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 10, macOS 11, Ubuntu 20.04]
 - Python Version: [e.g. 3.8, 3.9, 3.10]
 - Flashcard Creator Version: [e.g. 1.0.0]

**Additional context**
Add any other context about the problem here.
```

## 🎯 Post-Publishing Tasks

### 1. Test Everything
- [ ] Test the executable download
- [ ] Test the installation instructions
- [ ] Test the sample flashcards in Obsidian
- [ ] Verify all links work

### 2. Promote Your Project
- [ ] Share on Reddit (r/ObsidianMD, r/Anki, r/Python)
- [ ] Share on Discord (Obsidian community)
- [ ] Share on Twitter/other social media
- [ ] Consider creating a YouTube demo video

### 3. Monitor and Maintain
- [ ] Respond to issues and pull requests
- [ ] Update documentation as needed
- [ ] Consider adding new features based on feedback

## 🔧 Using the Helper Script

You can also use the included helper script:

```bash
python publish_to_github.py
```

This script will:
- Check if git is installed
- Initialize the repository
- Add and commit files
- Help you set up the remote origin
- Push to GitHub

## 📝 Additional Tips

### Screenshots and GIFs
Consider adding:
- Screenshot of the main interface
- GIF showing the workflow
- Screenshot of the generated markdown in Obsidian

### Documentation
- Keep the README updated
- Add troubleshooting section if needed
- Consider creating a wiki for advanced usage

### Version Management
- Use semantic versioning (1.0.0, 1.1.0, etc.)
- Create changelog for each release
- Tag releases properly

## 🎉 Congratulations!

Once you've completed these steps, your Flashcard Creator will be live on GitHub and available to the Obsidian community. The comprehensive documentation and professional setup will help users discover and use your tool effectively.

**Happy publishing! 🚀** 