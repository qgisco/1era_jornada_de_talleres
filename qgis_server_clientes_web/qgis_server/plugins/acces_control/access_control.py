from qgis.server import QgsAccessControlFilter

class RestrictedAccessControl(QgsAccessControlFilter):
    def __init__(self, server_iface):
        super(QgsAccessControlFilter, self).__init__(server_iface)

    def layerFilterExpression(self, layer):
        """ Return an additional expression filter """
        #return "intersects_bbox( $geometry, geom_from_wkt('LINESTRING(-8245386.2 525874.5, -8245321.2 525920.4)' ) )"
        return super(RestrictedAccessControl, self).layerFilterExpression(layer)

    def layerFilterSubsetString(self, layer):
        """ Return an additional subset string (typically SQL) filter """
        #return """ "fid" = '473' """
        return super(RestrictedAccessControl, self).layerFilterSubsetString(layer)

    def layerPermissions(self, layer):
        """ Return the layer rights """
        #if layer.name() == 'construccion':
        #    rights = QgsAccessControlFilter.LayerPermissions()
        #    rights.canRead = rights.canInsert = rights.canUpdate = rights.canDelete = False
        #    return rights

        return super(RestrictedAccessControl, self).layerPermissions(layer)

    def authorizedLayerAttributes(self, layer, attributes):
        """ Return the authorised layer attributes """
        #return ["area_terreno", "avaluo_terreno"] 
        return super(RestrictedAccessControl, self).authorizedLayerAttributes(layer, attributes)

    def allowToEdit(self, layer, feature):
        """ Are we authorise to modify the following geometry """
        #if layer.name() == 'construccion':
        #    return feature['fid'] >= 67 and feature['fid'] <= 80
            
        return super(RestrictedAccessControl, self).allowToEdit(layer, feature)

    def cacheKey(self):
        return super(RestrictedAccessControl, self).cacheKey()


class AccessControl:
    def __init__(self, serverIface):
        # Save reference to the QGIS server interface
        serverIface.registerAccessControl( RestrictedAccessControl(serverIface), 100 )

