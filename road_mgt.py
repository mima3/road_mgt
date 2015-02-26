# -*- coding: utf-8 -*-
import urllib
import urllib2
from lxml import etree
import csv
from collections import defaultdict


def get_road_surface(offset, limit):
    """
    路面状況データ
    """
    url = ('http://roadmgt.herokuapp.com/api/v1/datapoints?data_type=road-surface&offset=%d&limit=%d' % (offset, limit))

    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    conn = opener.open(req)
    cont = conn.read()
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(cont, parser)
    namespaces = {
        'geo' : 'http://www.w3.org/2003/01/geo/wgs84_pos#',
        'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', 
        'rdfs' : 'http://www.w3.org/2000/01/rdf-schema#', 
        'rm' : 'http://roadmgt.herokuapp.com/vocab/rm#'
    }

    row = []
    datas = {}
    value_tags = root.xpath('//rdf:Description', namespaces=namespaces)
    value_tags = root.xpath('//rdf:Description', namespaces=namespaces)
    for value_tag in value_tags:
        label = value_tag.find('rdfs:label', namespaces).text
        step = value_tag.find('rm:step', namespaces).text
        alt = value_tag.find('geo:alt', namespaces).text
        analysis_timestamp = value_tag.find('rm:analysis_timestamp', namespaces).text
        rutting_amount = value_tag.find('rm:rutting_amount', namespaces).text
        municipality_id = value_tag.find('rm:municipality_id', namespaces).text
        speed_fluctuation_flag = value_tag.find('rm:speed_fluctuation_flag', namespaces).text
        section_id = value_tag.find('rm:section_id', namespaces).text
        distance = value_tag.find('rm:distance', namespaces).text
        long = value_tag.find('geo:long', namespaces).text
        iri = value_tag.find('rm:iri', namespaces).text
        cracking_rate = value_tag.find('rm:cracking_rate', namespaces).text
        pothole_num = value_tag.find('rm:pothole_num', namespaces).text
        subsidence_and_puddle = value_tag.find('rm:subsidence_and_puddle', namespaces).text
        speed = value_tag.find('rm:speed', namespaces).text
        rms = value_tag.find('rm:rms', namespaces).text
        lat = value_tag.find('geo:lat', namespaces).text
        too_slow_fast_flag = value_tag.find('rm:too_slow_fast_flag', namespaces).text
        patching_num = value_tag.find('rm:patching_num', namespaces).text

        row.append({
            'label' : label,
            'step' : step,
            'alt' : alt,
            'analysis_timestamp' : analysis_timestamp,
            'rutting_amount' : rutting_amount,
            'municipality_id' : municipality_id,
            'speed_fluctuation_flag' : speed_fluctuation_flag,
            'section_id' : section_id,
            'distance' : distance,
            'long' : long,
            'iri' : iri,
            'cracking_rate' : cracking_rate,
            'pothole_num' : pothole_num,
            'subsidence_and_puddle' : subsidence_and_puddle,
            'speed' : speed,
            'rms' : rms,
            'lat' : lat,
            'too_slow_fast_flag' : too_slow_fast_flag,
            'patching_num' :patching_num
        })
    return row

def get_meas_locale(offset, limit):
    """
    路面計測時の位置データ
    """
    url = ('http://roadmgt.herokuapp.com/api/v1/datapoints?data_type=meas-locale&offset=%d&limit=%d' % (offset, limit))

    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    conn = opener.open(req)
    cont = conn.read()
    parser = etree.XMLParser(recover=True)
    root = etree.fromstring(cont, parser)

    namespaces = {
        'geo' : 'http://www.w3.org/2003/01/geo/wgs84_pos#',
        'rdf' : 'http://www.w3.org/1999/02/22-rdf-syntax-ns#', 
        'rdfs' : 'http://www.w3.org/2000/01/rdf-schema#', 
        'rm' : 'http://roadmgt.herokuapp.com/vocab/rm#'
    }

    row = []
    datas = {}
    value_tags = root.xpath('//rdf:Description', namespaces=namespaces)
    for value_tag in value_tags:
        label = value_tag.find('rdfs:label', namespaces).text
        gpstimestamp = value_tag.find('rm:gpstimestamp', namespaces).text
        course = value_tag.find('rm:course', namespaces).text
        measurement_start_timestamp = value_tag.find('rm:measurement_start_timestamp', namespaces).text
        mounting_direction = value_tag.find('rm:mounting_direction', namespaces).text
        car_model = value_tag.find('rm:car_model', namespaces).text
        long = value_tag.find('geo:long', namespaces).text
        lat = value_tag.find('geo:lat', namespaces).text
        alt = value_tag.find('geo:alt', namespaces).text
        model_number = value_tag.find('rm:model_number', namespaces).text
        car_number = value_tag.find('rm:car_number', namespaces).text
        speed = value_tag.find('rm:speed', namespaces).text
        vertical_accuracy = value_tag.find('rm:vertical_accuracy', namespaces).text
        measurement_timestamp = value_tag.find('rm:measurement_timestamp', namespaces).text
        horizontal_accuracy = value_tag.find('rm:horizontal_accuracy', namespaces).text
        row.append({
            'label' : label,
            'gpstimestamp' : gpstimestamp,
            'course' : course,
            'measurement_start_timestamp' : measurement_start_timestamp,
            'mounting_direction' : mounting_direction,
            'car_model' : car_model,
            'long' : long,
            'lat' : lat,
            'alt' : alt,
            'model_number' : model_number,
            'car_number' : car_number,
            'speed' : speed,
            'vertical_accuracy' : vertical_accuracy,
            'measurement_timestamp' : measurement_timestamp,
            'horizontal_accuracy' : horizontal_accuracy
        })
    return row

def get_road_surface_all():
    ret = []
    limit = 300
    offset = 0
    try:
        while True:
            print ('get_road_surface_all %d' % offset)
            r = get_road_surface(offset, limit)
            ret.extend(r)
            offset += limit
    except urllib2.HTTPError, ex:
        if ex.code == 404:
            return ret
        else:
            raise
