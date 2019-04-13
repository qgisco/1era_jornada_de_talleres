from qgis.core import (QgsApplication, 
                       QgsVectorLayer)

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix 
QgsApplication.setPrefixPath('C:\OSGeo4W\apps\qgis-ltr', True)
qgs = QgsApplication([], False) # No GUI
qgs.initQgis()

airport_layer = QgsVectorLayer("C:\pyqgis\geodata\sample_data.gpkg|layername=Airports", "airport", "ogr")

print(airport_layer.isValid())
print(airport_layer.featureCount())
for f in airport_layer.getFeatures():
    print(f['name'], f.geometry().asWkt())

qgs.exitQgis()
