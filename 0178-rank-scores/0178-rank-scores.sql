# Write your MySQL query statement below
select S1.score,count(S2.score) as 'rank' 
from Scores S1,
(SELECT DISTINCT SCORE FROM SCORES)  S2
WHERE S1.SCORE<=S2.SCORE
group by S1.id
order by S1.score Desc;