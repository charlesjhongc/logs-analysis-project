# Logs Analysis Project
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
### Print directly
```sh
$ python log_analysis.py
```
### Import as a module
```python
>>> import log_analysis
>>> log_analysis.top_three_article()
"Candidate is jerk, alleges rival" — 338647 views
"Bears love berries, alleges bear" — 253801 views
"Bad things gone, say good people" — 170098 views
>>> log_analysis.most_pop_author()
Ursula La Multa — 507594 views
Rudolf von Treppenwitz — 423457 views
Anonymous Contributor — 170098 views
Markoff Chaney — 84557 views
>>> log_analysis.err_request_day()
July 17, 2016 — 2.3% errors
```
## Architecture
- top_three_article()  //List the most popular three articles of all time.
- most_pop_author()    //List the most popular article authors of all time.
- err_request_day()    //List date with more than 1% of requests lead to errors.
