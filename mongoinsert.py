import time
from pymongo import Connection
db = Connection().foo
collection = db.bar

start = time.time()
for i in range(1000000):
	collection.insert({"foo": "bar", "baz": i ,"z": 10 - i})

total=time.time()-start
print "%d second" % total

