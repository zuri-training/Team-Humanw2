# Team-Humanw2

<details><summary><h2>Table of Contents</h2></summary>

* [Project Title](#Project-Title)
* [Project Description](#project-description)
* [Resource](#resource)
* [Website Features](#website-features)
* [Technologies Used](#technologies-used)
* [Project Status](#project-status)
* [Collaboration Guide](#collaboration-guide)</details>

## Project Title
cc-gen

## Project Description
    A library of different types of credit card designs

## Resource
* [Product Documentation](https://docs.google.com/document/d/15_CW3yIrWMxepYVp_7WHOLzd5md7q2thjMBgyGg_PrE/edit?usp=sharing)
* [Figma](https://www.figma.com/file/vHvm0LLeEOO2wDEw9tMcG7/Team-Humanw2-CC_gen?node-id=0%3A1&t=z3IEJkfp8tAnV9JV-1)
* [Database Schema](https://www.figma.com)

## Website Features

Unauthenticated Users;

* Visit the platform to view basic information about the platform
* View and interacts with documentation
* Able to view but can't download from the library

Authenticated Users;
* Access to all the Unauthenticated user features.
* Users can download credit card code sample
* Users can see usage sample
* Users can comment under a design, react and share on social media
* Downloaded cc design should come with all files (hence, download should be a compressed format)
* Allow user save data and come back to download

## Technologies Used
* Design: <a href="https://www.figma.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/figma-colored.svg" width="36" height="36" alt="Figma" /></a>
* Frontend: <a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/html5-colored.svg" width="36" height="36" alt="HTML5" /></a>
	<a href="https://www.w3.org/TR/CSS/#css" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/css3-colored.svg" width="36" height="36" alt="CSS3" /></a>
	<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/javascript-colored.svg" width="36" height="36" alt="JavaScript" /></a>
* Backend: <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a>
   <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"><img src="https://verbose-equals-true.gitlab.io/django-postgres-vue-gitlab-ecs/django.jpg" width="36" height="36" alt="Django"/></a>
* Version Control System: <a href="https://www.github.com/" target="_blank" rel="noreferrer"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="36" height="36" alt="Github"/></a>

## Project Status
 _ongoing_
 
## Collaboration Guide
For TeamQuail members, follow the following steps to collaborate:
1. Visit the Repository to the Project on Github Website: "https://github.com/zuri-training/Team-Humanw2.git" <br/>
2. Fork the repository: Click the "Fork" button on the upper right corner of the Repo page.* <br/>
3. Make a local clone: 
     Click on the "Code" button on the Repo page 
     Copy the URL for the forked Repo "https://github.com/zuri-training/Team-Humanw2.git" 
     Create a Folder on your Local machine / Computer for the project Workspace <br/>
     Open Command prompt / Terminal in the same folder location <br/>
     In your Terminal, type: <br/>
        `git clone https://github.com/zuri-training/Team-Humanw2.git`
4. Open terminal and set upstream branch: <br/>
    `git remote add upstream https://github.com/zuri-training/Team-Humanw2.git`
5. Pull upstream to get up to date with the original repo:<br/>
    `git pull upstream main`
6. Create a new branch for the task you are working on :<br/>
    `git checkout -b branchName`<br/>
    *(Make sure your branchName is descriptive in context to the feature you are working on. Also be sure to check which branch you are on using `git status` before you begin working)*
7. When you're done with your task, do:<br/>
    `git add`<br/>
   - Commit your work with a message:<br/>
   `git commit -m "message"`
8. To avoid conflicts:<br/>
    `git pull upstream main`
9. Then push your branch:<br/>
    `git push origin branchName` - This creates the branch remotely and pushes to that branch on the Github
10. Go to Github and create a new pull request to the main branch. It will then be reviewed and merged into the master.
