USE world;

SELECT cn.name AS Country, ln.language AS "Language", ln.percentage AS Percentage 
FROM  world.countries AS cn INNER JOIN world.languages AS ln ON cn.id = ln.country_id 
WHERE ln.language LIKE UPPER('slovene')
ORDER BY ln.percentage DESC;

SELECT cn.name AS Country, COUNT(ci.id) AS "Total Number of Cities"
FROM  countries AS cn INNER JOIN cities AS ci ON cn.id = ci.country_id
GROUP BY cn.name
ORDER BY COUNT(ci.id) DESC;

SELECT ci.name AS City, ci.population AS Population
FROM world.countries AS cn INNER JOIN world.cities AS ci ON cn.id = ci.country_id
WHERE cn.name = 'Mexico' AND ci.population > 500000
ORDER BY ci.population DESC;

SELECT cn.name AS Country, ln.language AS "Language", ln.percentage AS Percentage
FROM world.countries AS cn INNER JOIN world.languages AS ln ON cn.id = ln.country_id
WHERE ln.percentage > 89
ORDER BY ln.percentage DESC;

SELECT cn.name AS Country, cn.surface_area AS "Surface Area", cn.population AS Population
FROM world.countries AS cn
WHERE cn.surface_area < 501 AND cn.population > 100000
ORDER BY cn.surface_area DESC;

SELECT cn.name AS Country, cn.government_form AS "Government Form", cn.capital AS Capital, cn.life_expectancy AS "Life Expectancy"
FROM world.countries AS cn
WHERE cn.government_form = 'Constitutional Monarchy';

SELECT cn.name AS Country, ci.name AS City, ci.district AS "State/Province", ci.population AS Population
FROM world.countries AS cn INNER JOIN world.cities AS ci ON cn.id = ci.country_id
WHERE ci.district = 'Buenos Aires' AND ci.population > 500000;

SELECT cn.region AS Region, COUNT(cn.id) AS "Number of Countries"
FROM world.countries AS cn
GROUP BY cn.region
ORDER BY COUNT(cn.id) DESC;



