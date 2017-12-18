# logs-analysis-project
## My view creation
```sql
create view valid_hits as select articles.title, count(*) as hits from articles, log where log.path = '/article/'||articles.slug group by articles.title order by hits desc;
```
