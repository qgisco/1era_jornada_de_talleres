LAYER_TERRENO = "terreno"
LAYER_CONSTRUCCION = "construccion"
ADMIN_R = "Administrativo_R_Escala_1500.000_Cartografia_Base__IGAC"

PERMISSIONS = {
  "propietarios": {    # Acceso a toda la info de su predio y a los polígonos de terreno a nivel de referencia
      LAYER_TERRENO: {
        'features': {'sql': ' "predio_documento_identidad" = \'{}\' '},
        'attributes': {'all': True},
        'rights': {'read': True, 'insert': False, 'update': False, 'delete': False} 
      },        
      LAYER_CONSTRUCCION: {
        'features': {'sql': ' "predio_documento_identidad" = \'{}\' '},
        'attributes': {'all': True},
        'rights': {'read': True, 'insert': False, 'update': False, 'delete': False} 
      }
  },
  "igac": {    # Acceso a toda la info catastral
      LAYER_TERRENO: {
        'features': {'all': True},
        'attributes': {'all': True},
        'rights': {'read': True, 'insert': True, 'update': True, 'delete': True} 
      },        
      LAYER_CONSTRUCCION: {
        'features': {'all': True},
        'attributes': {'all': True},
        'rights': {'read': True, 'insert': True, 'update': True, 'delete': True} 
      }
  },
  "snr": {    # Acceso a toda la info registral
      LAYER_TERRENO: {
        'features': {'all': True},
        'attributes': {'remove': ['avaluo_terreno', 'predio_avaluo_predio']},
        'rights': {'read': True, 'insert': False, 'update': False, 'delete': False} 
      },        
      LAYER_CONSTRUCCION: {
        'features': {'all': True},
        'attributes': {'remove': ['avaluo_construccion']},
        'rights': {'read': True, 'insert': False, 'update': False, 'delete': False}
      }
  },
  "proyectos": {   # Acceso a polígonos y avalúos para determinar costos de adquisición de predios
      LAYER_TERRENO: {
        'rights': {'read': False, 'insert': False, 'update': False, 'delete': False} 
      },        
      LAYER_CONSTRUCCION: {
        'features': {'all': True},
        'attributes': {'these': ['avaluo_construccion']},
        'rights': {'read': True, 'insert': False, 'update': False, 'delete': False} 
      }
  },
  "otros":{  # Acceso a los polígonos de terreno y construcción sin mayor info alfanumérica
      LAYER_TERRENO: {
        'features': {'all': True},
        'attributes': {'these': ['fid']},
        'rights': {'read': True, 'insert': False, 'update': False, 'delete': False} 
      },        
      LAYER_CONSTRUCCION: {
        'features': {'all': True},
        'attributes': {'these': ['fid']},
        'rights': {'read': True, 'insert': False, 'update': False, 'delete': False}
      },
      ADMIN_R: {
        #'features': {'sql': ' "FID" = \'193\' '},
        'features': {'expression': "intersects_bbox( $geometry, geom_from_wkt('LINESTRING(-76 4.7, -75.6 5)' ) )"},
        'attributes': {'remove': ["PROYECTO", "FECHA", "GLOBALID"]},
        'rights': {'read': True, 'insert': False, 'update': False, 'delete': False} 
      }
  }
}


ROLES = {
  "pedro": "propietarios",
  "pablo": "propietarios",
  "irene": "igac",
  "isabel": "igac",
  "sandra": "snr",
  "XYZ": "proyectos",
  "invitado": "otros",
  "germap": "otros"
}


PROPIETARIOS = {
  "pedro": {'cc': 80199143},
  "pablo": {'cc': 1000123456}
}
