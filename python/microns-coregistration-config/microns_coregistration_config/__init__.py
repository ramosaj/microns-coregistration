"""
Configuration package/module for microns-coregistration.
"""

from . import adapters
from . import externals

import traceback

try:
    import datajoint as dj
except:
    traceback.print_exc()
    raise ImportError('DataJoint package not found.')

# Also important to run the dj flags at SOME point during normal datajoint initialization, probably don't want to have this in every config though?

# TODO: place in microns-utils
def enable_datajoint_flags(enable_python_native_blobs=True):
    """
    Enable experimental datajoint features
    
    These flags are required by 0.12.0+ (for now).
    """
    dj.config['enable_python_native_blobs'] = enable_python_native_blobs
    dj.errors._switch_filepath_types(True)
    dj.errors._switch_adapted_types(True)
    
enable_datajoint_flags()

# IMPORTANT: You can organize several schemas' config files (or folders) however you want as long as
# the correct schema configurations are plugged in for the enum variations (obviously).

from enum import Enum

class SCHEMAS(Enum):
    MINNIE_EM = 'microns_minnie_em'


def register_externals(schema_name:str=None, stores_config:dict=None):
    """
    TODO: Check logic/ add validation if passing both stores_config and schema_name

    Registers the external stores for a schema_name in this module.
    """
    if schema_name is None and stores_config is None:
        raise Exception("Either schema_name or stores_config must be set")

    if schema_name is not None: 
        stores_config = externals_mapping[schema_name]

    if 'stores' not in dj.config:
        dj.config['stores'] = stores_config
    else:
        dj.config['stores'].update(stores_config)


def register_adapters(schema_name:str=None, adapter_objects:dict=None, context=None):
    """
    TODO: Check logic/ add validation if passing both stores_config and schema_name

    Imports the adapters for a schema_name into the global namespace.
    
    This function is probably not necessary, but standardization is nice.
    """
    if schema_name is None and adapter_objects is None:
        raise Exception("Either schema_name or adapter_objects must be set")

    if schema_name is not None: 
        adapter_objects = adapters_mapping[schema_name]
    
    if context is None:
        # if context is missing, use the calling namespace
        import inspect
        frame = inspect.currentframe().f_back
        context = frame.f_locals
        del frame
    
    for name, adapter in adapter_objects.items():
        context[name] = adapter

# Typing annotation hints not strictly necessary. This import is also not necessary if you only specify one type.
from typing import Union

config_mapping = {
    SCHEMAS.MINNIE_EM: {
        "externals": externals.minnie_em,
        "adapters": None
    }
}

adapters_mapping = {
    'microns_minnie_em': config_mapping[SCHEMAS.MINNIE_EM]["adapters"]
}

externals_mapping = {
    'microns_minnie_em': config_mapping[SCHEMAS.MINNIE_EM]["externals"]
}

# def create_vm(schema: Union[SCHEMAS, str]):
#     """
#     Creates a virtual module after registering the external stores, and includes the adapter objects in the vm.
#     """
    
#     # Steps that create_vm should take for each schema:
#     # 1. Register externals with dj.config
#     # 2. Choose which schema's config to load.
#     # 3. Load a dict with the relevant adapters into the adapter object field of a virtual module.
    
#     schema = SCHEMAS(schema)
    
#     mapping = config_mapping[schema]
#     externals = mapping['externals']
#     if externals is not None:
#         register_externals(externals)
#     schema_name = schema.value
#     return dj.create_virtual_module(schema_name, schema_name, add_objects=mapping['adapters'])

def create_vm(schema_name:str):
    """
    Creates a virtual module after registering the external stores, and includes the adapter objects in the vm.
    """
    
    # Steps that create_vm should take for each schema:
    # 1. Register externals with dj.config
    # 2. Choose which schema's config to load.
    # 3. Load a dict with the relevant adapters into the adapter object field of a virtual module.
    if externals is not None:
        register_externals(schema_name)
    
    return dj.create_virtual_module(schema_name, schema_name, add_objects=adapters_mapping[schema_name])