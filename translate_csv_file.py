import tqdm
import sys
import csv
import click
import read_config
import transformer

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


@click.command()
@click.argument('file_path', type=str)
@click.argument('column_number', type=int)
@click.argument('source_lang', type=str)
@click.argument('target_lang', type=str)
def main(file_path, column_number, source_lang, target_lang):
    config = read_config.read('config.json')

    output_path = Path(config.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    tokenizer, model = transformer.load_model(config)

    translator = transformer.pipe(tokenizer, model, config, source_lang, target_lang)

    with open(Path('output', Path(file_path).name), 'w', encoding='utf8') as file:
        writer = csv.writer(file, lineterminator='\n')
        for (result, row) in tqdm.tqdm(zip(translator(read_col(file_path, column_number)), read(file_path)),
                                       desc='Translate: ' + file_path, total=file_count(file_path), unit='row'):
            row[column_number] = result[0]['translation_text']
            writer.writerow(row)


if __name__ == '__main__':
    sys.exit(main())
