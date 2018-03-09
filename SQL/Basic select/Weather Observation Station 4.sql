/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

/*
COUNT = return number of rows match condition
*/

select count(CITY) - count(DISTINCT CITY) from STATION;
