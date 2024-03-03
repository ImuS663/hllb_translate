import click
from transformers import Pipeline


class Text:
    @classmethod
    def translate(cls, translater: Pipeline):
        while True:
            text = input('Enter text: ')

            result = translater(text)[0]['translation_text']
            click.echo(result)
