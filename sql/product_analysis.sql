SELECT 
    Category, ROUND(SUM(Sales), 2) AS Total_Sales
FROM
    samplesuperstore
GROUP BY Category
ORDER BY Total_Sales DESC;