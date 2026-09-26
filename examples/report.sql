WITH totals AS (
    SELECT customer_id, SUM(amount) AS total_amount
    FROM orders
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.customer_name,
    CASE WHEN t.total_amount > 1000 THEN 'HIGH' ELSE 'STANDARD' END AS segment,
    ROW_NUMBER() OVER (ORDER BY t.total_amount DESC) AS rn
FROM customers c
JOIN totals t ON t.customer_id = c.customer_id
ORDER BY t.total_amount DESC;
