from pathlib import Path
from microns_utils import config_utils

base_path = Path() / '/mnt' / 'dj-stor01' / 'microns'
minnie_stack_path = base_path / 'minnie' / 'stacks'

minnie_em = {
    'stacks': config_utils.make_store_dict(minnie_stack_path)
}

minnie65_auto_match = {
    'stacks': config_utils.make_store_dict(minnie_stack_path)
}

minnie65_coregistration = {
    'stacks': config_utils.make_store_dict(minnie_stack_path)
}

minnie65_manual_match = {
    'stacks': config_utils.make_store_dict(minnie_stack_path)
}