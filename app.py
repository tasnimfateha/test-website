from flask import Flask, render_template, request
from database import job_list, job_details, addApplication, search_jobs
from flask_paginate import Pagination, get_page_parameter

app = Flask(__name__)

db_name = 'job.db'

@app.route("/")
def index():
  jobs= job_list()
  return render_template('index.html', jobs=jobs)

@app.route('/job/<int:id>/apply')
def show_job(id):
  job = job_details(id)
  
  if not job:
    return "Not Found", 404
  
  return render_template('jobpage.html', 
                         job=job)

@app.route("/job/<id>/apply", methods=['post'])
def applyJob(id):
  data = request.form
  job = job_details(id)
  addApplication(id, data)
  return render_template('applicationSubmitted.html', 
                         application=data,
                         job=job)

@app.route('/search', methods=['POST'])
def search_jobs_route():
    position = request.form['position']
    location = request.form['location']
    jobs = search_jobs(position, location)
    return render_template('index.html', jobs=jobs)

@app.route('/jobs')
def jobs():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 10
    total = len(job_list())
    pagination = Pagination(page=page, total=total, per_page=per_page)
    jobs = job_list()[pagination.offset: pagination.offset +      pagination.per_page]
    return render_template('jobitem.html', jobs=jobs, pagination=pagination)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug= True)