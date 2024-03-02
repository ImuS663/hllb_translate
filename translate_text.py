import sys
import click
import transformer

from pathlib import Path


@click.command()
@click.argument('source_lang', type=str)
@click.argument('target_lang', type=str)
@click.option('-c', '--cache-dir', type=Path, default=Path('.cache'), show_default=True, help='Change cache dir')
@click.option('-d', '--device', type=click.Choice(['cpu', 'cuda'], case_sensitive=False),
              default='cpu', show_default=True, help='Choose device.')
def main(source_lang, target_lang, cache_dir, device):

    tokenizer, model = transformer.load_model(cache_dir)

    translator = transformer.pipe(tokenizer, model, source_lang, target_lang, 6, device)

    is_exit = False

    while not is_exit:
        text = input('Enter text: ')

        if text == 'exit()':
            is_exit = True
            print('Exit!')
        elif text == 'change_lang()':
            source_lang = input('Enter source: ')
            target_lang = input('Enter target: ')

            translator = transformer.pipe(tokenizer, model, source_lang, target_lang, 6, device)
        else:
            result = translator(text)[0]['translation_text']
            print(result)


if __name__ == '__main__':
    sys.exit(main())
