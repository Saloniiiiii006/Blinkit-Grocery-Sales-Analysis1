-- ==========================================
-- BLINKIT DATA ANALYSIS
-- ==========================================
USE blinkit_analysis;

-- 1. Total Revenue
SELECT
ROUND(SUM(o.Qty * p.Price),2) AS Total_Revenue
FROM orders o
JOIN products p
ON o.P_ID = p.P_ID;

-- 2. Total Orders
SELECT COUNT(*) AS Total_Orders
FROM orders;

-- 3. Total Customers
SELECT COUNT(*) AS Total_Customers
FROM customers;

-- 4. Average Order Value
SELECT
ROUND(SUM(o.Qty * p.Price)/COUNT(DISTINCT o.Or_ID),2) AS Average_Order_Value
FROM orders o
JOIN products p
ON o.P_ID = p.P_ID;

-- 5. Top 10 Best Selling Products
SELECT
p.PName,
SUM(o.Qty) AS Total_Quantity
FROM orders o
JOIN products p
ON o.P_ID = p.P_ID
GROUP BY p.PName
ORDER BY Total_Quantity DESC
LIMIT 10;

-- 6. Revenue by Category

SELECT
p.Category,
ROUND(SUM(o.Qty * p.Price),2) AS Revenue
FROM orders o
JOIN products p
ON o.P_ID = p.P_ID
GROUP BY p.Category
ORDER BY Revenue DESC;

-- 8. Revenue by Brand
SELECT
p.Brand,
ROUND(SUM(o.Qty * p.Price),2) AS Revenue
FROM orders o
JOIN products p
ON o.P_ID = p.P_ID
GROUP BY p.Brand
ORDER BY Revenue DESC;

-- 9.Most Ordered Categories
SELECT
p.Category,
SUM(o.Qty) AS Total_Items_Sold
FROM orders o
JOIN products p
ON o.P_ID = p.P_ID
GROUP BY p.Category
ORDER BY Total_Items_Sold DESC;

-- 10. Most Ordered Brands
SELECT
p.Brand,
SUM(o.Qty) AS Total_Items_Sold
FROM orders o
JOIN products p
ON o.P_ID = p.P_ID
GROUP BY p.Brand
ORDER BY Total_Items_Sold DESC;

-- 11. Most Expensive Products
SELECT
PName,
Brand,
Category,
Price
FROM products
ORDER BY Price DESC
LIMIT 10;

SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM delivery;
