import tqdm
import sys
import click
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
@click.option('-b', '--batch-size', type=int, default=6, show_default=True, help='Change batch size.')
@click.option('-c', '--cache-dir', type=Path, default=Path('.cache'), show_default=True, help='Change cache dir')
@click.option('-d', '--device', type=click.Choice(['cpu', 'cuda'], case_sensitive=False),
              default='cpu', show_default=True, help='Choose device.')
@click.option('-o', '--output-dir', type=Path, default=Path('output'), show_default=True, help='Change output dir')
def main(file_path, source_lang, target_lang, batch_size, cache_dir, device, output_dir):

    output_dir.mkdir(parents=True, exist_ok=True)

    tokenizer, model = transformer.load_model(cache_dir)

    translator = transformer.pipe(tokenizer, model, source_lang, target_lang, batch_size, device)

    with open(Path('output', file_path.name), 'w', encoding='utf8') as file:
        for result in tqdm.tqdm(translator(read(file_path)), desc=f'Translate: {file_path}',
                                total=file_count(file_path), unit='row'):
            file.write(result[0]['translation_text'] + '\n')


if __name__ == '__main__':
    sys.exit(main())
