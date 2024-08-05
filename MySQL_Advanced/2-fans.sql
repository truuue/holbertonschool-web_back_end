-- Ensure the table exists and has the correct structure
SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
