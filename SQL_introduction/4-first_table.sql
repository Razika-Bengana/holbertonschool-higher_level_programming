-- script that creates a table called first_table in the current database in your MySQL server
-- the database name will be passed as argument of mysql command
-- if the database already exists, the script should not fail
CREATE TABLE IF NOT EXISTS first_table (id INT,
name VARCHAR(256));
