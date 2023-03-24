DROP TABLE IF EXISTS managers;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS evaluations;

CREATE TABLE managers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    picture VARCHAR(255),
    start_date DATE,
    end_date DATE,
    active BOOLEAN
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    picture VARCHAR(255),
    job_description VARCHAR(255),
    contact_details INT,
    qol_accommodations VARCHAR(255),
    start_date DATE,
    end_date DATE,
    active BOOLEAN,
    manager_id INT REFERENCES managers(id) 
);

-- CREATE TABLE evaluations (
--     id SERIAL PRIMARY KEY,
--     score FLOAT,
--     date DATE,
--     comment VARCHAR(255)
--     employee_id INT NOT NULL REFERENCES employees(id) ON DELETE CASCADE
-- );