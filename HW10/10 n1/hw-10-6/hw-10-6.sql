SELECT couch_name,MAX(cont_price) FROM
(SELECT couch.couch_id, couch.couch_name, contract.cont_price
FROM couch
RIGHT JOIN contract
ON couch.couch_id = contract.person_id)
GROUP BY couch_name;


SELECT DISTINCT seas_id , MAX(cont_price) FROM
(SELECT player.player_id, player.player_name, contract.cont_price, contract.seas_id
FROM player
RIGHT JOIN contract
ON player.player_id = contract.person_id)
GROUP BY player_name;


SELECT city_name, COUNT(*) AS numberOfTeams
FROM
(SELECT city.city_id, city.city_name, team.team_name
FROM city
FULL OUTER JOIN team
ON city.city_id = team.city_id)
GROUP BY city_name;


