# -*- coding: utf-8 -*-
import os
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import road_mgt
import jpgrid


database_proxy = Proxy()  # Create a proxy for our db.


class RoadSurface(Model):
    """
    路面状況データモデル
    """
    label = TextField(primary_key=True)
    mesh_code = TextField(index=True)
    step = FloatField()
    alt = FloatField()
    analysis_timestamp = TextField()
    rutting_amount = FloatField()
    municipality_id = IntegerField()
    speed_fluctuation_flag = IntegerField()
    section_id = IntegerField()
    distance = FloatField()
    long = FloatField()
    iri = FloatField()
    cracking_rate = FloatField()
    pothole_num = IntegerField()
    subsidence_and_puddle = FloatField()
    speed = FloatField()
    rms = FloatField()
    lat = FloatField()
    too_slow_fast_flag = IntegerField()
    patching_num =  IntegerField()

    class Meta:
        database = database_proxy

def connect(path):
    """
    データベースへの接続
    @param path sqliteのパス
    """
    db = SqliteExtDatabase(path)
    database_proxy.initialize(db)


def setup(path):
    """
    データベースの作成
    @param path sqliteのパス
    """
    connect(path)

    database_proxy.create_tables([RoadSurface], True)


def import_road_surfacet():
    """
    路面状況のインポート
    """
    with database_proxy.transaction():
        RoadSurface.delete().execute()
        ret = road_mgt.get_road_surface_all()
        for item in ret:
            try:
                RoadSurface.get(RoadSurface.label == item['label'])
            except RoadSurface.DoesNotExist:
                RoadSurface.create(
                    label = item['label'],
                    mesh_code = jpgrid.encodeEighth(float(item['lat']) , float(item['long'])),
                    step = item['step'],
                    alt =item['alt'],
                    analysis_timestamp = item['analysis_timestamp'],
                    rutting_amount = item['rutting_amount'],
                    municipality_id = item['municipality_id'],
                    speed_fluctuation_flag = item['speed_fluctuation_flag'],
                    section_id = item['section_id'],
                    distance = item['distance'],
                    long = item['long'],
                    iri = item['iri'],
                    cracking_rate = item['cracking_rate'],
                    pothole_num = item['pothole_num'],
                    subsidence_and_puddle = item['subsidence_and_puddle'],
                    speed = item['speed'],
                    rms = item['rms'],
                    lat = item['lat'],
                    too_slow_fast_flag = item['too_slow_fast_flag'],
                    patching_num = item['patching_num']
                )
        database_proxy.commit()


def get_road_surface_mesh():
    query = RoadSurface.select(
        RoadSurface.mesh_code,
        fn.avg(RoadSurface.iri).alias('iri_avg'),
        fn.avg(RoadSurface.step).alias('step_avg'),
        fn.avg(RoadSurface.rutting_amount).alias('rutting_amount_avg'),
        fn.avg(RoadSurface.cracking_rate).alias('cracking_rate_avg'),
        fn.avg(RoadSurface.pothole_num).alias('pothole_num_avg'),
        fn.avg(RoadSurface.subsidence_and_puddle).alias('subsidence_and_puddle_avg'),
        fn.avg(RoadSurface.speed).alias('speed_avg'),
        fn.sum(RoadSurface.pothole_num).alias('pothole_num_sum'),
        fn.sum(RoadSurface.patching_num).alias('patching_num_sum')
    ).group_by(RoadSurface.mesh_code)
    ret = []
    for row in query:
        meshbox = jpgrid.bbox(row.mesh_code)
        ret.append({
            'mesh_code' : row.mesh_code,
            's' : meshbox['s'],
            'w' : meshbox['w'],
            'n' : meshbox['n'],
            'e' : meshbox['e'],
            'iri_avg' : row.iri_avg,
            'step_avg' : row.step_avg,
            'rutting_amount_avg' : row.rutting_amount_avg,
            'cracking_rate_avg' : row.cracking_rate_avg,
            'pothole_num_avg' : row.pothole_num_avg,
            'subsidence_and_puddle_avg' : row.subsidence_and_puddle_avg,
            'pothole_num_sum' : row.pothole_num_sum,
            'patching_num_sum' : row.patching_num_sum,
        })
    return ret


def get_road_surface():
    query = RoadSurface.select(
        RoadSurface.label,
        RoadSurface.step,
        RoadSurface.alt,
        RoadSurface.analysis_timestamp,
        RoadSurface.rutting_amount,
        RoadSurface.long,
        RoadSurface.iri,
        RoadSurface.cracking_rate,
        RoadSurface.pothole_num,
        RoadSurface.subsidence_and_puddle,
        RoadSurface.lat,
        RoadSurface.patching_num
    )
    ret = []
    for row in query:
        ret.append({
            'label' : row.label,
            'step' : row.step,
            'alt' : row.alt,
            'analysis_timestamp' : row.analysis_timestamp,
            'rutting_amount' : row.rutting_amount,
            'long' : row.long,
            'iri' : row.iri,
            'cracking_rate' : row.cracking_rate,
            'pothole_num' : row.pothole_num,
            'subsidence_and_puddle' : row.subsidence_and_puddle,
            'lat' : row.lat,
            'patching_num' : row.patching_num
        })
    return ret


def get_road_surface_range():
    query = RoadSurface.select(
        fn.max(RoadSurface.lat).alias('lat_max'),
        fn.min(RoadSurface.lat).alias('lat_min'),
        fn.max(RoadSurface.long).alias('long_max'),
        fn.min(RoadSurface.long).alias('long_min')
    )
    for row in query:
        return {
          'lat_max' : row.lat_max,
          'lat_min' : row.lat_min,
          'long_max' : row.long_max,
          'long_min' : row.long_min,
        }
    return null;
