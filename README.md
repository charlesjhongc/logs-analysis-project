# logs-analysis-project
## Create 2 SQL views first
```sql
create view valid_hits as
  select articles.title, count(*) as hits
  from articles, log
  where log.path = '/article/'||articles.slug
  group by articles.title
  order by hits desc;
```
```sql
create view date_overview as
  select date_trunc('day', time) as day,
  cast(sum(case when status!='200 OK' then 1 else 0 end) as real) / cast(sum(case when status!='' then 1 else 0 end) as real) as err_ratio
  from log
  group by day
  order by day;
```
## Usage
```python
>>> import log_analysis
>>> log_analysis.top_three_article()
>>> log_analysis.most_pop_author()
>>> log_analysis.err_request_day()
```
## Architecture of log_analysis
- top_three_article()
  List the most popular three articles of all time.
- most_pop_author()
  List the most popular article authors of all time.
- err_request_day()
  List date with more than 1% of requests lead to errors.
