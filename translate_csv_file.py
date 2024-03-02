import tqdm
import sys
import csv
import click
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
@click.argument('file_path', type=Path)
@click.argument('column_number', type=int)
@click.argument('source_lang', type=str)
@click.argument('target_lang', type=str)
@click.option('-b', '--batch-size', type=int, default=6, show_default=True, help='Change batch size.')
@click.option('-c', '--cache-dir', type=Path, default=Path('.cache'), show_default=True, help='Change cache dir')
@click.option('-d', '--device', type=click.Choice(['cpu', 'cuda'], case_sensitive=False),
              default='cpu', show_default=True, help='Choose device.')
@click.option('-o', '--output-dir', type=Path, default=Path('output'), show_default=True, help='Change output dir')
def main(file_path, column_number, source_lang, target_lang, batch_size, cache_dir, device, output_dir):

    column_number -= 1

    output_dir.mkdir(parents=True, exist_ok=True)

    tokenizer, model = transformer.load_model(cache_dir)

    translator = transformer.pipe(tokenizer, model, source_lang, target_lang, batch_size, device)

    with open(Path('output', file_path.name), 'w', encoding='utf8') as file:
        writer = csv.writer(file, lineterminator='\n')
        for (result, row) in tqdm.tqdm(zip(translator(read_col(file_path, column_number)), read(file_path)),
                                       desc=f'Translate: {file_path}', total=file_count(file_path), unit='row'):
            row[column_number] = result[0]['translation_text']
            writer.writerow(row)


if __name__ == '__main__':
    sys.exit(main())
