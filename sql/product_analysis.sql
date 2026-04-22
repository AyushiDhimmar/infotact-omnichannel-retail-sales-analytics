SELECT 
    Category, SUM(Sales) AS Total_Sales
FROM
    samplesuperstore
GROUP BY Category
ORDER BY Total_Sales DESC;