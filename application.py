# coding=utf-8
from bottle import get, post, template, request, Bottle, response, redirect, abort
from json import dumps
import os
import json
from collections import defaultdict
import time
import cgi
import urllib
import road_mgt_db
import peewee


app = Bottle()


def setup(conf):
    global app
    road_mgt_db.connect(conf.get('database', 'path'))


@app.get('/')
def Home():
    #return 'road_mgt_db page...'
    redirect("/road_mgt/road_mgt.html")


@app.get('/json/get_road_surface_mesh')
def get_road_surface_mesh():
    ret = road_mgt_db.get_road_surface_mesh()
    response.content_type = 'application/json;charset=utf-8'
    return json.dumps(ret)


@app.get('/json/get_road_surface')
def get_road_surface():
    ret = road_mgt_db.get_road_surface()
    response.content_type = 'application/json;charset=utf-8'
    return json.dumps(ret)

@app.get('/json/get_road_surface_range')
def get_road_surface():
    ret = road_mgt_db.get_road_surface_range()
    response.content_type = 'application/json;charset=utf-8'
    return json.dumps(ret)


