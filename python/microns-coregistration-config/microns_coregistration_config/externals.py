from pathlib import Path

# TODO: place in microns-utils
def make_store_dict(path):
    return {
        'protocol': 'file',
        'location': str(path),
        'stage': str(path)
    }

base_path = '/mnt' / 'dj-stor01' / 'microns'

minnie_em = {
    'stacks': make_store_dict(Path() / base_path / 'minnie' / 'stacks')
}