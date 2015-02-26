#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import road_mgt_db
import sys


def main(argvs, argc):
    if argc != 2:
        print ("Usage #python %s sqlite_path" % argvs[0])
        return 1
    db_path = argvs[1]
    road_mgt_db.setup(db_path)
    road_mgt_db.import_road_surfacet()

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    sys.exit(main(argvs, argc))
