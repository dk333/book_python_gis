#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
import mapnik
mapfile = '/gdata/world_population.xml'
m = mapnik.Map(1000, 500, '+proj=latlong +datum=WGS84')
mapnik.load_map(m, mapfile)
###############################################################################
m.zoom_all()
mapnik.render_to_file(m, 'map.png')
###############################################################################
mapnik.render_to_file(map, 'map.png', 'png256')
###############################################################################
###############################################################################
