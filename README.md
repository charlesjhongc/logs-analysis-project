# logs-analysis-project
## My view creation
```sql
create view valid_hits as select articles.title, count(*) as hits from articles, log where log.path = '/article/'||articles.slug group by articles.title order by hits desc;
```
```sql
create view date_overview as select date_trunc('day', time) as day, cast(sum(case when status!='200 OK' then 1 else 0 end) as real) / cast(sum(case when status!='' then 1 else 0 end) as real) as err_ratio from log group by day order by day;
```
