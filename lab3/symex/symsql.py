## This module wraps SQLalchemy's methods to be friendly to
## symbolic / concolic execution.

import fuzzy 
import sqlalchemy.orm


oldget = sqlalchemy.orm.query.Query.get
#the original get method takes an primary key object and returns the row to that primary key


def newget(query, primary_key):

  primaryKey=query.all()[0].__table__.primary_key.columns.keys()[0]

  #query.all() execute the query spqcified and returns the result as colums as attributed result 
  for q in query.all():
    #getattr() returns the col corresponding to the primaryKey
    name=getattr(q,primaryKey)
    if(name==primary_key):
      return q

  #print query.get(fuzzy.concrete_values[primary_key])
  #raw
  ## Exercise 5: your code here.
  ##
  ## Find the object with the primary key "primary_key" in SQLalchemy
  ## query object "query", and do so in a symbolic-friendly way.
  ##
  ## Hint: given a SQLalchemy row object r, you can find the name of
  ## its primary key using r.__table__.primary_key.columns.keys()[0]
  return None


sqlalchemy.orm.query.Query.get = newget
