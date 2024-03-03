import csv
import click
from tabulate import tabulate


class Languages:
    @staticmethod
    def __read_lang() -> list[list[str]]:
        filename = 'languages.csv'
        with open(filename, mode='r', encoding='utf-8') as file:
            return list(csv.reader(file))

    @staticmethod
    def __print(langs: list[list[str]]) -> None:
        tab = tabulate(langs, headers=('Language', ' FLORES-200 code'), tablefmt='presto', colalign=('left', 'center'))

        click.echo(tab)

    @classmethod
    def print_all(cls) -> None:
        langs = cls.__read_lang()

        if len(langs) == 0:
            click.echo('Nothing found!')
            exit()

        cls.__print(langs)

    @classmethod
    def find(cls, text: str) -> None:
        result: list[list[str]] = []

        langs = cls.__read_lang()

        for lang in langs:
            if lang[0].find(text) != -1 or lang[1].find(text) != -1:
                result.append(lang)

        if len(result) == 0:
            click.echo('Nothing found!')
            exit()

        cls.__print(result)

    @classmethod
    def get_lang_name(cls, lang_code: str) -> str:
        langs = cls.__read_lang()

        lang_name = ''

        for lang in langs:
            if lang[1] == lang_code:
                lang_name = lang[0]

        return lang_name
