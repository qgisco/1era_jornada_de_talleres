# -*- coding: utf-8 -*-

def serverClassFactory(serverIface):
    from .hello_server import HelloServer
    return HelloServer(serverIface)
