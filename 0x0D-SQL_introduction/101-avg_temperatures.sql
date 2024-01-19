-- This script displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT `city`, AVG(`value`) AS average_temperatrue
FROM `temperatures`
GROUP BY `city`
ORDER BY `average_temperatrue` DESC;
