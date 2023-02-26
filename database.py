import csv
import sqlite3

# connecting to the database
connection = sqlite3.connect('job.db')

# Creating a cursor object to execute SQL queries on a database table
cursor = connection.cursor()

# Drop table if exists
cursor.execute('DROP TABLE IF EXISTS allJob')

# Table Definition
# Table Definition
create_job_table = '''CREATE TABLE allJob(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              Title TEXT,
              Company TEXT,
              Location TEXT,
              JobDescription TEXT);'''

# Creating the table into our database
cursor.execute(create_job_table)

# Opening the data.csv file
file = open('data.csv')

# Reading the contents of the data.csv file
contents = csv.reader(file)

# SQL query to insert data into the allJob table
insert_job = "INSERT INTO allJob (Title,Company,Location,JobDescription) VALUES (?,?,?,?)"

# Importing the contents of the file into our allJob table
cursor.executemany(insert_job, contents)


# Drop table if exists
cursor.execute('DROP TABLE IF EXISTS applications')

# Table Definition
create_application_table = '''CREATE TABLE applications (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 job_id INTEGER,
                 full_name TEXT,
                 email TEXT,
                 linkedin_url TEXT,
                 education TEXT,
                 work_experience TEXT,
                 FOREIGN KEY(job_id) REFERENCES allJob(id))'''

cursor.execute(create_application_table)
# SQL query to retrieve all data from the allJob table
def job_list():
    connection = sqlite3.connect('job.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    select_all = "SELECT * FROM allJob"
    rows = cursor.execute(select_all).fetchall()
    jobs = []

    # Output to the console screen
    for r in rows:
        jobs.append(dict(r))
    return jobs

# Get job by ID
def job_details(id):
    connection = sqlite3.connect('job.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    result = cursor.execute("SELECT * FROM allJob WHERE id = ?", (id,))
    row = result.fetchone()
    if row is None:
        return None
    else:
        return dict(row)

def addApplication(job_id, data):
    connection = sqlite3.connect('job.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    query = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(query, (
            job_id,
            data['full_name'],
            data['email'],
            data['linkedin_url'],
            data['education'],
            data['work_experience'],
        ))

def search_jobs(position, location):
    connection = sqlite3.connect('job.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM allJob WHERE Title LIKE ? AND Location LIKE ?", ('%'+position+'%', '%'+location+'%'))
    rows = cursor.fetchall()
    jobs = []
    for r in rows:
        jobs.append(dict(r))
    return jobs

# Committing the changes
connection.commit()

# closing the database connection
connection.close()