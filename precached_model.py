import sys
import click
import transformer

from pathlib import Path


@click.command()
@click.option('-c', '--cache-dir', type=Path, default=Path('.cache'), show_default=True, help='Change cache dir')
def main(cache_dir):
    model_name = sys.argv[1]
    
    print('Start load:', model_name)

    transformer.load_model(cache_dir)

    input('Load completed, press any key...')


if __name__ == '__main__':
    sys.exit(main())
