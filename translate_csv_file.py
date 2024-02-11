import tqdm
import sys
import csv
import read_config

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline, Pipeline
from pathlib import Path


def read_col(file_name: str, column_number: int):
    for row in csv.reader(open(file_name, 'r', encoding='utf8')):
        yield row[column_number]


def read(file_name: str):
    for row in csv.reader(open(file_name, 'r', encoding='utf8')):
        yield row


def file_count(file_name: str):
    with open(file_name, 'r') as file:
        num_lines = sum(1 for _ in csv.reader(file))
    return num_lines


def main():
    file_path = sys.argv[1]
    column_number = int(sys.argv[2])
    source_lang = sys.argv[3]
    target_lang = sys.argv[4]

    config = read_config.read('config.json')

    output_path = Path(config.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(config.model_name, cache_dir=config.cache_dir)
    model = AutoModelForSeq2SeqLM.from_pretrained(config.model_name, cache_dir=config.cache_dir)

    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang=source_lang,
                          tgt_lang=target_lang, max_length=400, device=config.device, batch_size=config.batch_size)

    with open(Path('output', Path(file_path).name), 'w', encoding='utf8') as file:
        writer = csv.writer(file, lineterminator='\n')
        for (result, row) in tqdm.tqdm(zip(translator(read_col(file_path, column_number)), read(file_path)),
                                       desc='Translate: ' + file_path, total=file_count(file_path), unit='row'):
            row[column_number] = result[0]['translation_text']
            writer.writerow(row)


if __name__ == '__main__':
    sys.exit(main())
