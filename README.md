# Flask-web-application

This is a course work for Advanced programming (CS551P). 

This is a job searching website inspired by uk.indeed.com. I used an open dataset from kaggle.com. This dataset consists of 2500 job postings that were posted through the Armenian human resource portal CareerCenter. The data was extracted from the Yahoo! mailing group https://groups.yahoo.com/neo/groups/careercenter-am. This was the only online human resource portal in the early 2000s. 

A job posting usually has some structure, although some fields of the posting are not necessarily filled out by the client (poster). The data was cleaned and modified by removing posts that were not job related or had no structure. The data consists of job posts from 2004-2015. 

ACKNOWLEDGEMENT:

The data collection and initial research was funded by the American University of Armenia’s research grant (2015).source: https://www.kaggle.com/datasets/madhab/jobposts

SETTING UP THIS PROJECT:

Pull this Git repository into your system.

Load the application settings into your terminal and start the server with

    export FLASK_APP=app.py 
    export FLASK_ENV=development
    python3 -m flask run 
    Alternatively for codio python3 -m flask run -h 0.0.0.0

Find box name with Project->Box Name,then modify with port 5000. Then you can able to see the project running in a server.

HOW TO OPERATE AS A USER:

1. Use the search button to find a specific job based on location and position.
2. Once you find a job that suits you, click on the "Apply" button.
3. It will take you to application page. There you can see the details of the job and a application form.
4. Fill out the application form with appropriate details and format. 
5. It will then take you to a application successful page where you will be able to see your details with a message confirming that your application is successful.
6. click 'Back to Home' button to get back to the Home page.


