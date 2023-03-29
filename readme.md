### Employee Management App

### To run the app locally
This app uses Flask, Jinja2, Python3 and PostgreSQL to run. It can be launched via a interface such as VSCode.
Open your terminal:
- ```create db [choicename]``` to create the database.
- ```psql -d employee_management -f db/employee_management.sql``` to create tables and populate with some prepared information.
- ```flask run``` to create the local server.
- The app will run on ```http://127.0.0.1:4999/``` on your browser.

## Brief

A [random company] has approached you to build a web application to help them manage their employees and managers. A manager may look after many employees at a time. An employee is registered with only one manager.

#### MVP

- The company wants to be able to register employees and their business relevant data. Important information for the manager to know is -
  - Name
  - Job description
  - Contact details
  - Performance evaluation
  - QoL accommodations
  - Start and end of employment dates 
- Be able to assign employees to managers
- CRUD actions for managers / employees - remember the user - what would they want to see on each View? What Views should there be?
- Display managers and their current team members

### Possible Extensions

- Assign monthly performance evaluations to employees (date/month, score, comment) - Complete
- Average performance evaluation scores and display comments (select by month/evaluation?) on each employee's page
- Display list of employees currently employed by the business (today's date is between start and end of employment?)
- Find employees and/or managers by name/job_description

### Consider for later
- Promote an employee to management track
- Display the lowest performing employees (bottom 30%?) in the past 3 months for focused support and coaching
- Add a way for employees to evaluate their managers?
- Prevent records deletion if less than 6 years have passed
