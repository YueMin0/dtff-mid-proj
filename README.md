# dtff-proj
This is a project for Digital Tools for Finance created by Yue Min. The structure of this repository follows the [Assignment](https://github.com/ipozdeev/digital-tools-for-finance#assignment) section of the course. (All topics are covered including the opional.)

## Summary

1. Project environment: a script, [`create_dir.py`](https://github.com/YueMin0/dtff-proj/blob/main/create_dir.py), that creates a new directory of a given name in the project directory
    * Demo:  
   ![Alt Text](https://raw.githubusercontent.com/YueMin0/dtff-proj/main/demo_materials/ProjDemo/create_dir.gif)
2. Version control with git: (see also [commit history](https://github.com/YueMin0/dtff-proj/commits/main))
    1. Create a local repository for the project directory;
    2. Changes are committed and published to the remote repository;
    3. Merge changes from 2-person workflow
   
   Version control (local and remote) | Collaboration part zoomed in
   :---------------------------------:|:-------------:
   ![](https://raw.githubusercontent.com/YueMin0/dtff-proj/main/demo_materials/ProjDemo/git_vc.png)|![](https://raw.githubusercontent.com/YueMin0/dtff-proj/main/demo_materials/ProjDemo/git_collab.png)
3. LaTeX projects (in folder [`text/`](https://github.com/YueMin0/dtff-proj/tree/main/text)): 
    1. A `.tex` file (`FirstLine.tex`) which produces a document with a single sentence is stored in subfolder `playground/`;
    2. `Reference - A Theory of Auctions and Competitive Bidding.bib` is auto-parsed by DOI using JabRef;
    3. A LaTex-produced [article](https://github.com/YueMin0/dtff-mid-proj/blob/main/text/paper/first_article.pdf) is stored in subfolder `paper/`;  
    4. A LaTex-produced [beamer presentation](https://github.com/YueMin0/dtff-mid-proj/blob/main/text/presentation/first_prez.pdf) is stored in subfolder `presentation/`, in which a heatmap table and a line plot (both produced by R) are presented
4. Data management (in folder [`data/`](https://github.com/YueMin0/dtff-proj/tree/main/data))
    1. A sample database, which contains Starbucks' monthly stock price for last 60 months, is stored in folder `research_data/`;
    2. A database API is established using Python:
        - `__init__.py`
        - `connect.py`: database authentication (in my case, it configures the environment variable to the data files folder)
        - `downstream.py`: a function that extracts a subset from a database for usage in endpoint function
        - `upstream.py`: functions for overwirtting existing data, appending new data, and deleting data
        - `utilities.py`: provides a data adapter converting other file types to `.csv`, test files are stored in subfolder `test_files/`
    3. The demo usage and test run of the database API can be found in the [data_management_demos](https://github.com/YueMin0/dtff-proj/tree/main/demo_materials/ProjDemo/data_management_demos).
5. Web API: a [jupyter notebook](https://github.com/YueMin0/dtff-mid-proj/blob/main/web_api/web_api.ipynb) in folder `web_api/` consists relevant exercises
6. An [`R shiny` app](https://github.com/YueMin0/dtff-proj/blob/main/shiny.R) presents interactively the worldwide progress of life expectancy and GDP per capita.
    * Demo:
    ![Alt Text](https://raw.githubusercontent.com/YueMin0/dtff-proj/main/demo_materials/ProjDemo/r_shiny.gif)

