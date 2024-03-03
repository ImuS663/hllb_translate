import sys
import click
import transformer
from pathlib import Path
from translate_text import Text
from translate_txt_file import Txt
from translate_csv_file import Csv
from translate_lang import Languages


def check_langs(source_code: str, target_code: str) -> None:
    source = Languages.get_lang_name(source_code)
    target = Languages.get_lang_name(target_code)

    is_incorrect = False

    if source == '':
        click.echo(click.style('Error: ', fg='red') + 'Incorrect source language code!', err=True)
        is_incorrect = True

    if target == '':
        click.echo(click.style('Error: ', fg='red') + 'Incorrect target language code!', err=True)
        is_incorrect = True

    if is_incorrect:
        exit()

    click.echo(f'Translate: {click.style(source, fg="green")} -> {click.style(target, fg="green")}')


def check_file(file_path: Path) -> None:
    if not file_path.is_file():
        click.echo(click.style('Error: ', fg='red') + 'Incorrect path to file!', err=True)
        exit()


@click.group()
def cli():
    """Translate CLI"""


@cli.command('text')
@click.argument('source', type=str)
@click.argument('target', type=str)
@click.option('-c', '--cache-dir', type=Path, default=Path('.cache'), show_default=True, help='Change cache dir')
@click.option('-d', '--device', type=click.Choice(['CPU', 'CUDA'], case_sensitive=False),
              default='CPU', show_default=True, help='Choose device.')
def text(source: str, target: str, cache_dir: Path, device: str):
    """
    Translate string.

    SOURCE is the Source Language

    TARGET is the Target Language
    """
    check_langs(source, target)

    cache_dir.mkdir(parents=True, exist_ok=True)

    click.echo('Load model...')
    tokenizer, model = transformer.load_model(cache_dir)
    translater = transformer.pipe(tokenizer, model, source, target, 6, device)
    click.echo('Model loaded!')

    Text.translate(translater)


@cli.command('csv')
@click.argument('filename', type=Path)
@click.argument('column', type=int)
@click.argument('source', type=str)
@click.argument('target', type=str)
@click.option('-b', '--batch-size', type=int, default=6, show_default=True, help='Change batch size.')
@click.option('-c', '--cache-dir', type=Path, default=Path('.cache'), show_default=True, help='Change cache dir')
@click.option('-d', '--device', type=click.Choice(['CPU', 'CUDA'], case_sensitive=False),
              default='CPU', show_default=True, help='Choose device.')
@click.option('-o', '--output-dir', type=Path, default=Path('output'), show_default=True, help='Change output dir')
def csv_file(filename: Path, column: int, source: str, target: str, batch_size: int, cache_dir: Path,
             device: str, output_dir: Path):
    """
    Translate csv file.

    FILENAME is the path to target file.

    COLUMN is the number to target column.

    SOURCE is the Source Language

    TARGET is the Target Language
    """
    check_langs(source, target)

    check_file(filename)

    column -= 1

    cache_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    click.echo('Load model...')
    tokenizer, model = transformer.load_model(cache_dir)
    translater = transformer.pipe(tokenizer, model, source, target, batch_size, device)
    click.echo('Model loaded!')

    click.echo('Start translate.')
    Csv.translate(filename, column, output_dir, translater)
    click.echo(click.style('Translate complete!', fg='green'))


@cli.command('txt')
@click.argument('filename', type=Path)
@click.argument('source', type=str)
@click.argument('target', type=str)
@click.option('-b', '--batch-size', type=int, default=6, show_default=True, help='Change batch size.')
@click.option('-c', '--cache-dir', type=Path, default=Path('.cache'), show_default=True, help='Change cache dir')
@click.option('-d', '--device', type=click.Choice(['CPU', 'CUDA'], case_sensitive=False),
              default='CPU', show_default=True, help='Choose device.')
@click.option('-o', '--output-dir', type=Path, default=Path('output'), show_default=True, help='Change output dir')
def txt_file(filename: Path, source: str, target: str, batch_size: int, cache_dir: Path,
             device: str, output_dir: Path):
    """
    Translate txt file.

    FILENAME is the path to target file.

    SOURCE is the Source Language

    TARGET is the Target Language
    """
    check_langs(source, target)

    check_file(filename)

    cache_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    click.echo('Load model...')
    tokenizer, model = transformer.load_model(cache_dir)
    translater = transformer.pipe(tokenizer, model, source, target, batch_size, device)
    click.echo('Model loaded!')

    click.echo('Start translate.')
    Txt.translate(filename, output_dir, translater)
    click.echo(click.style('Translate complete!', fg='green'))


@cli.command('langs')
@click.option('-f', '--find', type=str, default='', help='Find language.')
def lang_all(find: str):
    """Print all supported languages."""
    if find == '':
        Languages.print_all()
    else:
        Languages.find(find)


if __name__ == '__main__':
    sys.exit(cli())
