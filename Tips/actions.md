Quick Reference Guide for Git Commands
Here are the essential Git commands you'll use frequently to manage your code.
Command	Description
git clone [url]	Creates a local copy of a remote repository.
git add [file]	Stages a specific file, preparing it for a commit.
git add .	Stages all new and modified files in the current directory.
git commit -m "[message]"	Records the staged changes to the local repository with a descriptive message.
git push	Uploads your committed changes from your local repository to the remote repository.
git pull	Fetches changes from the remote repository and merges them into your current local branch.
git status	Displays the state of your working directory and staging area, showing which files are modified, staged, or untracked.
git branch	Lists all of the branches in your repository.
git branch [branch-name]	Creates a new branch.
git checkout [branch-name]	Switches to the specified branch.
git merge [branch-name]	Merges the specified branch's history into the current branch.
Understanding the GitHub Flow
A common and effective way to use these commands is to follow the GitHub Flow. This involves these general steps:
Create a Branch: Before making changes, create a new branch to work on. This keeps your changes isolated from the main codebase.
git checkout -b new-feature (This creates a new branch and switches to it)
Make and Commit Changes: Make your desired changes to the code. Then, stage and commit them.
git add .
git commit -m "Add new feature"
Push to the Remote Repository: Push your new branch and its commits to GitHub.
git push origin new-feature
Open a Pull Request: On GitHub, open a pull request. This is a formal way to propose your changes and ask for them to be reviewed before they are merged into the main branch.
Merge: Once the pull request is approved, you can merge it into the main branch on GitHub.
Update Your Local Repository: After merging, switch back to your main branch and pull the latest changes.
git checkout main
git pull
GitHub Actions: The Automation Aspect
While you perform the Git commands above manually, GitHub Actions can automate tasks that happen after you push your code to the repository.
Think of it this way:
You use git push to send your code to GitHub.
GitHub Actions sees that push and can automatically run tests, build your project, or even deploy it to a server.
You configure this automation by creating a .yml file in a .github/workflows directory in your repository. This file defines what events trigger the actions (like a push or a pull request) and what jobs to run.