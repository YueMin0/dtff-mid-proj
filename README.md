# dtff-mid-proj
This is a project for Digital Tools for Finance created by Yue Min.

There are in total five topics: 
1. Project environment: a function `create_dir.py` that creates a new directory of a given name in the project directory
   ![Alt Text](https://raw.githubusercontent.com/YueMin0/dtff-mid-proj/main/demo_materials/MidProj/create_dir.gif)
2. Version control with git: 
    1. Create a local repository for the project directory;
    2. Changes are committed and published to the remote repository;
    3. Merge changes from 2-person workflow
3. LaTex (folder `text/`): 
    1. A `.tex` file (`FirstLine.tex`) which produces a document with a single sentence is stored in subfolder `playground/`;
    2. `Reference - A Theory of Auctions and Competitive Bidding.bib` is auto-parsed by DOI using JabRef;
    3. A LaTex-produced article is stored in subfolder `paper/`;  
    4. A LaTex-produced beamer presentation is stored in subfolder `presentation/`
4. Data management
    1. A sample database, which consists last Starbuck's monthly stock price for last 60 months, is stored in folder `research_data/`;
    2. A database API is established using Python:
        - `__init__.py`
        - `utilities.py`: provides a data adapter converting other file types to `.csv`, test files are stored in subfolder `test_files/`
        - `downstream.py`: a function that extracts a subset from a database for usage in endpoint function
        - `upstream.py`: functions for overwirtting existing data, appending new data, and deleting data
5. Web API: a `jupyter notebook` in folder `web_api/` consists relevant exercises

