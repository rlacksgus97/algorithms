-- 코드를 입력하세요
SELECT hour(datetime) HOUR, count(datetime) COUNT
from animal_outs
group by hour(datetime)
having HOUR >= 9 and HOUR < 20
order by HOUR
