-- 코드를 입력하세요
SELECT outs.animal_id, outs.name
from animal_outs outs
left outer join animal_ins ins
on outs.animal_id = ins.animal_id
where ins.animal_id is NULL
order by outs.animal_id