import tqdm
import sys
import click
import read_config
import transformer

from pathlib import Path


def read(file_name: str):
    for row in open(file_name, 'r', encoding='utf8'):
        yield row


def file_count(file_name: str):
    with open(file_name, 'rb') as file:
        num_lines = sum(1 for _ in file)
    return num_lines


@click.command()
@click.argument('file_path', type=Path)
@click.argument('source_lang', type=str)
@click.argument('target_lang', type=str)
def main(file_path, source_lang, target_lang):
    config = read_config.read('config.json')

    output_path = Path(config.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    tokenizer, model = transformer.load_model(config)

    translator = transformer.pipe(tokenizer, model, config, source_lang, target_lang)

    with open(Path('output', file_path.name), 'w', encoding='utf8') as file:
        for result in tqdm.tqdm(translator(read(file_path)), desc='Translate: ' + file_path,
                                total=file_count(file_path), unit='row'):
            file.write(result[0]['translation_text'] + '\n')


if __name__ == '__main__':
    sys.exit(main())
