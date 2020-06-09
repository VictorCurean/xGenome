from xgenom.persistence.db import db
import pickle


curr = db.cursor()
curr.execute("SELECT * FROM suffixarrays WHERE idRef = 4")
myres = curr.fetchall()[0][1]


data = pickle.loads(myres)


curr.close()