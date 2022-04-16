select b.order_id, a.review_score, d.product_category_name 
from tb_order_reviews as a
join tb_order_payments as b
on a.order_id = b.order_id 
join tb_order_items as c
on b.order_id = c.order_id
join tb_products as d
on c.product_id = d.product_id 