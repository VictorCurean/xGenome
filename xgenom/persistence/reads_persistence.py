"""
Python file that contains the functions for persisting NGS reads from a genome
"""
import MySQLdb._exceptions
from xgenom.persistence.db import db

def persist_read_metainf(date, species, machine):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO readsmetainfs (date, species, machine) VALUES (%s, %s, %s)"
        val = (date, species, machine)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        return True
    except MySQLdb._exceptions.Error:
        return False

def persist_reads(id, read_list):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO reads (idRead, readName, sequence, phredscore) VALUES (%s, %s, %s, %s)"
        for r in read_list:
            val = (id, r.read_id, r.sequence, r.phredscore)
            cursor.execute(sql, val)

        db.commit()
        cursor.close()
        return True
    except MySQLdb._exceptions.Error:
        return False

