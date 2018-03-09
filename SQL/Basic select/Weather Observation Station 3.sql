/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/


//select query to eliminate duplicate

select DISTINCT CITY from STATION where MOD(ID,2) = 0;