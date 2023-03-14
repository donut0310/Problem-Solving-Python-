-- 코드를 입력하세요
SELECT ri.rest_id, ri.rest_name, ri.food_type, ri.favorites, ri.address, round(avg(review_score), 2) as score
from rest_info as ri
join rest_review as rr
on ri.rest_id = rr.rest_id
group by rest_id
having address like '서울%'
order by score desc, favorites desc