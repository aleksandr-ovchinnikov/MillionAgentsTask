SELECT user_id from reports WHERE created_at > '2021-01-01'
UNION ALL
SELECT sum(reward) from reports where created_at >= '2022-01-01';


