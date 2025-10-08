# 1. Git vs. GitHub:
# Git is a version control system that tracks changes in your code locally on your computer.
# GitHub is an online platform that hosts Git repositories and allows sharing and collaboration with others.
# 2. Terminal vs. Command Line:
# The terminal is the program that lets you type text commands to interact with your computer.
# The command line is the actual interface where you enter those commands to run programs or navigate files.
# 3. Local vs. Remote Repository:
# A local repository exists on your own computer where you make and test changes.
# A remote repository is stored online
# 4. Version Control:
# Version control is a system that records changes to files over time, allowing you to revert to earlier versions and collaborate safely.
# 5. Staging Area:
# The staging area is where you place changes before committing them to the repository—it’s like a holding zone for edits you want to save.
# 6. git add:
# Adds changes in your working directory to the staging area, preparing them to be committed.
# 7. git commit:
# Saves a snapshot of the staged changes to the repository’s history with a message describing what you did.
# 8. git push:
# Uploads your local commits to a remote repository so they’re saved and shared online.
# 9. git status:
# Shows the current state of your working directory
# 10. git pull:
# Gets changes from the remote repository into your local repository.
# 11. pwd:
# Shows the full path of the directory you’re currently in.
# 12. ls:
# Lists the files and folders in the current directory.
# 13. cd:
# Stands for “change directory” and lets you move between folders in the file system.
# 14. nano:
# Opens a simple text editor in the terminal so you can create or edit files directly.
# 15. touch:
# Creates a new, empty file (or updates the timestamp of an existing one).
# 16. mv:
# Moves or renames a file or folder.
# 17. rm:
# Deletes a file
# 18. cat:
# Displays the contents of a file in the terminal window.

# Questions: 
# 1) pwd
# 2) ls
# 3) cd ../brianna_repo
#  git pull
# 4) mv homework.py ../judy_decal/homework/
# 5) cd ../judy_decal/homework
# 6) cat homework.py
# 7) git add .
# git commit -m "Finished homework"
# git push
# 8) git pull --rebase
# git push
# 9) cd ~/Recent

def check_Data_type (input):
    return(print(type(input)))

#check_Data_type(3.14)

def evenOrOdd(n):
    if n % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def duplicateList(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
        new_list.append(item)
    return new_list

# this function needs a colon at the end
def square(num):
    return num * num

print(evenOrOdd(7)) 



