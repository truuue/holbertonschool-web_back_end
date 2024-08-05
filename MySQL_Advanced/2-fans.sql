-- Ensure the table exists and has the correct structure
CREATE TABLE IF NOT EXISTS metal_bands (
    origin VARCHAR(255),
    nb_fans INT
);

-- Query to rank country origins by the number of (non-unique) fans
-- Aggregates the number of fans by country and orders the results
SELECT
    origin,
    SUM(nb_fans) AS total_fans
FROM
    metal_bands
GROUP BY
    origin
ORDER BY
    total_fans DESC;