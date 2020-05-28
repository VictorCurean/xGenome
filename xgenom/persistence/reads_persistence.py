"""
Python file that contains the functions for persisting NGS reads from a genome
"""

from xgenom.persistence.db import db, cursor

def persist_read_metainf(date, species, machine):
    sql = "INSERT INTO readsmetainfs (date, species, machine) VALUES (%s, %s, %s)"
    val = (date, species, machine)
    cursor.execute(sql, val)
    db.commit()
    return cursor.lastrowid

def persist_reads(id, read_list):
    sql = "INSERT INTO reads (idRead, readName, sequence, phredscore) VALUES (%s, %s, %s, %s)"
    for r in read_list:
        val = (id, r.read_id, r.sequence, r.phredscore)
        cursor.execute(sql, val)

    db.commit()
    return cursor.rowcount

