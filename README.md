2️⃣ Open Terminal / PowerShell in Your Project Folder

Navigate to your local project directory:

cd path\to\your\project


Example:

cd C:\Users\Monesha\Documents\my-project

3️⃣ Initialize Git (if not already)
git init

4️⃣ Check Git Status
git status

5️⃣ Add Files to Git

Add everything:

git add .


Or add specific files:

git add filename.ext

6️⃣ Commit Changes
git commit -m "Initial commit"

7️⃣ Add GitHub Remote Repository

Copy the HTTPS URL from GitHub (looks like below):

https://github.com/username/repository-name.git


Then run:

git remote add origin https://github.com/username/repository-name.git


Verify:

git remote -v

8️⃣ Push Local Code to GitHub

If your branch is main:

git branch -M main
git push -u origin main


If your branch is master:

git push -u origin master
