-- 코드를 입력하세요
# 중성화 X -> Intact
# 중성화 O -> Spayed or Neutered
SELECT ai.animal_id, ai.animal_type, ai.name
from animal_ins ai
join animal_outs ao
on ai.animal_id = ao.animal_id
where ai.sex_upon_intake like 'Intact%' 
 and (ao.sex_upon_outcome like 'Spayed%' or ao.sex_upon_outcome like 'Neutered%')
order by ai.animal_id