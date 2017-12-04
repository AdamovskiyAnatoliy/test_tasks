SELECT email, name, subscription_date 
FROM general 
WHERE EXTRACT(MONTH FROM subscription_date) = EXTRACT(MONTH FROM now()) AND
EXTRACT(YEAR FROM subscription_date) = EXTRACT(YEAR FROM now());
