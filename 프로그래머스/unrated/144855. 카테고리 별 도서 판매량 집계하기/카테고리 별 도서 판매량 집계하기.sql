-- 코드를 입력하세요
SELECT b.category, sum(bs.sales) as total_sales
from book as b
join book_sales as bs
on b.book_id = bs.book_id
# where bs.sales_date >= '2022-01-01' and bs.sales_date <= '2022-01-31'
where bs.sales_date between '2022-01-01' and '2022-01-31'
group by b.category
order by b.category