__author__ = 'xuft'

#coding=utf-8
import  os
'''
os.getcwd()
os.name
os.remove('filename')
os.removedirs('path')
os.system('shellcmd')
os.mkdir('newpath')
os.chdir('filepath')
os.listdir('filepath')
os.sep
os.linesep
os.path.split('path\\file')
os.path.isfile('path\\file.txt')
os.path.isdir('path\\item')
os.path.exists('path\\item')
os.path.abspath('filename')
os.path.normpath(path)
os.apth.getsize('path\\file.txt')
os.apth.splitext('path\\file.txt')
os.path.join(path,filename)
os.path.basename('path\\file.txt')
os.path.dirname(path)
'''
cwd=os.getcwd()
print cwd  ,'###os.getcwd()'
name = os.name
if name == 'posix':
    print ("this is Linux or Unix") ,'##os.name'
elif name == 'nt':
    print ("this is windows") ,'##os.name'
else:
    print ("this is other system"),'##os.name'


def seek_file(f):
    print f+' thanks'


def read_file(f):
    c=open(f)
    print c.read()


print "this is the function result:",seek_file('good')
c = 'ip.txt'

read_file(c)
