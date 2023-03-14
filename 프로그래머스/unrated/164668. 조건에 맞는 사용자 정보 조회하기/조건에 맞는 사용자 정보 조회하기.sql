-- 코드를 입력하세요
SELECT uu.user_id, uu.nickname, sum(ub.price) as total_sales
from used_goods_board as ub
join used_goods_user as uu
on ub.writer_id = uu.user_id
where ub.status = 'DONE'
group by uu.user_id
having total_sales >= 700000
order by total_sales
# select ub.writer_id, uu.nickname, sum(ub.price)
# from used_goods_board as ub
# join used_goods_user as uu
# on ub.writer_id = uu.user_id
# where uu.nickname = '크크큭'