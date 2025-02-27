import pathlib

root_dir = pathlib.Path(__file__).parent.parent.parent
cache_dir = root_dir / ".cache"
cache_dir.mkdir(exist_ok=True)
