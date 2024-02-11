import json


class Config:
    cache_dir: str
    model_name: str
    device: str
    batch_size: int
    output_dir: str

    def __init__(self, cache_dir, model_name, device, batch_size, output_dir):
        self.cache_dir = cache_dir
        self.model_name = model_name
        self.device = device
        self.batch_size = batch_size
        self.output_dir = output_dir


def read(path: str) -> Config:
    with open('config.json') as config_file:
        data = json.load(config_file)

    return Config(data['cache_dir'], data['model_name'], data['device'], data['batch_size'], data['output_dir'])
