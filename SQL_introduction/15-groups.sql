-- script that lists the number of records with the same score in the table second_table of the database hbtn_0c_0 in your MySQL server
-- the result should display the score, and the number of records for this score with the label number
-- the list should be sorted by the number of records (descending)
-- the database name will be passed as an argument to mysql command
SELECT score, COUNT('score') as number FROM second_table
GROUP BY score, ORDER BY score DESC;
