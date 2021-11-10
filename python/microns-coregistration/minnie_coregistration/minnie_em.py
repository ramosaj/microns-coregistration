import datajoint as dj
import numpy as np
import pandas as pd
import json

from microns_coregistration_api import config
schema_name = 'microns_minnie_em'

config.register_adapters(schema_name, context=locals())
config.register_externals(schema_name)

schema = dj.schema(schema_name)
schema.spawn_missing_classes()