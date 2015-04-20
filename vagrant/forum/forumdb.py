#
# Database access functions for the web forum.
# 

import time
import psycopg2
## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    db = psycopg2.connect("dbname=forum")
    c = db.cursor()
    c.execute("SELECT * FROM posts ORDER BY time DESC;")
    rows = c.fetchall()
    db.close()
    posts = [{'content':str(row[0]), 'time': str(row[1])}  for row in rows]
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    db = psycopg2.connect("dbname=forum")
    c = db.cursor()
    c.execute("INSERT INTO posts(content) VALUES ( %s )" , (content,))
    db.commit()
    db.close()
    
   
