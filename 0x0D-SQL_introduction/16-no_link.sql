--  lists all records of the table second_table of the database hbtn_0c_0
-- rows without a name value are not shown
-- Results  displays the score and the name in descending order of score
SELECT score, name
FROM second_table
WHERE
name IS NOT NULL
AND
score IS NOT NULL
ORDER BY score DESC;
