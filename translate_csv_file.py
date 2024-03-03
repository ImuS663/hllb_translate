import csv
import tqdm
from pathlib import Path
from typing import Generator, Any
from transformers import Pipeline


class Csv:
    @staticmethod
    def __read_col(file: Path, column_number: int) -> Generator[str, Any, None]:
        for row in csv.reader(open(file, 'r', encoding='utf8')):
            yield row[column_number]

    @staticmethod
    def __read(file: Path) -> Generator[list[str], Any, None]:
        for row in csv.reader(open(file, 'r', encoding='utf8')):
            yield row

    @staticmethod
    def __file_count(file: Path) -> int:
        with open(file, 'r') as file:
            num_lines = sum(1 for _ in csv.reader(file))
        return num_lines

    @classmethod
    def translate(cls, file: Path, column: int, output_dir: Path, translater: Pipeline):
        with open(output_dir / file.name, 'w', encoding='utf8') as out_file:
            writer = csv.writer(out_file, lineterminator='\n')
            for (result, row) in tqdm.tqdm(zip(translater(cls.__read_col(file, column)), cls.__read(file)),
                                           desc=f'Translate: {file}', total=cls.__file_count(file), unit='row'):
                row[column] = result[0]['translation_text']
                writer.writerow(row)
