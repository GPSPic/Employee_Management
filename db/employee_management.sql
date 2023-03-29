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
    manager_id INT REFERENCES managers(id) ON DELETE SET NULL
);

CREATE TABLE evaluations (
    id SERIAL PRIMARY KEY,
    score FLOAT,
    date DATE,
    comment VARCHAR(255),
    employee_id INT NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    manager_id INT REFERENCES managers(id) ON DELETE SET NULL
);

INSERT INTO managers (name, picture, start_date, end_date, active) 
VALUES ('Lord Z', 'http://3.bp.blogspot.com/-0VoCeFGHHME/VeUjPchytgI/AAAAAAAADE0/JRFtSedhGgs/s1600/Bored%2BZedd.PNG', '2023-01-01', NULL, 't');

INSERT INTO managers (name, picture, start_date, end_date, active) 
VALUES ('Rita Repulsa', 'https://comicvine.gamespot.com/a/uploads/scale_medium/3/30334/1115423-powerranger2486.jpg', '2022-01-01', NULL, 't');

INSERT INTO managers (name, picture, start_date, end_date, active) 
VALUES ('Zordon', 'https://upload.wikimedia.org/wikipedia/en/b/bc/Zordon_power_rangers.jpg', '2021-01-01', NULL, 't');

INSERT INTO managers (name, picture, start_date, end_date, active) 
VALUES ('King Mondo', 'https://morphinlegacy.com/wp-content/uploads/2022/09/King-Mondo.png', '2021-01-01', '2022-02-02', 'f');

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Tommy Oliver', 'picture_placeholder', 'Multicolor ranger', 5554357, NULL, '2023-01-01', NULL, 't', 1);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Goldar', 'picture_placeholder', 'Gold goon', 5554357, NULL, '2023-01-01', NULL, 't', 2);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Finster', 'picture_placeholder', 'Mad scientist', 5554357, NULL, '2023-01-01', NULL, 't', 2);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Alpha 5', 'picture_placeholder', 'Doomsayer', 5554357, NULL, '2023-01-01', NULL, 't', NULL);

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
VALUES ('Adam Park', 'picture_placeholder', 'Dolphin trainer', 5550003, NULL, '2022-11-01', '2022-12-02', 'f', NULL);

INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
VALUES ('Queen Machina', 'picture_placeholder', 'Stay at home mom', 5550003, NULL, '2021-11-01', '2022-02-02', 'f', NULL);

INSERT INTO evaluations (score, date, comment, employee_id, manager_id)
VALUES (100, '2023-03-01', 'Great work, keep it up', 1, 1);

INSERT INTO evaluations (score, date, comment, employee_id, manager_id)
VALUES (75, '2023-02-01', 'Could use more evil', 1, 1);

INSERT INTO evaluations (score, date, comment, employee_id, manager_id)
VALUES (0, '2023-01-01', 'Graaaaaaaah!', 1, 1);

INSERT INTO evaluations (score, date, comment, employee_id, manager_id)
VALUES (0, '2023-01-01', 'I have a headache!', 2, 2);

INSERT INTO evaluations (score, date, comment, employee_id, manager_id)
VALUES (90, '2023-01-01', 'Great job on the building stomping', 2, 2);

INSERT INTO evaluations (score, date, comment, employee_id, manager_id)
VALUES (100, '2023-01-01', 'Stellar scheming.', 3, 2);

INSERT INTO evaluations (score, date, comment, employee_id, manager_id) 
VALUES (80, '2022-12-01', 'Can do better at being worse', 3, 2);

INSERT INTO evaluations (score, date, comment, employee_id, manager_id) 
VALUES (99, '2022-11-01', 'It''s good to be evil', 1, 1);

