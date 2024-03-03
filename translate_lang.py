import sys
import csv
import click
import tabulate


@click.group()
def main():
    print()


@main.command('list', help='Print all languages.')
def list_all():
    with open('languages.csv') as file:
        reader = csv.reader(file)
        print(tabulate.tabulate(reader, headers=('Language', ' FLORES-200 code'),
                                tablefmt='presto', colalign=('left', 'center')))


@main.command('find', help='Print language languages.')
@click.argument('lang', type=str)
def list_all(lang):
    with open('languages.csv') as file:
        reader = csv.reader(file)
        ex = []

        for row in reader:
            if row[0].lower().find(lang) != -1:
                ex.append(row)

        if len(ex) == 0:
            print('Nothing found!')
            exit()

        print(tabulate.tabulate(ex, headers=('Language', ' FLORES-200 code'),
                                tablefmt='presto', colalign=('left', 'center')))


if __name__ == '__main__':
    sys.exit(main())
