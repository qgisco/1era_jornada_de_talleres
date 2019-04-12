import os
import base64

from qgis.core import QgsMessageLog
from qgis.server import QgsAccessControlFilter, QgsServerFilter

from .config import *

class RestrictedAccessControlWithUsers(QgsAccessControlFilter):
    def __init__(self, server_iface):
        super(QgsAccessControlFilter, self).__init__(server_iface)

    def _get_user(self):
        username = None
        QgsMessageLog.logMessage("##### READING AUTHENTICATED USER #####")
        auth = self.serverInterface().getEnv('HTTP_AUTHORIZATION')
        if not auth:
            QgsMessageLog.logMessage("# NOT AUTH, SEARCHING IN request #")
            auth = self.serverInterface().requestHandler().requestHeader('HTTP_AUTHORIZATION')
        if auth:
            username, password = base64.b64decode(auth[6:]).split(b':')
            username = username.decode("utf-8")
            QgsMessageLog.logMessage("# {}:{} #".format(username, password))

        QgsMessageLog.logMessage("##### FINISHED READING #####")
        return username

    def layerFilterExpression(self, layer):
        """ Return an additional expression filter """
        username = self._get_user()
        if username in ROLES:
            role = ROLES[username]
            permissions = PERMISSIONS[role]
            if layer.name() in permissions:
                layer_permissions = permissions[layer.name()]
                if "features" in layer_permissions and 'expression' in layer_permissions["features"]:
                    QgsMessageLog.logMessage("# Expression: {} #".format(layer_permissions["features"]["expression"]))
                    return layer_permissions["features"]["expression"]

        # return super(RestrictedAccessControlWithUsers, self).layerFilterExpression(layer)
        return "1 = 2" # No access for users not belonging to any role

    def layerFilterSubsetString(self, layer):
        """ Return an additional subset string (typically SQL) filter """
        username = self._get_user()
        if username in ROLES:
            role = ROLES[username]
            permissions = PERMISSIONS[role]
            if layer.name() in permissions:
                layer_permissions = permissions[layer.name()]
                if "features" in layer_permissions and 'sql' in layer_permissions["features"]:
                    if role == "propietarios":
                        return layer_permissions["features"]["sql"].format(PROPIETARIOS[username]['cc'])
                    else:
                        return layer_permissions["features"]["sql"]

        # return super(RestrictedAccessControlWithUsers, self).layerFilterSubsetString(layer)
        return "1 = 2" # No access for users not belonging to any role        

    def layerPermissions(self, layer):
        """ Return the layer rights """
        username = self._get_user()
        QgsMessageLog.logMessage("# Layer {} #".format(layer.name()))
        rights = QgsAccessControlFilter.LayerPermissions()
        if username in ROLES:
            role = ROLES[username]
            permissions = PERMISSIONS[role]
            if layer.name() in permissions:
                layer_permissions = permissions[layer.name()]
                if "rights" in layer_permissions:
                    rights.canRead = layer_permissions["rights"]["read"]
                    rights.canInsert = layer_permissions["rights"]["insert"]
                    rights.canUpdate = layer_permissions["rights"]["update"]
                    rights.canDelete = layer_permissions["rights"]["delete"]
                    return rights

        # return super(RestrictedAccessControlWithUsers, self).layerPermissions(layer)
        rights.canRead = rights.canInsert = rights.canUpdate = rights.canDelete = False
        return rights # No access for users not belonging to any role        

    def authorizedLayerAttributes(self, layer, attributes):
        """ Return the authorised layer attributes """
        username = self._get_user()
        if username in ROLES:
            role = ROLES[username]
            permissions = PERMISSIONS[role]
            if layer.name() in permissions:
                layer_permissions = permissions[layer.name()]
                if "attributes" in layer_permissions:
                    if 'all' in layer_permissions["attributes"]:
                        return attributes
                    elif 'these' in layer_permissions["attributes"]:
                        return layer_permissions["attributes"]["these"]
                    elif 'remove' in layer_permissions["attributes"]:
                        return list(set(attributes) - set(layer_permissions["attributes"]["remove"]))
                
        # return super(RestrictedAccessControlWithUsers, self).authorizedLayerAttributes(layer, attributes)
        return [] # No access for users not belonging to any role        

    def allowToEdit(self, layer, feature):
        """ Are we authorise to modify the following geometry """
        # return super(RestrictedAccessControlWithUsers, self).allowToEdit(layer, feature)
        return False # No access for users not belonging to any role

    def cacheKey(self):
        return super(RestrictedAccessControlWithUsers, self).cacheKey()


class AccessControl:
    def __init__(self, serverIface):
        # Save reference to the QGIS server interface
        serverIface.registerAccessControl( RestrictedAccessControlWithUsers(serverIface), 100 )
        #serverIface.registerFilter( HTTPBasicFilter(serverIface), 10 )

