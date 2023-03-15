with users as (
    select user_id
    from user_info
    where year(joined) = '2021'
    )

select year(os.sales_date) year, month(os.sales_date) month, 
    count(distinct os.user_id) puchased_users, 
    round(count(distinct os.user_id) / (select count(user_id) from users), 1) puchased_ratio
from users u
join online_sale os
on u.user_id = os.user_id
group by year(os.sales_date), month(os.sales_date)
order by year, month

