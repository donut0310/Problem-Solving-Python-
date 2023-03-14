-- 코드를 입력하세요
SELECT distinct(hf.flavor)
from first_half as hf
inner join icecream_info as ii on hf.flavor = ii.flavor
where hf.total_order > 3000 and ii.ingredient_type = 'fruit_based'
order by total_order desc