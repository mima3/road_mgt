#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import road_mgt_db
import sys


def main(argvs, argc):
    road_mgt_db.setup('road_mgt.sqlite')
    print road_mgt_db.get_road_surfacet_mesh()

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    sys.exit(main(argvs, argc))
