SELECT 
    City, SUM(Sales) AS City_Sales
FROM
    samplesuperstore
GROUP BY City
ORDER BY City_Sales DESC;