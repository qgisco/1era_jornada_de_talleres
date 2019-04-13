import sys

from qgis.core import (QgsApplication, 
                       QgsVectorLayer)

from qgis.analysis import QgsNativeAlgorithms

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix 
QgsApplication.setPrefixPath('C:\OSGeo4W\apps\qgis-ltr', True)
qgs = QgsApplication([], False) # No GUI
qgs.initQgis()

# Append the path where processing plugin can be found
sys.path.append('C:\\OSGeo4W\\apps\\qgis-ltr\\python\\plugins')
#print(sys.path)

import processing
from processing.core.Processing import Processing
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

airport_layer = QgsVectorLayer("C:\pyqgis\geodata\sample_data.gpkg|layername=Airports", "airport", "ogr")

# You can get a complete list of Processing algs in:
# https://gis.stackexchange.com/a/276979
res = processing.run("native:buffer", {
    'INPUT':airport_layer,
    'DISTANCE':1000,
    'SEGMENTS':20,
    'END_CAP_STYLE':0,
    'JOIN_STYLE':0,
    'MITER_LIMIT':2,
    'DISSOLVE':False,'OUTPUT':'memory:'})

buffers = res['OUTPUT']

print(buffers.isValid())
print(buffers.featureCount())
for f in buffers.getFeatures():
    print(f['name'], f.geometry().area())

qgs.exitQgis()
