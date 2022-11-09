-- script that lists all cities contained in the database hbtn_0d_usa
-- each record should display: cities.id - cities.name - states.name
-- results must be sorted in ascending order by cities.id
-- the database name will be passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name FROM states
JOIN cities ON states.id = cities.state_id
ORDER BY cities.id;
