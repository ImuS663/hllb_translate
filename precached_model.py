import sys
import read_config

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def main():
    model_name = sys.argv[1]

    config = read_config.read('config.json')
    
    print('Start load:', model_name)

    AutoTokenizer.from_pretrained(model_name, cache_dir=config.cache_dir)
    AutoModelForSeq2SeqLM.from_pretrained(model_name, cache_dir=config.cache_dir)

    input('Load completed, press any key...')


if __name__ == '__main__':
    sys.exit(main())
