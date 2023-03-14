-- 코드를 입력하세요
select flavor
from 
    (SELECT flavor, sum(total_order) as t1
    from july
    group by flavor

    union all

    select flavor, sum(total_order) as t2
    from first_half
    group by flavor
    ) as t
group by flavor
order by sum(t1) desc
limit 3


