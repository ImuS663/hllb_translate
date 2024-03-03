import tqdm
from pathlib import Path
from typing import Generator, Any
from transformers import Pipeline


class Txt:
    @staticmethod
    def __read(file_name: Path) -> Generator[str, Any, None]:
        for row in open(file_name, 'r', encoding='utf8'):
            yield row

    @staticmethod
    def __file_count(file_name: Path) -> int:
        with open(file_name, 'rb') as file:
            num_lines = sum(1 for _ in file)
        return num_lines

    @classmethod
    def translate(cls, file: Path, output_dir: Path, translater: Pipeline):
        with open(output_dir / file.name, 'w', encoding='utf8') as out_file:
            for result in tqdm.tqdm(translater(cls.__read(file)), desc=f'Translate: {file}',
                                    total=cls.__file_count(file), unit='row'):
                out_file.write(result[0]['translation_text'] + '\n')

