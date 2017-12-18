#!/usr/bin/env python
# implementation of log reporting tool

import psycopg2

def top_three_article():
    """Returns the number of players currently registered."""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    #TODO why do I have to include title in aggregate so I can select it?
    c.execute("select articles.title, count(*) as number from log_slug, articles where log_slug.ltrim = articles.slug group by articles.slug, articles.title order by number desc limit 3")
    ans = c.fetchall()
    db.close()
    return

top_three_article()
