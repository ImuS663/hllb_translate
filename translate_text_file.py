import tqdm
import sys
import read_config

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from pathlib import Path


def read(file_name: str):
    for row in open(file_name, 'r', encoding='utf8'):
        yield row


def file_count(file_name: str):
    with open(file_name, 'rb') as file:
        num_lines = sum(1 for _ in file)
    return num_lines


def main():
    file_path = sys.argv[1]
    source_lang = sys.argv[2]
    target_lang = sys.argv[3]

    config = read_config.read('config.json')

    output_path = Path(config.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(config.model_name, cache_dir=config.cache_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(config.model_name, cache_dir=config.cache_dir)

    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=source_lang,
                          tgt_lang=target_lang, max_length=400, device=config.device, batch_size=config.batch_size)

    with open(Path('output', Path(file_path).name), 'w', encoding='utf8') as file:
        for result in tqdm.tqdm(translator(read(file_path)), desc='Translate: ' + file_path,
                                total=file_count(file_path), unit='row'):
            file.write(result[0]['translation_text'] + '\n')


if __name__ == '__main__':
    sys.exit(main())
