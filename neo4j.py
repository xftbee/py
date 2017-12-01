#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'xuft'

from neo4j import GraphDatabase , INCOMING

db = GraphDatabase('neodb')

with db.transaction:
    users = db.node()
    db.reference_node.USERS(users)
    user_idx = db.node.indexes.create('users')


def create_user(name):
    with db.transaction:
        user = db.node(name=name)
        user.INSTANCE_OF(users)
        user_idx['name'][name] = user
    return user



def get_user(name):
    return user_idx['name'][name].single


for name in ['user1','user2','user3','user4']:
    create_user(name)

for relationship in get_user('user1').FOLLOWS.incoming:
    u = relationship.start
    print u['name']

nid = get_user('user4').id

query = "START n=node({id}) MATCH n-[:FOLLOWS]->m-[:FOLLOWS]->fof RETURN n,m,fof"

for row in db.query(query,id=nid):
    node = row['fof']
    print node['name']
