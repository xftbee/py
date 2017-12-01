#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Neo4j图形数据库示例
# 
from neo4j import GraphDatabase, INCOMING
 
# 创建或连接数据库
db = GraphDatabase('neodb')
# 在一个事务内完成写或读操作
with db.transaction:
    #创建用户组节点
    users = db.node()
    # 连接到参考节点，方便查找
    db.reference_node.USERS(users)
 
    # 为用户组建立索引，便于快速查找
    user_idx = db.node.indexes.create('users')
 
#创建用户节点
def create_user(name):
    with db.transaction:
        user = db.node(name=name)
        user.INSTANCE_OF(users)
        #  建立基于用户name的索引
        user_idx['name'][name] = user
    return user
 
 #根据用户名获得用户节点
def get_user(name):
    return user_idx['name'][name].single
 
#建立节点
for name in ['user1', 'user2','user3','user4']:
   create_user(name)
 
#为节点间添加关注关系（FOLLOWS）
with db.transaction:
    get_user('user2').FOLLOWS(get_user('user1'))
    get_user('user3').FOLLOWS(get_user('user1'))
    get_user('user4').FOLLOWS(get_user('user3'))
 
# 获得用户1的粉丝
for relationship in get_user('user1').FOLLOWS.incoming:
    u = relationship.start
    print u['name']
#输出结果：user2，user3
 
#为用户4推荐好友，即该用户关注的用户所关注的用户
nid = get_user('user4').id
#设置查询语句
query = "START n=node({id}) MATCH n-[:FOLLOWS]->m-[:FOLLOWS]->fof RETURN n,m,fof"
 
for row in db.query(query,id=nid):
    node = row['fof']
    print node['name'] 
#输出结果：user1