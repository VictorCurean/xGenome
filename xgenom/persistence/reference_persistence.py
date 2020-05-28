"""
Python file that contains the functions for persisting a genome reference and the additional data structures
such as the BWT of the reference, the Suffix Array and the First Function, in order to have the FM Index
"""

from xgenom.persistence.db import db, cursor

def persist_reference_meta(name, date, specimen):
    """
    Function for persisting a reference meta infos record in the refmetainfs table.
    This table is used to centralize information about the content of a reference, as well as its afferent data structures
    that are used for building the FM-Index
    The refmatainfs table has autoincrement mode on, so that the id has not to be specifically given.
    In order however to mantain the reference to this table for further operations on the other tables that contain a
    foreign key to this table, the function returns the id of the inserted record.
    :param name: the name of the reference - optional in the database
    :param date: the date of the reference - optional in the database
    :param specimen: the specimen of the reference - optional in the database
    :return: the id of the inserted record
    """
    sql = "INSERT INTO refmetainfs (name, date, specimen) VALUES (%s, %s, %s)"
    val = (name, date, specimen)
    cursor.execute(sql, val)
    db.commit()
    return cursor.lastrowid

def persist_reference(id, reference):
    sql = "INSERT INTO refs (idRef, refcontent) VALUES (%s, %s)"
    val = (id, reference)
    cursor.execute(sql, val)
    db.commit()

def persist_bwt(id, bwt):
    sql = "INSERT INTO bwts (idRef, bwtcontent) VALUES (%s, %s)"
    val = (id, bwt)
    cursor.execute(sql, val)
    db.commit()

def persist_sa(id, sa):
    sql = "INSERT INTO suffixarrays (idRef, suffixarraycontent) VALUES (%s, %s)"
    val = (id, sa)
    cursor.execute(sql, val)
    db.commit()




