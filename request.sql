select c.name , w.temperature_max from city c join weather w on w.city_id= c.id where temperature_max > 30;

SELECT c.name, MAX(w.precipitation)  FROM city c JOIN weather w ON w.city_id = c.id GROUP BY c.name ORDER BY MAX(w.precipitation)  DESC LIMIT 5;

