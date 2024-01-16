-- Script that displays the top 3 of cities temperature during July and August
-- Ordered by temperature (descending)
SELECT city, AVG(value) AS temp_avg
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY temp_avg DESC
LIMIT 3;
