-- script that updates the score of Bob to 10 in the table second_table
-- not allowed to use Bob’s id value, only the name field
-- the database name will be passed as argument of mysql command
UPDATE second_table SET score = 10 WHERE name = 'Bob';
