# Git & GitHub Cheat Sheet

## Initial Setup
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git init                    # Initialize a new repository
git clone <url>            # Clone an existing repository
```

## Basic Commands
```bash
git status                  # Check repository status
git add <file>             # Add file to staging area
git add .                  # Add all files to staging area
git commit -m "message"    # Commit staged changes
git push                   # Push commits to remote repository
git pull                   # Fetch and merge remote changes
```

## Branching
```bash
git branch                 # List branches
git branch <name>         # Create new branch
git checkout <branch>     # Switch to branch
git checkout -b <branch>  # Create and switch to new branch
git merge <branch>        # Merge branch into current branch
git branch -d <branch>    # Delete branch
```

## Remote Repository
```bash
git remote add origin <url>    # Add remote repository
git remote -v                  # List remote repositories
git push -u origin <branch>    # Push and set upstream branch
git fetch                      # Download remote changes without merging
git remote remove <name>       # Remove remote repository
```

## History & Differences
```bash
git log                    # View commit history
git log --oneline         # Compact commit history
git diff                  # Show unstaged changes
git diff --staged         # Show staged changes
git blame <file>          # Show who changed each line
```

## Undo Changes
```bash
git restore <file>        # Discard changes in working directory
git reset HEAD <file>     # Unstage file
git reset --soft HEAD~1   # Undo last commit, keep changes staged
git reset --hard HEAD~1   # Undo last commit and all changes
git revert <commit>       # Create new commit that undoes changes
```

## Stashing
```bash
git stash                 # Temporarily save changes
git stash list           # List stashed changes
git stash pop            # Apply and remove latest stash
git stash apply          # Apply latest stash without removing it
git stash drop           # Remove latest stash
```

## GitHub-Specific
```bash
# Fork Repository
# Click 'Fork' button on GitHub repository page

# Pull Requests
git checkout -b feature-branch
# Make changes
git push origin feature-branch
# Create PR on GitHub interface

# Sync Fork
git remote add upstream <original-repo-url>
git fetch upstream
git merge upstream/main
```

## Advanced
```bash
git rebase <branch>       # Reapply commits on top of another branch
git cherry-pick <commit>  # Apply specific commit to current branch
git tag <name>           # Create lightweight tag
git tag -a <name> -m "message"  # Create annotated tag
```

Would you like me to explain any of these commands in more detail?
