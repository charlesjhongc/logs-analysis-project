#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Implementation of a log analysis tool

import psycopg2
import datetime


def top_three_article():
    # TODO DESC
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    # TODO why do I have to include title in aggregate so I can select it?
    c.execute("select title, hits from valid_hits limit 3")
    ans = c.fetchall()
    db.close()
    for i in range(3):
        print("\"{}\" — {} views".format(ans[i][0], ans[i][1]))
    return


def most_pop_author():
    # TODO DESC
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select authors.name, sum(valid_hits.hits) as popularity\
    from authors, articles, valid_hits\
    where authors.id = articles.author and articles.title = valid_hits.title\
    group by authors.name order by popularity desc")
    ans = c.fetchall()
    db.close()
    for author in ans:
        print("{} — {} views".format(author[0], author[1]))
    return


def err_request_day():
    # TODO DESC
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("select day, err_ratio from date_overview\
    where err_ratio > 0.01")
    ans = c.fetchall()
    db.close()
    for record in ans:
        print("{} — {:.1%} errors".format(
                record[0].strftime("%B %d, %Y"), record[1]))
    return

if __name__ == '__main__':
    top_three_article()
    most_pop_author()
    err_request_day()
