import sys

from qgis.core import (QgsApplication,
                       QgsVectorLayer)

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix 
QgsApplication.setPrefixPath('C:\OSGeo4W\apps\qgis-ltr', True)
qgs = QgsApplication([], False) # No GUI
qgs.initQgis()

# Append the path where processing plugin can be found
sys.path.append('C:\\OSGeo4W\\apps\\qgis-ltr\\python\\plugins')
# print(sys.path)

import processing
from processing.core.Processing import Processing
Processing.initialize()

airport_layer = QgsVectorLayer("C:\pyqgis\geodata\sample_data.gpkg|layername=Airports", "airport", "ogr")

res = processing.run("gdal:buffervectors", {
    'INPUT':airport_layer,
    'GEOMETRY':'geom',
    'DISTANCE':1000,
    'FIELD':None,
    'DISSOLVE':False,
    'EXPLODE_COLLECTIONS':False,
    'OPTIONS':'',
    'OUTPUT':'C:/borrar/tmp/OUTPUT.shp'})

buffers = QgsVectorLayer(res['OUTPUT'], "buffer", "ogr")

print(buffers.isValid())
print(buffers.featureCount())
for f in buffers.getFeatures():
    print(f['name'], f.geometry().area())

qgs.exitQgis()
