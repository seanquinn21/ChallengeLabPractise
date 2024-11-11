# Task 1: Run `eduroam-linux-UoG.py` to connect Raspberry Pi to Eduroam.
# Run this Python script in the terminal to connect to Eduroam.
python3 eduroam-linux-UoG.py

# Task 2: Set up Git credentials.
# This sets the name and email for Git commits.
git config --global user.name "YourName"
git config --global user.email "your.email@university.com"

# Task 3: Clone the Lab 1 repository into the `ee347` folder.
# Replace the repository URL with the actual GitHub Classroom link.
mkdir -p ~/ee347  # Creates the `ee347` directory if it doesn't exist
cd ~/ee347        # Navigate into the `ee347` folder
git clone <Lab1-Repository-URL> lab1  # Clones into the `lab1` folder

# Task 4: Create the specified file and folder structure.
# Navigates into the `lab1` directory, where we'll create the folder structure.
cd lab1
# Creates a new folder named `folder_a` inside `lab1`.
mkdir folder_a
# Creates a nested folder `folder_b` inside `folder_a`.
mkdir folder_a/folder_b
# Creates three text files: `file_a.txt` in `lab1`, `file_b.txt` in `folder_a`, 
# and `file_c.txt` in `folder_a`, as well as `file_d.txt` inside `folder_b`.
# These files are created using `touch`, which is a command to create empty files.
touch file_a.txt folder_a/file_b.txt folder_a/file_c.txt folder_a/folder_b/file_d.txt


# Task 5: Add `file_c.txt` to `.gitignore`.
# Open `.gitignore` (create it if it doesn't exist) and add the following line:
echo "folder_a/file_c.txt" >> .gitignore  # Appends file path to `.gitignore`
git add .gitignore
git commit -m "Task 5: Add file_c.txt to .gitignore"
git push origin main

# Task 6: Create and switch to a new branch called `new-branch`.
# Make the file structure changes on this branch.
git checkout -b new-branch  #Creates and switches to `new-branch`
mkdir folder_a/folder_c
mv folder_a/file_b.txt folder_a/folder_c/  # Moves `file_b.txt` to `folder_c` 
git add . 
git commit -m "Task 6: Restructure file organization" 
git push origin new-branch 

# Task 7: Edit `file_b.txt` to add team members' names.
# Open `file_b.txt` in any editor, add names, and commit.
echo -e "Team Member 1\nTeam Member 2" > folder_a/folder_c/file_b.txt
git add folder_a/folder_c/file_b.txt
git commit -m "Task 7: Add team member names to file_b.txt"
git push origin new-branch

# Task 8: Revert the changes from task 7.
# `git revert` creates a new commit that undoes the previous commit.
git revert HEAD  # Reverts the last commit (Task 7 changes)

# Task 9: Merge `new-branch` into the master branch.
# First, switch back to `main`, then merge `new-branch`.
git checkout main
git merge new-branch
git push origin main  # Pushes the merged changes to GitHub

# Task 10: Push all changes to GitHub to complete.
# This is a final push to ensure all work is updated in GitHub.
git push origin main
