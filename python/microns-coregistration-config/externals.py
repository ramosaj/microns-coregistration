from pathlib import Path

# TODO: place in microns-utils
def make_store_dict(path):
    return {
        'protocol': 'file',
        'location': str(path),
        'stage': str(path)
    }

minnie_em_external_stack_path = Path() / '/mnt' / 'dj-stor01' / 'microns'/ 'minnie' / 'stacks'

minnie_em = {
    'stacks': make_store_dict(minnie_em_external_stack_path)
    }