#!/usr/bin/env python
# implementation of log reporting tool

import psycopg2

def top_three_article():
    """Returns the number of players currently registered."""
    db = psycopg2.connect("dbname=tournament")
    c = db.cursor()
    c.execute("select count(*) as num from players")
    ans = c.fetchall()
    db.close()
    return ans[0][0]
