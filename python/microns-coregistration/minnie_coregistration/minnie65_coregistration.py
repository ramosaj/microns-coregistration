import datajoint as dj
import numpy as np
import pandas as pd
import json

import microns_coregistration_config as config
schema_name = 'microns_minnie65_coregistration'

config.register_adapters(schema_name, context=locals())
config.register_externals(schema_name)

schema = dj.schema(schema_name)
# schema.spawn_missing_classes()
