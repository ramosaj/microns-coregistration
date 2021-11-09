from pathlib import Path

# TODO: place in microns-utils
def make_store_dict(path):
    return {
        'protocol': 'file',
        'location': str(path),
        'stage': str(path)
    }

base_path = Path() / '/mnt' / 'dj-stor01' / 'microns'

minnie_em = {
    'stacks': make_store_dict(base_path / 'minnie' / 'stacks')
}