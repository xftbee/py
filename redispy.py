__author__ = 'xuft'

import redis
import time

def insredis():
    """


    """
    r = redis.Redis(host='192.168.100.189',port=9221,db=0)
    for i in range(200000):
        r.set('drdwwwtsdffw33'+str(i),'ssdfvsr3dfsdsfsdfsdfbsgsdgdshhresaddshijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'+str(i))
        #print i

if __name__ == "__main__":
    start = time.time()
    insredis()
    total=time.time()-start
    print "%d second" % total