from ora_sql_complexity import measure

def test_metrics():
    sql="""WITH x AS (SELECT customer_id, SUM(amount) s FROM orders GROUP BY customer_id)
    SELECT c.customer_id, CASE WHEN x.s>100 THEN 1 ELSE 0 END flag,
           ROW_NUMBER() OVER (ORDER BY x.s DESC) rn
    FROM customers c JOIN x ON x.customer_id=c.customer_id"""
    m=measure(sql)
    assert m.joins==1
    assert m.cases==1
    assert m.windows==1
    assert m.score>0
