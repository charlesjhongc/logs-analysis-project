#!/usr/bin/env python
# implementation of log reporting tool
# create view valid_hits as select articles.title, count(*) as hits from articles, log where log.path = '/article/'||articles.slug group by articles.title order by hits desc;
import psycopg2

def top_three_article():
    #TODO DESC
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    #TODO why do I have to include title in aggregate so I can select it?
    c.execute("select title, hits from valid_hits limit 3")
    ans = c.fetchall()
    db.close()
    #TODO use for loop?
    print ("\"{}\" — {} views".format(ans[0][0],ans[0][1]))
    print ("\"{}\" — {} views".format(ans[1][0],ans[1][1]))
    print ("\"{}\" — {} views".format(ans[2][0],ans[2][1]))
    return

def most_pop_author():
    #TODO DESC
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select authors.name, sum(valid_hits.hits) as popularity from authors, articles, valid_hits where authors.id = articles.author and articles.title = valid_hits.title group by authors.name order by popularity desc")
    ans = c.fetchall()
    db.close()
    #TODO use for loop?
    print ("{} — {} views".format(ans[0][0],ans[0][1]))
    print ("{} — {} views".format(ans[1][0],ans[1][1]))
    print ("{} — {} views".format(ans[2][0],ans[2][1]))
    print ("{} — {} views".format(ans[3][0],ans[3][1]))
    return

top_three_article()
most_pop_author()
