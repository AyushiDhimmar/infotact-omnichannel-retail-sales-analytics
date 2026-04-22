SELECT 
    City, ROUND(SUM(Sales), 2) AS City_Sales
FROM
    samplesuperstore
GROUP BY City
ORDER BY City_Sales DESC;