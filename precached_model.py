import json
import sys

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def main():
    with open('config.json') as config_file:
        data = json.load(config_file)

    model_name = sys.argv[1]

    cache_dir = data['cache_dir']
    
    print('Start load:', model_name)

    AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
    AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=cache_dir)

    input('Load completed, press any key...')


if __name__ == '__main__':
    sys.exit(main())
