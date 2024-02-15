import sys
import click
import read_config
import transformer


@click.command()
@click.argument('source_lang', type=str)
@click.argument('target_lang', type=str)
def main(source_lang, target_lang):

    config = read_config.read('config.json')

    tokenizer, model = transformer.load_model(config)

    translator = transformer.pipe(tokenizer, model, config, source_lang, target_lang)

    is_exit = False

    while not is_exit:
        text = input('Enter text: ')

        if text == 'exit()':
            is_exit = True
            print('Exit!')
        elif text == 'change_lang()':
            source_lang = input('Enter source: ')
            target_lang = input('Enter target: ')

            translator = transformer.pipe(tokenizer, model, config, source_lang, target_lang)
        else:
            result = translator(text)[0]['translation_text']
            print(result)


if __name__ == '__main__':
    sys.exit(main())
