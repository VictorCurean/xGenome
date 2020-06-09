"""
Python file that contains the functions for persisting a genome reference and the additional data structures
such as the BWT of the reference, the Suffix Array and the First Function, in order to have the FM Index
"""
import MySQLdb._exceptions
from xgenom.persistence.db import db
import pickle

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
    try:
        cursor = db.cursor()
        sql = "INSERT INTO refmetainfs (name, date, specimen) VALUES (%s, %s, %s)"
        val = (name, date, specimen)
        cursor.execute(sql, val)
        db.commit()
        rowid = cursor.lastrowid
        cursor.close()
        return rowid
    except MySQLdb._exceptions.Error:
        return False

def persist_reference(id, reference):
    try:
        pdata = pickle.dumps(reference, pickle.HIGHEST_PROTOCOL)

        cursor = db.cursor()
        sql = "INSERT INTO refs (idRef, refcontent) VALUES (%s, %s)"
        val = (id, pdata)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        return True
    except MySQLdb._exceptions.Error:
        return False

def persist_bwt(id, bwt):
    try:
        pdata = pickle.dumps(bwt, pickle.HIGHEST_PROTOCOL)
        cursor = db.cursor()
        sql = "INSERT INTO bwts (idRef, bwtcontent) VALUES (%s, %s)"
        val = (id, pdata)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        return True
    except MySQLdb._exceptions.Error:
        return False

def persist_sa(id, sa):
    try:
        pdata = pickle.dumps(sa, pickle.HIGHEST_PROTOCOL)
        cursor = db.cursor()
        sql = "INSERT INTO suffixarrays (idRef, suffixarraycontent) VALUES (%s, %s)"
        val = (id, pdata)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        return True
    except MySQLdb._exceptions.Error:
        return False




