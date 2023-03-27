DROP TABLE IF EXISTS evaluations;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS managers;

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
--     manager_id INT NOT NULL REFERENCES managers(id) ON DELETE CASCADE
-- );

INSERT INTO managers (name, picture, start_date, end_date, active) 
VALUES ('Lord Z', 'picture_placeholder', '2023-01-01', NULL, 't');

INSERT INTO managers (name, picture, start_date, end_date, active) 
VALUES ('Rita Repulsa', 'picture_placeholder', '2022-01-01', NULL, 't');

INSERT INTO managers (name, picture, start_date, end_date, active) 
VALUES ('Zordon', 'picture_placeholder', '2021-01-01', NULL, 't');

INSERT INTO managers (name, picture, start_date, end_date, active) 
VALUES ('King Mondo', 'picture_placeholder', '2021-01-01', '2022-02-02', 'f');

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Tommy Oliver', 'picture_placeholder', 'Multicolor ranger', 5554357, NULL, '2023-01-01', NULL, 't', 1);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Goldar', 'picture_placeholder', 'Gold goon', 5554357, NULL, '2023-01-01', NULL, 't', 2);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Finster', 'picture_placeholder', 'Mad scientist', 5554357, NULL, '2023-01-01', NULL, 't', 2);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Alpha 5', 'picture_placeholder', 'Karate Teacher', 5554357, NULL, '2023-01-01', NULL, 't', NULL);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Jason Lee Scott', 'picture_placeholder', 'Karate Teacher', 5554357, NULL, '2023-01-01', NULL, 't', 3);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Kimberley Hart', 'picture_placeholder', 'Gymnast', 5559999, NULL, '2023-02-01', NULL, 't', 3);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Billy Cranston', 'picture_placeholder', 'Tech Wiz', 5550001, NULL, '2023-01-20', NULL, 't', 3);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Trini Kwan', 'picture_placeholder', 'Rollerblader', 5550002, NULL, '2022-12-01', NULL, 't', 3);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Zack Taylor', 'picture_placeholder', 'Hip-hop artist', 5550003, NULL, '2022-11-01', NULL, 't', 3);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Adam Park', 'picture_placeholder', 'Dolphin trainer', 5550003, NULL, '2022-11-01', '2022-12-02', 'f', 3);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Queen Machina', 'picture_placeholder', 'Stay at home mom', 5550003, NULL, '2021-11-01', '2022-02-02', 'f', 4);

