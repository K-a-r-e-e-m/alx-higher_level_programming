-- This script displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
SELECT `city`, AVG(`value`)
FROM `temperatures`
ORDER BY `value` DESC;
