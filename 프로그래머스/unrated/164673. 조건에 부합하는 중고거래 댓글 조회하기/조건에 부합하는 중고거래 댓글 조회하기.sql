-- 코드를 입력하세요
SELECT ub.title, ub.board_id, ur.reply_id, ur.writer_id, ur.contents, date_format(ur.created_date, '%Y-%m-%d') as created_date
from used_goods_board as ub
join used_goods_reply as ur
on ub.board_id = ur.board_id
where ub.created_date >= '2022-10-01' and ub.created_date <= '2022-10-31'
order by ur.created_date, ub.title